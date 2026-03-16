from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel,RunnableBranch
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

propt1 = PromptTemplate(
    template='explain this topic either in 300 words or less  {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='write a summary of the following text in less than 50 words - {text}',
    input_variables=['text']
)

tex_gen_chain = RunnableSequence(propt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser), #if word count is greater than 300 then it will execute the prompt2 chain
    RunnablePassthrough())

final_chain = RunnableSequence(tex_gen_chain, branch_chain)
result = final_chain.invoke({'topic':'russia vs ukraine war'})
print(result)

#syntax of RunnableBranch is RunnableBranch(
# (condition, chain),
#  else_chain,
#  default_chain
# ) where condition is a lambda function that takes the output of the previous chain and returns a boolean value, if the condition is true then it will execute the chain mentioned in the condition otherwise it will execute the else_chain.