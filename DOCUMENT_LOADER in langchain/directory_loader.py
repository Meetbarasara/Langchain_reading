from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf', #All .pdf files in the ROOT directory will be loaded
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()# will take less time to load as it is a generator (generator means it will load one document at a time instead of loading all documents at once)

for document in docs:
    print(document.metadata)


#DirectoryLoader is a document loader that lets you load multiple documents from a directory (folder) of files.

#globs 
# "**/*.txt" - all .txt files in the directory and all subdirectories
#"data/*.csv" - all .csv files in the "data" directory (but not subdirectories)
#"**/*" - all files (any type) in the directory and subdirectories