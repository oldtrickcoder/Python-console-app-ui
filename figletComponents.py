from pyfiglet import Figlet
import pyfiglet

from colorama import Fore, Style, init
# Initialize Colorama for cross-platform compatibility
init(autoreset=True) # autoreset ensures colors are reset after each print

def print_colored_figlet(text, font="standard", color=Fore.CYAN):
    """
    Prints FIGlet text with a specified foreground color.
    """
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(color + ascii_art)

def print_colored_figlet_with_style(text, font="standard", color=Fore.GREEN, style=Style.BRIGHT):
    """
    Prints FIGlet text with a specified foreground color and style (e.g., bright).
    """
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(style + color + ascii_art)

def print_banner():
    figlet = Figlet(font='3-d')
    banner = figlet.renderText('My Cool App')
    print(banner)
    print("Welcome to My Cool App!")
    print("This app demonstrates the use of the Rich library.")
    print("Enjoy your experience!\n")