from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel ,RunnableBranch ,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

model = ChatOpenAI()
parser =StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal["positive","negative"] =Field(description="give the sentiment of the feedback text")

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
  template="classify the sentiment of the following feedback text into positive or  negative Text: {feedback} \n {format_instructions}",
  input_variables=["feedback"],
  partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
  template="generate a response to the following positive feedback text: {feedback}",
  input_variables=["feedback"]
)   

prompt3 = PromptTemplate(
  template="generate a response to the following negative feedback text: {feedback}",
  input_variables=["feedback"]
)   

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive' , prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative' , prompt3 | model | parser),
    RunnableLambda(lambda x: "neutral feedback, no response needed")
)

chain = classifier_chain | branch_chain

print(chain.invoke({"feedback":"I love the new design of your website, it's very user-friendly!"}))