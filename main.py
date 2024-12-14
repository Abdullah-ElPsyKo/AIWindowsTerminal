import os
from rich.console import Console
from prompt_toolkit import PromptSession
from llm_interface import get_command_suggestion

# Setup
console = Console()
session = PromptSession()

def execute_command(command):
    """ Execute the command as is. """
    if command.lower() == "cls":
        os.system("cls")  # Properly clear the screen
    else:
        os.system(command)

def main():
    console.print("[bold cyan]Welcome to the Smart Terminal! Type 'jarvis' followed by a command.[/bold cyan]")

    while True:
        try:
            user_input = session.prompt(">>> ").strip()

            if user_input.lower().startswith("jarvis"):
                # Extract query after "jarvis"
                query = user_input[len("jarvis"):].strip()

                # Query LLM for a system command suggestion
                suggested_command = get_command_suggestion(query)

                # Confirm or edit suggestion
                edited_command = session.prompt(default=suggested_command).strip()
                execute_command(edited_command)


            else:
                # Directly execute non-Jarvis commands
                execute_command(user_input)

        except (KeyboardInterrupt, EOFError):
            console.print("\n[red]Goodbye![/red]")
            break

if __name__ == "__main__":
    main()
