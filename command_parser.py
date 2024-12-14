import os
from rich.console import Console

console = Console()

def execute_command(command):
    if not command:
        console.print("[red]No valid command to execute![/red]")
        return

    try:
        console.print(f"[yellow]Executing:[/yellow] {command}")
        result = os.popen(command).read()
        console.print(f"[green]Result:[/green]\n{result}")
    except Exception as e:
        console.print(f"[red]Execution error:[/red] {e}")
