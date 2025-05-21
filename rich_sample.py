
from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.markdown import Markdown
import time
from rich.syntax import Syntax

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
        time.sleep(0.1)

def rich_markdown_sample():
    markdown_text = """
    # Title
    This is a paragraph with **bold** and *italic* text.
        """
    markdown = Markdown(markdown_text)
    print(markdown)

def rich_syntax():
    code = """
    def hello_world():
    print("Hello, world!")
    """
    syntax = Syntax(code, "python", line_numbers=True)
    print(syntax)