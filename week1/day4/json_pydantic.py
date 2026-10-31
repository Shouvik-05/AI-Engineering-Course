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

#Structure the output
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    address: str
    email: str
    phone_number: int
    issue: str = None

schema = Ticket.model_json_schema()
response_format = {
    "type": "json_object"
}

system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema: {schema}. And give the output in JSON format. If any of the fields are not present in the ticket, return them as null. Keep the issue field as brief as possible. Do not add any extra information or explanation. Only return the JSON object.
"""
#SYSTEM ROLE
message_system = {
    "role": "system",
    "content": system_prompt
}

text = "Hello, My name is Shouvik Bhattacharjee. i have an iphone which is not working at all. my address is delhi. my email is shouvik.bhattacharjee@example.com and my phone number is +91-9876543210. Please help me to fix my iphone."
prompt = f"""
This is a customer ticket. please extract the personal information from this.
{text}
"""

message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]

#Temperature by default is 0 meaning safe

response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)
#print(response)

answer = response.choices[0].message.content
#print(answer)

#how to read this json reply

import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.address)
print(ticket.email)
print(ticket.phone_number)
print(ticket.issue)

