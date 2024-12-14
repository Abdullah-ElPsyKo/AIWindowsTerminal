import requests
from config import LOCAL_LLM_API

def get_command_suggestion(user_input):
    payload = {
        "model": "llama-3.2-3b-instruct",  # Change to the correct model
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that only returns valid Windows command-line commands. "
                    "Respond with the command only, without explanations, formatting, or backticks."
                )
            },
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.3,
        "max_tokens": 100,
        "stream": False
    }

    try:
        response = requests.post(
            f"{LOCAL_LLM_API}/v1/chat/completions",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            result = response.json()
            # Clean and return the raw command
            command = result["choices"][0]["message"]["content"].strip()
            return command.replace("`", "").strip()
        else:
            return f"[ERROR] {response.status_code} - {response.text}"
    except Exception as e:
        return f"Connection error: {e}"
