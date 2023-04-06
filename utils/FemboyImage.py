def femboy():
    import requests
    import xml.etree.ElementTree as ET
    import os
    import colorama
    from colorama import Fore, init
    from concurrent.futures import ThreadPoolExecutor
    colorama.init()
    Pink = Fore.LIGHTMAGENTA_EX
    Reset = Fore.RESET
    pid = 1  # starting page
    tags = 'astolfo_%28fate%29'
    url = f'https://safebooru.org//index.php?page=dapi&s=post&q=index&tags={tags}&pid={pid}'
    response = requests.get(url)
    root = ET.fromstring(response.content)
    if not os.path.exists('Femboy'):
        os.makedirs('Femboy')
        
    def download_image(post):
        image_url = post.get('sample_url')
        post_id = post.get('id')
        ext = os.path.splitext(image_url)[1]
        filename = f'Femboy/{post_id}{ext}'
        img_data = requests.get(image_url).content
        if not os.path.exists(filename):
            # Download the file
            with open(filename, 'wb') as f:
                f.write(img_data)
                print(f'{Pink}{filename}{Reset} Downloaded {Pink}:3{Reset} ')

    while True:
        with ThreadPoolExecutor(max_workers=8) as executor:
            executor.map(download_image, root.findall('post'))
        line_count = len(root.findall('post'))
        if line_count == 0:
            input(f'ended - {url}')
            break
        pid += 1
        url = f'https://safebooru.org//index.php?page=dapi&s=post&q=index&tags={tags}&pid={pid}'
        response = requests.get(url)
        root = ET.fromstring(response.content)
