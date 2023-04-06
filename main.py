import sys, subprocess, time, colorama, shutil, keyboard
from colorama import Fore, init
from utils.Baka import Baka
from utils.CatBoy import Catboy
from utils.FemboyImage import femboy
from utils.nsfw import femboynsfw
colorama.init()

Pink = Fore.LIGHTMAGENTA_EX
Reset = Fore.RESET
def print_centered(text):
    console_width, _ = shutil.get_terminal_size()
    for line in text.split('\n'):
        padding = (console_width - len(line)) // 2
        print(' ' * padding + line)
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

keys_to_watch = ['enter', 'esc']

while True:
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    clear_console()
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    print_centered(f'''{Pink}                                                                                                                                                                                       
                      #@@@@@@@@@@,                                                                  
                  #@@/            @@@                         /@@@@*    *@@@@                       
                @@&                  @@                     @@                @@                    
               @@                      @                  @@                    @(                  
              (@                        @                @@                      @.                 
              (@                        @                @                        @                 
               @                        @                @                        @                 
               @@                      @  %              @@                      @                  
                 @                   ,&  @@    @@    @@   .@                    @                   
                   @@              @      %@@@@ @@@@,        @                @                     
                        .(@@@@.                                 (@                                  
                        
Press Enter or Escape to Continue{Pink}''')
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    clear_console()
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    
    print_centered(f'''                                                                                                                                                                                                                                             
    *@@@@/                                                                       
    %(       ,%@@&/.   ,%@@@( &                                                   
    .&                          @                  @/                  .#@@@(&     
    (,                          #                 .% ,@@@@@@@@@@@@%*          ,    
    ./                          &                 .(                          ,    
    %                         .                   @                         (     
    ,.                      /   @     ##     (    @                       *      
        ,.                  *     &&   @%@. ,@#      ./                    .       
            #            ,                              #.              *          
                                                            *%##.                
                                                                                    
                                                                                                        
Press Enter or Escape to Continue{Pink}''')
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    clear_console()
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break

    print_centered(f'''                                                                                                                                                                                                                                                                                                                                                                                                                         
    .@@#,                                                                          
    (,            ...,,,,,,.    #                                                  
    ./                          &                 .@@*                             
    %                         .                   @     .*(#%%%%%#(/****/#@@@     
    ,.                     /   @     ##     (    @                       *      
        ,.                 *     &&   @%@. ,@#      ./                    .       
            #            ,                             #.              *          
                                                            *%##.                
                                                                                                        
Press Enter or Escape to Continue{Pink}''')
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    clear_console()
    print_centered(f'''                                                                                                                                                                                                                                                                                                                                                                                                                   
    .@@                                                                            
    (, /@.                                                                         
    ./    @&                   (@(                                                 
    %      ,@(             #@..                                                   
    ,.       .@@%(/(%@@@%   /   @     ##     (   *@@@.                           
        ,.                  *     &&   @%@. ,@#      ./  ,@@&.          @@ .       
            #            ,                              #.      (@@@@@* *          
                                                            *%##.                
                                                                                    
                                                                                                            
Press Enter or Escape to Continue{Reset}''')
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break
    time.sleep(0.04)
    if any(keyboard.is_pressed(key) for key in keys_to_watch):
        break

clear_console()

input('')

while True:
    clear_console()
    print_centered(f'''
    {Pink}Choose what you want :3{Reset}

    [{Pink}1{Reset}] {Pink}Baka{Reset} Gif {Pink}Generator{Reset}
    [{Pink}2{Reset}] {Pink}Cat{Reset} Boy {Pink}Generator{Reset}
    [{Pink}3{Reset}] {Pink}Femboy{Reset} SFW {Pink}Generator{Reset}
    [{Pink}4{Reset}] {Pink}Femboy{Reset} NSFW {Pink}Generator{Reset}''')
    choice = input_centered('-> ')
    if choice == '1':
        clear_console()
        Baka()
    elif choice == '2':
        clear_console()
        Catboy()
    elif choice == '3':
        clear_console()
        femboy()
    elif choice == '4':
        clear_console()
        femboynsfw()
