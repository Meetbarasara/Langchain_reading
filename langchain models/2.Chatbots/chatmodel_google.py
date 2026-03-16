from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

response = model.invoke("What is the capital of India?") 
print(response.content) #.content to filter out the response and get the answer only.