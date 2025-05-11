from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df=pd.read_csv("realistic_restaurant_reviews.csv")
#text > tokens (byte pair encoding) > token id > vector embeddings (semantic relationship) 
embeddings=OllamaEmbeddings(model="mxbai-embed-large")

# Checking if db_location already exists means we already have the embeddings no need to generate again
db_location="./chroma_langchain_db"
add_documents= not os.path.exists(db_location)

if add_documents:
    documents = []
    ids=[]

    for i,row in df.iterrows():
        document=Document(
            # Data on which we will be querying
            page_content=row["Title"]+" "+row["Review"],
            # Not used during querying
            metadata={"rating":row["Rating"],"date":row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store=Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location, # So that we are not generating the embeddings again and again
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents,ids=ids)

retriever=vector_store.as_retriever(
    search_kwargs={"k":5} # So that we are looking at 5 relevant reviews before answering
)
