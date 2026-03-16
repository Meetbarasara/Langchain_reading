from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


prompt=PromptTemplate(
  template="generate 5 interesting facts about {topic}",
  input_variables=["topic"]
)
model = ChatOpenAI()
parser =StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({"topic":"space"})
  
print(result)

chain.get_graph().print_ascii()