# AIWindowsTerminal

**Description:** A smart terminal application that uses an AI-powered assistant to interpret commands and execute system tasks on Windows.

## Features

- Intelligent command suggestions using an LLM.
- Interactive terminal with command editing and execution.
- Support for standard Windows system commands.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abdullah-ElPsyKo/AIWindowsTerminal.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AIWindowsTerminal
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run main.py file:
   ```bash
   python main.py
   ```

## Usage

1. Run the main application:
   ```bash
   python main.py
   ```
2. Type commands directly or use "jarvis" followed by a command query for AI assistance.

### Configuration

- Ensure that `config.py` is set up correctly with your local LLM API endpoint.
- This project supports integration with **LM Studio** or similar local language models.

## Example

```
>>> jarvis what is my ip
ipconfig | findstr /v "IPv4"
```

The suggested command is displayed directly, and the user can press **Enter** to run it or edit the command before execution.

