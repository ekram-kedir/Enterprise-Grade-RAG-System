import requests
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter  
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
import weaviate
from weaviate.embedded import EmbeddedOptions
from dotenv import load_dotenv,find_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
import weaviate
from weaviate.embedded import EmbeddedOptions
from dotenv import load_dotenv,find_dotenv
# 
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

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

