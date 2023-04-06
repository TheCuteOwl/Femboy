def Baka():
    import time
    import requests
    import json
    import os
    import colorama
    from colorama import Fore, init
    import shutil, sys, subprocess
    colorama.init()
    while True:
        def input_centered(prompt):
            console_width, _ = shutil.get_terminal_size()
            prompt_lines = prompt.split('\n')
            padding = (console_width - max(len(line) for line in prompt_lines)) // 2
            centered_prompt = '\n'.join(' ' * padding + line for line in prompt_lines)
            user_input = input(centered_prompt)
            return user_input


        def clear_console():
            if sys.platform.startswith('win'):
                _ = subprocess.call('cls', shell=True)
            elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                _ = subprocess.call('clear', shell=True)
            else:
                print('Unsupported platform. Cannot clear console.')
        def print_centered(text):
            console_width, _ = shutil.get_terminal_size()
            for line in text.split('\n'):
                padding = (console_width - len(line)) // 2
                print(' ' * padding + line + ' ' * (console_width - padding - len(line)))

        def download():
            # Send requests to catboys API
                url = 'https://api.catboys.com/baka'
                response = requests.get(url)

                # Get the JSON response, get the URL from the JSON, generate the filename, and get the image data
                data = json.loads(response.content)
                image_url = data["url"]
                filename = os.path.join(os.path.basename(image_url))
                filename = filename.replace('image', 'Baka')
                filename = f'Baka/{filename}'

                # Download the file if it doesn't exist already
                if not os.path.exists(filename):
                    img_data = requests.get(image_url).content

                    # Download the file
                    with open(filename, 'wb') as f:
                        f.write(img_data)
                        print(f'{Pink}{filename}{Reset} Downloaded {Pink}:3{Reset} ')
        Pink = Fore.LIGHTMAGENTA_EX
        Reset = Fore.RESET
        print_centered(f'''{Pink}
        How{Reset} many {Pink}Baka{Reset} Gif you want to {Pink}download{Reset}
        [{Pink}1{Reset}] {Pink}All{Reset} of them ({Pink}11{Reset})
        [{Pink}2{Reset}] {Pink}Specific{Reset} Number{Reset}
        [{Pink}3{Reset}] {Pink}Go{Reset} Back''')
        choice = input_centered(f'{Pink}->{Reset} ')
        if not os.path.exists('Baka'):
                    os.makedirs('Baka')

        if choice == '1':
            clear_console()
            while True:
                download()
        elif choice == '2':
            clear_console()
            print_centered(f'{Pink}How{Reset} many {Pink}Baka{Reset} Gif you want to {Pink}download{Reset}')
            try:
                a = input_centered('-> ')
                clear_console()
                for x in range(int(a)):
                    download()
                clear_console()
            except:
                 continue
            break

        elif choice == '3':
            break
        else: 
            clear_console()
            print_centered(f'{Pink}Choose{Reset} between {Pink}1{Reset} and {Pink}2{Reset} and {Pink}3{Reset}')
            time.sleep(1)
            clear_console()

