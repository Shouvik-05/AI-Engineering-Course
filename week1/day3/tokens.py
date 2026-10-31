import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")
client = Groq(api_key=api_key)
model="openai/gpt-oss-120b"
role = "user"

# 3 prompts
prompt1 = "Hi!"
prompt2 = "Explain Time Travel in detail."
prompt3 = "Write a 100 words essay on machine learnng."

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=5000,
    )
    usage = response.usage
    print(f"Prompt: {prompt} -->Your tokens: {usage.prompt_tokens}, completion_tokens: {usage.completion_tokens}, total_tokens: {usage.total_tokens}, finish_reason: {response.choices[0].finish_reason}   ")


# print("#"*50)

# answer = response.choices[0].message.content
# print(f"Answer: {answer}")
