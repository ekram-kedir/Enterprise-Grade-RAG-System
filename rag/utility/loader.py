from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter  


# Data loader
def data_loader(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()

    # Chunk the data
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    return chunks
