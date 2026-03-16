from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)

model1 = ChatHuggingFace(llm=llm)
model2 = ChatOpenAI()

prompt1=PromptTemplate(
  template="generate short and simple notes from the following text: {text}",
  input_variables=["text"]
)

prompt2=PromptTemplate(
    template = "generate 5 short question answer from the following text: {text}",
    input_variables=["text"]
)

prompt3=PromptTemplate(
  template="""Format the following notes and question-answer pairs into a single organized document. 
  Do not rewrite the content into paragraphs. Keep the notes under a 'Notes' heading, and explicitly list the questions and answers under a 'Q&A' heading.
  
  Notes:
  {notes}
  
  Question Answer pairs:
  {qa}""",
  input_variables=["notes","qa"]
)
parser =StrOutputParser()

parrallel_chain = RunnableParallel(
  {"notes": prompt1 | model1 | parser,
   "qa": prompt2 | model2 | parser}
)

merge_chain = prompt3 | model2 | parser

chain = parrallel_chain | merge_chain

result = chain.invoke({"text":"""
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""})

print(result) 