import subprocess
import json

def chat_with_local(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3.1"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input in ["quit", "exit"]:
            break
        print("Chatbot:", chat_with_local(user_input))