from rich.console import Console
from rich_sample import rich__ColorFont,rich_progress_sample1,rich_sample_Table,rich_markdown_sample,rich_syntax,create_chart,StarWarsTable
import pyfiglet
from figletComponents import print_colored_figlet, print_colored_figlet_with_style, print_banner,print_figlet_gradient_char_by_char
from colorama import Fore, Style, init
init(autoreset=True) # autoreset ensures colors are reset 
from ascii_chart_sample import AsciiChart
# from termgraph import termgraph_example
from termgraphComponents import termgraph_example



def Run_rich():
    print('Lets running the App')
    # print(Fore.CYAN + Style.BRIGHT + pyfiglet.figlet_format("Hello", font="alligator") + Style.RESET_ALL)
    print_figlet_gradient_char_by_char("Python", font="3-d", start_hex="#FFA818", end_hex="#FFD700")
    print(Fore.RED + pyfiglet.figlet_format("DOOM", font="doom") + Style.RESET_ALL)
    Pause()
    # print_banner()
    # rich__ColorFont()
    rich_sample_Table()
    rich_progress_sample1()
    rich_markdown_sample()
    rich_syntax()
    print('App finished running')

def Pause():
    input("Press Enter to continue...")

def Run_Chart():
    print('Lets RUn Chart')
    print_figlet_gradient_char_by_char("Chart Sample", font="alligator2", start_hex="#c90ca9", end_hex="#0f8ac4")
    Pause()
    console = Console()
    data = [5, 8, 3, 9, 2, 7, 6]
    chart = create_chart(data, title="Sample Chart")
    console.print(chart)
    StarWarsTable()
    print('Chart finished running')

    

# if __name__ == "__main__":
init(autoreset=True)
    #Run_rich()
Run_Chart()
termgraph_example()
AsciiChart()
print('All finished running')