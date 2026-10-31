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
prompt = "Suggest me a name for my clothing company. The name should be in one word. Suggest only one name."

#SYSTEM ROLE
message_system = {
    "role": "system",
    "content": "You are a brand manager who suggests name for my clothing company. name should be in one word."
}

message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]

#Temperature by default is 0 meaning safe

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0
)
#print(response)

print("#"*50)

answer = response.choices[0].message.content
print(f"Answer: {answer}")
