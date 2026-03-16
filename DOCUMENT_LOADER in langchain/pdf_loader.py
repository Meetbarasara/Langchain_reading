from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))#each page is a separate document

print(docs[0].page_content)
print(docs[1].metadata)


# PyPDFLoader is a document loader in LangChain used to load content from PDF files and 
# convert each page into a Document object.

# Limitations:
# It uses the PyPDF library under the hood — not great with scanned PDFs or complex 
# layouts