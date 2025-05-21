from pyfiglet import Figlet
import pyfiglet
from rich.console import Console
from rich.color import Color
from rich.style import Style

from colorama import Fore, Style, init
# Initialize Colorama for cross-platform compatibility
init(autoreset=True) # autoreset ensures colors are reset after each print
console = Console()
def print_colored_figlet(text, font="standard", color=Fore.CYAN):
    """
    Prints FIGlet text with a specified foreground color.
    """
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(color + ascii_art)

def print_colored_figlet_with_style(text, font="standard", color=Fore.GREEN, style=Style.BRIGHT):
    # """
    # Prints FIGlet text with a specified foreground color and style (e.g., bright).
    # """
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(style + color + ascii_art)

def print_banner():
    figlet = Figlet(font='3-d')
    banner = figlet.renderText('My Cool App')
    print(banner)
    print("Welcome to My Cool App!")
    print("This app demonstrates the use of the Rich library.")
    print("Enjoy your experience!\n")

def interpolate_color(color1, color2, fraction):
    # """
    # Interpolates between two RGB colors.
    # fraction is between 0.0 and 1.0
    # """
   # CORRECTED: Access RGB values using ._rgb
    r1, g1, b1 = color1.triplet.red, color1.triplet.green, color1.triplet.blue
    r2, g2, b2 = color2.triplet.red, color2.triplet.green, color2.triplet.blue

    r = int(r1 + (r2 - r1) * fraction)
    g = int(g1 + (g2 - g1) * fraction)
    b = int(b1 + (b2 - b1) * fraction)
    return Color.from_rgb(r, g, b)

def print_figlet_gradient_char_by_char(text, font="standard", start_hex="#FF0000", end_hex="#0000FF"):
    figlet_text = pyfiglet.figlet_format(text, font=font)
    
    start_color = Color.parse(start_hex)
    end_color = Color.parse(end_hex)

    # Calculate total width of the FIGlet text
    lines = figlet_text.splitlines()
    if not lines:
        return
    max_width = max(len(line) for line in lines)

    # Generate a list of colors for each horizontal position
    gradient_colors = []
    for i in range(max_width):
        fraction = i / max(1, max_width - 1) # Avoid division by zero for single-char width
        gradient_colors.append(interpolate_color(start_color,end_color, fraction))
    
    # Apply colors character by character
    output_lines = []
    for line in lines:
        colored_line = []
   
        for i, char in enumerate(line):
            if char != ' ': # Don't color spaces unless they are part of the figlet character
                color = gradient_colors[min(i, max_width - 1)] # Ensure index is within bounds
                #print(color,"Color data")
                colored_line.append(f"[{color[0]}]{char}[/]")
            else:
                colored_line.append(' ')
        output_lines.append("".join(colored_line))
    
    console.print("\n".join(output_lines))

# --- Examples ---
# console.print("\n[bold]Character-by-Character Gradient:[/bold]\n")
# print_figlet_gradient_char_by_char("Python", font="doom", start_hex="#FFA500", end_hex="#FFD700") # Orange to Gold
# console.print("\n")
# print_figlet_gradient_char_by_char("Awesome", font="slant", start_hex="#8A2BE2", end_hex="#4169E1") # Blue Violet to Royal Blue
# console.print("\n")
# print_figlet_gradient_char_by_char("Gradient", font="banner", start_hex="#00FF00", end_hex="#FFFF00") # Green to Yellow


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
