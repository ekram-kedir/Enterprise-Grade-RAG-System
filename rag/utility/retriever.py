import requests
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
import weaviate
from weaviate.embedded import EmbeddedOptions
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate

def create_retriever(chunks):

  # Setup vector database
  client = weaviate.Client(
    embedded_options = EmbeddedOptions()
  )

  # Populate vector database
  vectorstore = Weaviate.from_documents(
      client = client,    
      documents = chunks,
      embedding = OpenAIEmbeddings(),
      by_text = False
  )

  # Define vectorstore as retriever to enable semantic search
  retriever = vectorstore.as_retriever()
  return retriever

