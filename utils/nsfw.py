def femboynsfw():
    import requests
    import json, os
    import colorama
    import time
    from colorama import Fore, init
    from concurrent.futures import ThreadPoolExecutor

    colorama.init
    Pink = Fore.LIGHTMAGENTA_EX
    Reset = Fore.RESET
    pid = 1  # starting page
    tags = input('''Which one did you want ? :

    [1] Astolfo
    [2] Felix''')

    if tags == '1':
        tags = 'astolfo_%28fate%29'
    elif tags == '2':
        tags = 'felix_argyle'

    if not os.path.exists('FemboyNSFW'):
        os.makedirs('FemboyNSFW')

    def download_image(post):
        file_url = post['file_url']
        id = post['id']
        extension = file_url.split(".")[-1]
        filename = f"FemboyNSFW/{id}.{extension}"
        response = requests.get(file_url)
        with open(filename, 'wb') as f:
            f.write(response.content)
            print(f'{Pink}{filename}{Reset} Downloaded {Pink}:3{Reset} ')

    while True:
        url = f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags={tags}&pid={pid}&json=1"
        response = requests.get(url)
        data = json.loads(response.content)

        if not data['post']:
            # No more posts on this page, stop looping
            break

        with ThreadPoolExecutor(max_workers=16) as executor:
            futures = [executor.submit(download_image, post) for post in data['post']]
            for future in futures:
                future.result()

        pid += 1  # Move on to the next page
