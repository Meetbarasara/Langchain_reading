from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='example.csv')

docs = loader.load()

print(len(docs))
print(docs[1])


# CSVLoader is a document loader used to load CSV files into LangChain 
# Document objects — one per row, by default.