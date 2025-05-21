
from rich_sample import rich__ColorFont,rich_progress_sample1,rich_sample_Table,rich_markdown_sample,rich_syntax
# import os
# import sys
# from pyfiglet import Figlet
# import pyfiglet
from figletComponents import print_colored_figlet, print_colored_figlet_with_style, print_banner
from colorama import Fore, Style, init
# Initialize Colorama for cross-platform compatibility
init(autoreset=True) # autoreset ensures colors are reset after each print






def Run_rich():
    print('Lets running the App')
    print_colored_figlet_with_style("Important", font="isometric1", color=Fore.BLUE, style=Style.BRIGHT)
    print_banner()
    rich__ColorFont()
    rich_sample_Table()
    rich_progress_sample1()
    rich_markdown_sample()
    rich_syntax()
    print('App finished running')


# ----------------------------------
# FIGLET SAMPLE  
# -----------------------------------

# --- Examples ---
# print_colored_figlet("My Title", font="slant", color=Fore.RED)
# print_colored_figlet("Welcome!", font="block", color=Fore.YELLOW)
# print_colored_figlet("Console App", font="chunky", color=Fore.MAGENTA)
# print_colored_figlet_with_style("Important", font="isometric1", color=Fore.BLUE, style=Style.BRIGHT)

# # You can also combine colors and styles directly:
# print(Fore.CYAN + Style.BRIGHT + pyfiglet.figlet_format("Hello", font="standard") + Style.RESET_ALL)
# print(Fore.RED + pyfiglet.figlet_format("Error", font="doom") + Style.RESET_ALL)
    

if __name__ == "__main__":
    init(autoreset=True)
    Run_rich()