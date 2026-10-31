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

prompt = "Do you know Virat Kohli"
message = {
    "role": role,
    "content": prompt
}

messages = [message]

response = client.chat.completions.create(
    model=model,
    messages=messages
)
#print(response)

print("#"*50)

answer = response.choices[0].message.content
print(f"Answer: {answer}")
