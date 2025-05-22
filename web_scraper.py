import streamlit as st

from langchain_community.document_loaders import SeleniumURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import  OllamaLLM
from ollama import embeddings

template = """
You are an assistant for question-answering task. Answer the question based on the context below. Keep the answer concise and if the question cannot be answered using the information provided answer with "I don't know".
Question: {question}
Context: {context}
Answer: 
"""

embeddings = OllamaEmbeddings(model="llama3.2:1b")
vectors = InMemoryVectorStore(embeddings)

model = OllamaLLM(model="llama3.2:1b")

def load_web(url):
    loader = SeleniumURLLoader(
        urls=[url]
    ) # load the webpage inside a browser, so if the website is dynamic and contains a lots of 'JavaScript', it won't be any problem
    documents = loader.load()
    # Selenium gives a clean text output, so no need to clean
    return documents

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    chunked_documents = text_splitter.split_documents(documents)
    return chunked_documents

def index_documents(documents):
    vectors.add_documents(documents)

def related_documents(query):
    return vectors.similarity_search(query)

def QA(question, context):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    return chain.invoke({"question": question, "context": context})

st.title("Web Scraper")
url =  st.text_input("Enter URL: ")

documents = load_web(url)
chunked_documents = split_documents(documents)

index_documents(chunked_documents)

question = st.chat_input()
if question:
    st.chat_message("user").write(question)
    related_docs = related_documents(question)

    context = "\n\n".join([doc.page_content for doc in related_docs])

    answer = QA(question, context)
    st.chat_message("assistant").write(answer)