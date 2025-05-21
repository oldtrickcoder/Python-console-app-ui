
from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.markdown import Markdown
import time
from rich.syntax import Syntax
from rich.panel import Panel
def rich__ColorFont():
    print("[bold red]This is bold red text[/]")
    print("[italic blue on white]This is italic blue text on a white background[/]")
    print("This is [bold]some[/] text with [italic blue]mixed styles[/].")

def rich_sample_Table():
    console = Console()
    table = Table(title="Data Table")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Age", style="magenta")
    table.add_column("City", style="green")
    table.add_row("Alice", "30", "New York")
    table.add_row("Bob", "25", "London")
    table.add_row("Charlie", "35", "Paris")
    console.print(table)

def rich_progress_sample1():
    for i in track(range(20), description="Processing..."):
        time.sleep(0.3)

def rich_markdown_sample():
    markdown_text = """# Title 
    This is a paragraph with **bold** and *italic* text."""
    markdown = Markdown(markdown_text)
    print(markdown)

def rich_syntax():
    code = """
    def hello_world():
    print("Hello, world!")
    """
    syntax = Syntax(code, "python", line_numbers=True)
    print(syntax)


def create_chart(data, title="Chart"):
    max_value = max(data)
    num_rows = 10
    bar_width = 2
    scale = num_rows / max_value

    grid = Table.grid()
    grid.add_column()
    for _ in range(len(data)):
        grid.add_column(justify="center")
    grid.add_row(title, *[str(x) for x in data])

    for i in range(num_rows, 0, -1):
        row = [str(i * (max_value / num_rows))]
        for value in data:
            if value * scale >= i:
                row.append("[bold green]" + "█" * bar_width + "[/bold green]")
            else:
                row.append(" " * bar_width)
        grid.add_row(*row)

    return Panel(grid, title=title, expand=False)

def StarWarsTable():
    table = Table(title="Star Wars Movies")
    table.add_column("Released", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Box Office", justify="right", style="green")
    table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
    table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
    table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
    table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")
    console = Console()
    console.print(table)