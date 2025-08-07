# 🚀 Learning GenAI using LangChain

This is my personal learning journey through GenAI tools and frameworks — primarily focused on LangChain and Google Gemini.  
It contains code for working with prompts (static & dynamic), chat models, embedding models, and more.

learning_genai_by_langchain/

├── langchain_models/                            # General LangChain model testing

│   ├── chatmodels/                              # Chat model examples (ChatOpenAI, ChatGoogleGenerativeAI, HuggingFace, etc.)

│   └── embeddingmodels/                         # Embedding model examples (OpenAI, Gemini, HuggingFace, etc.)

├── langchain_prompts/                           # Prompt engineering and chatbot demos

├── structured_output/                           # Structured output parsing demos

├── chains_in_langchain/                         # Types of chains with examples

├── langchain_runnables/                         # Examples of mostly used runnables in langchain

├── langchain_document_loader/                   # Different ways to load documents for RAGs

├── langchain_text_splitters/                    # Text splitting ways available in langchain

├── Vectorstores_in_langchain/                   # vectorstores(FAISS, Chroma etc.)

├── Retrievers_in_langchain/                     # Retrievers(WikipediaRetriever, MMR etc.)

├── test.py                                      # General test file for quick experimentation

├── .env                                         # API keys for OpenAI, Gemini, etc. (not committed)

├── .gitignore                                   # Git ignore file for venv, .pkl etc.

├── requirements.txt                             # All required Python packages

└── README.md                                    # Main project documentation


## ⚙️ Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/learning_genai_by_langchain.git
cd learning_genai_by_langchain
```

### 🐍 2. Create & Activate Virtual Environment

```bash
python -m venv langchain-env
.\langchain-env\Scripts\activate    # On Windows
# source langchain-env/bin/activate  # On Linux/Mac
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 4. Setup `.env` file

Create a `.env` file in the root folder with the following:

```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACE_ACESS_TOKEN=your_HF_acess_token
```

---

## 🧑‍💻 Author

**Biswajit Nahak**  
> Final-year student | B.Tech ETC @IIIT BBSR

---

## 📜 License

This repository is for learning and educational purposes only.
