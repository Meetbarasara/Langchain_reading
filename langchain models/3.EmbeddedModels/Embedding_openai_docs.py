from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

embedding= OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

documents= [
  "Delhi is capital of india",
  "peris is the capital of france",
  "kolkata is the capital of west bengal",
  "gadhinagar is the capital of gujarat",
]
result = embedding.embed_documents(documents)

print (str(result))