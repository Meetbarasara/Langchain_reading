from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Set a fake user agent so websites don't block your scraper
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.amazon.in/HARLEY-DAVIDSON-Motorcycle-booking-Ex-Showroom-Warranty/dp/B0FDGY2KM1/?_encoding=UTF8&pd_rd_w=z6h54&content-id=amzn1.sym.19c1fe77-024a-484e-85dd-b22ab1977129&pf_rd_p=19c1fe77-024a-484e-85dd-b22ab1977129&pf_rd_r=X9NNEKTSDTE07V56QXXS&pd_rd_wg=Ve0cM&pd_rd_r=38a82be7-286d-433e-ad67-f3ccb3793836&ref_=pd_hp_d_btf_ls_gwc_pc_en4_&th=1'
loader = WebBaseLoader(url)  # we caan also pass a list of urls to load multiple web pages at once

docs = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))




# WebBaseLoader is a document loader in LangChain used to load and extract text content from  web pages (URLs).
# It uses BeautifulSoup under the hood to parse HTML and extract visible text.

# • When to Use:
# For blogs, news articles, or public websites where the content is primarily text-based and static.


# Limitations:
# •  Doesn’t handle JavaScript-heavy pages well (use SeleniumURLLoader for that).
# • Loads only static content (what's in the HTML, not what loads after the page renders)