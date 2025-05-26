# 🌐 AI Web Scraper

An intelligent web scraper that extracts content from dynamic web pages and enables question-answering using local LLMs (via Ollama). It leverages LangChain to process, embed, and retrieve contextually relevant information in response to user queries.
![scraper](https://github.com/user-attachments/assets/28de935d-8428-4bee-a166-bb991689f6b7)
![actual](https://github.com/user-attachments/assets/6e3a310b-525e-46d7-8b17-84710ebd331d)

---

## Features

- 🌍 Scrape and extract text from web pages using Selenium  
- ✂️ Split large text into manageable chunks for better processing  
- 🔍 Retrieve relevant information using **semantic similarity search**  
- 🧠 Answer questions using **LLaMA3.2:1b** local models via **Ollama**  
- 💬 Interactive UI built with **Streamlit**  
- 🔒 Runs entirely locally – no external API calls required  

---

## Use Cases

- Extract and query content from technical, legal, or academic web pages  
- Analyze long-form articles or policy documents  
- Build internal knowledge tools powered by web data  
- Perform research on dynamic websites that require JavaScript rendering  

---

## Built With

- **Python**  
- **LangChain** – for loading, splitting, vectorizing, and prompting  
- **Ollama** – for local language models and embedding generation  
- **Selenium** – for scraping JavaScript-rendered content  
- **Streamlit** – for the web-based user interface  
- **In-Memory Vector Store** – for fast retrieval of relevant content 
