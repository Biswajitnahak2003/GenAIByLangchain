#  LangChain Prompt Engineering Projects

Welcome to the **LangChain Prompt Engineering** project repository!  
This collection showcases multiple GenAI mini-projects using LangChain to build, test, and optimize LLM prompts for various use cases.

---


##  Why Prompt Engineering?

Prompt engineering is a crucial skill when working with GenAI. With good prompts, you can:
- Direct LLM behavior more precisely.
- Reduce hallucinations or irrelevant answers.
- Customize outputs for your application (e.g., chatbots, Q&A tools, agents).
- Create reusable and dynamic prompt templates for scaling across tasks or domains.

---

##  How Prompt Engineering Works in LangChain

LangChain supports several ways to build prompts:

### 🔹 1. **Static Prompts**
Use fixed strings that are passed directly to the model.

>  `prompt_static.py`:  
A minimal example using a simple prompt string.

---

### 🔹 2. **Dynamic Prompts with Templates**
These are parameterized templates that allow variables to be inserted dynamically.

>  `prompt_dynamic.py`  
>  `chat_prompt_templte.py`:  
Examples showing how to use LangChain's `PromptTemplate` and `ChatPromptTemplate`.

---

### 🔹 3. **Custom Prompt Classes**
LangChain allows you to extend or customize prompt behavior using your own classes.

>  `message_placeholder.py`:  
Demonstrates using `MessagesPlaceholder` to handle context-based prompt design.

---

### 🔹 4. **Prompt Generators**
Sometimes prompts are dynamically constructed based on JSON templates or other logic.

>  `prompt_generator.py`  
>  `template.json`:  
Example of generating prompts from structured JSON configuration.

---



## 📁 Project Structure

langchain_prompts/

├── prompt_static.py # Simple static prompt example

├── prompt_dynamic.py # Dynamic prompt template using PromptTemplate

├── chatbot_static.py # Static chatbot using LangChain prompt for conversation with history stored

├── chat_prompt_templte.py # Custom ChatPromptTemplate for dynamic chatbot

├── message_placeholder.py # Handles message from history

├── prompt_generator.py # Template to reuse saved in a json file 

├── chat_history.txt # history content stored from conversation

├── template.json # (in parent directory) JSON template for dynamic prompts

└── README.md # You're reading it :)


---

## 🚀 What's Implemented

###  `prompt_static.py`
- Demonstrates a basic static prompt

###  `prompt_dynamic.py`
- Builds prompts from external template file (`template.json`)
- Accepts dynamic user inputs (e.g., topic, tone, format)

###  `chat_prompt_templte.py`
- Builds a dynamic chatbot based on pre-defined prompt logic
- Organizes messages with placeholders and roles

### ✅ `chatbot_static.py`
- Builds a static chatbot based on pre-defined prompt logic
- Supports integration with history and memory

### ✅ `message_placeholder.py`
- Manages placeholder variables like `{input}`, `{history}`
- Keeps context tracking clean and modular

---

## 📦 Dependencies

Make sure your virtual environment is activated and install the following:

pip install langchain langchain-google-genai python-dotenv

📚 **References**

- [LangChain Docs](https://docs.langchain.com/)
- [OpenAI API](https://platform.openai.com/docs/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

👨‍💻 Author

by Biswajit Nahak
Feel free to contribute or fork this repo!


