from langchain_anthropic import ChatAnthropic, ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-2")

response = model.invoke("What is the capital of India?") # will not work as i have not paid for the API key.

print(response.content) #.content to filter out the response and get the answer only.