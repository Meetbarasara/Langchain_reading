from langchain_core.messages import HumanMessage, SystemMessage, AIMessage 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


#system message IS the instruction to the model
# system_message = SystemMessage(content="You are a helpful assistant that provides concise and accurate answers to` user queries. Always respond in a clear and informative manner, ensuring that your answers are relevant to the user's question. If you don't know the answer, say 'I don't know' instead of guessing.")

load_dotenv()
model = ChatOpenAI()

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)