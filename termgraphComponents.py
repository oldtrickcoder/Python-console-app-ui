import sys
import io
# Try importing 'main' directly from the top-level 'termgraph' module
# If this fails, we might need to inspect the installed package more closely.
from termgraph.termgraph import main as termgraph_main # CORRECTED IMPORT

from typing import List, Optional

def generate_termgraph(
    data_lines: List[str],
    chart_type: str = "bar",
    title: Optional[str] = None,
    width: int = 50,
    color: Optional[List[str]] = None, # Can be a single color string or a list of strings
    suffix: str = "",
    no_labels: bool = False,
    no_values: bool = False,
    # Add other termgraph arguments as needed
) -> str:
    """
    Generates a termgraph chart as a string by redirecting stdin/stdout and sys.argv.

    Args:
        data_lines (list): A list of strings, each representing a data line for termgraph.
        chart_type (str): "bar" (default) or "stacked".
        title (str, optional): Title of the graph.
        width (int): Width of the graph in characters.
        color (str/list, optional): Color(s) for the bars.
        suffix (str): Suffix to add to data points.
        no_labels (bool): If True, do not print the row labels.
        no_values (bool): If True, do not print the row values.

    Returns:
        str: The ASCII chart as a multi-line string.
    """
    
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    old_argv = sys.argv # Store original sys.argv

    input_buffer = io.StringIO("\n".join(data_lines))
    output_buffer = io.StringIO()

    sys.stdin = input_buffer
    sys.stdout = output_buffer

    try:
        # Build arguments list for termgraph
        # IMPORTANT: sys.argv[0] is typically the script name.
        # We need to prepend a dummy script name to the arguments.
        # This will simulate how termgraph would be called from the command line.
        args_for_termgraph = ["termgraph_dummy_script.py"] 

        if title:
            args_for_termgraph.extend(["--title", title])
        if width:
            args_for_termgraph.extend(["--width", str(width)])
        if color:
            if isinstance(color, list):
                args_for_termgraph.append("--color")
                args_for_termgraph.extend(color)
            else:
                args_for_termgraph.extend(["--color", color])
        if suffix:
            args_for_termgraph.extend(["--suffix", suffix])
        if no_labels:
            args_for_termgraph.append("--no-labels")
        if no_values:
            args_for_termgraph.append("--no-values")

        if chart_type == "stacked":
            args_for_termgraph.append("--stacked")
        
        # NOTE: If termgraph requires a filename even when reading from stdin,
        # you might need to add a dummy filename here, e.g.,
        # args_for_termgraph.append("dummy_data.txt")
        # Then, termgraph would try to read from "dummy_data.txt" but since
        # sys.stdin is redirected, it will read from input_buffer.
        # Let's start without it and add if it complains about missing filename.
        
        # IMPORTANT: Modify sys.argv for termgraph to read from
        sys.argv = args_for_termgraph

        # Call termgraph's main function (now with no arguments)
        termgraph_main() # No arguments passed directly here

    finally:
        # IMPORTANT: Restore all original streams/variables
        sys.stdin = old_stdin
        sys.stdout = old_stdout
        sys.argv = old_argv # Restore original sys.argv
    
    return output_buffer.getvalue()

# --- Example Console Application Usage (Same as before) ---


def termgraph_example():
    print("Welcome to My Console Dashboard!\n")

    daily_progress_data = [
        "Mon,70", "Tue,85", "Wed,75", "Thu,90", "Fri,95", "Sat,60", "Sun,80",
    ]
    print("--- Daily Progress % ---")
    progress_chart = generate_termgraph(
        daily_progress_data,
        title="Weekly Progress",
        color="green",
        suffix="%",
        width=150
    )
    print(progress_chart)

    print("\n" + "="*50 + "\n")

    monthly_downloads_data = [
        "Jan,1000,500", "Feb,1200,550", "Mar,1100,600", "Apr,1300,650", "May,1400,700", "Jun,1350,680",
    ]
    print("--- Monthly Downloads (App A vs App B) ---")
    downloads_chart = generate_termgraph(
        monthly_downloads_data,
        title="App Downloads Comparison",
        color=["cyan", "yellow"],
        suffix=" downloads",
        width=100
    )
    print(downloads_chart)

    print("\n" + "="*50 + "\n")
    
    tasks_data = [
        "Dev,10,5,2", # Label, High Priority, Medium Priority, Low Priority
        "Test,8,7,3",
        "Deploy,5,3,1"
    ]
    print("--- Tasks Completed by Phase (Stacked) ---")
    tasks_chart = generate_termgraph(
        monthly_downloads_data,
        title="App Downloads Comparison",
        color=["cyan", "yellow"], # This is correct for 2 series
        suffix=" downloads",
        width=60
    )
    
    print(tasks_chart)

    print("\nThank you for using the app!")