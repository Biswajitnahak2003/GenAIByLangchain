# LangChain Structured Output with Gemini 1.5 Flash


This is my personal learning journey through GenAI tools and frameworks — primarily focused on **LangChain**, **Google Gemini**, and **Hugging Face**.  
It contains code examples for working with structured outputs.

---

## 📌 Why Structured Output?

When working with Large Language Models (LLMs), raw string responses are hard to interpret, validate, or use in downstream tasks.  
**Structured output** solves this by making the model return data in predictable formats like dictionaries or JSON — ideal for applications like agents, tools, data extraction, and pipeline integrations.

---

## 🧩 How We Achieve Structured Output in LangChain

LangChain provides several ways to structure the LLM responses depending on the use-case and LLM support.

###  For OpenAI (and other supported models):
We use `StructuredOutputParser` with **function calling** or **tool calling** capabilities built into models like `gpt-4`.

-  **Example Used**: `StructuredOutputParser.from_response_schemas([...])`
-  Benefits: Automatic validation, cleaner responses, highly reliable

---

### 🛠️ For General LLMs (like Hugging Face or Gemini):
If function/tool calling is **not available**, we use the following fallback strategies:

1. ### 🔢 **StringOutputParser**  
   Parses plain text into useful strings.

2. ### 📦 **JsonOutputParser**  
   Ensures the response is a valid JSON — great for consistent structure.

3. ### 🧱 **StructuredOutputParser (manual)**  
   Defines a schema and parses the output manually (for LLMs without native support).

4. ### 📘 **PydanticOutputParser**  
   Uses [Pydantic](https://docs.pydantic.dev/) models for powerful data validation and conversion into Python classes.

---


## 📁 Folder Structure

langchain_structured_output/

├── using_pydantic.py # Validates Gemini output with a pydantic.BaseModel

├── schema.json # JSON Schema definition for a user profile

├── main_json_schema.py # Validates Gemini output using schema.json

├── str_op_parser.py # Uses StrOutputParser for direct string response

└── json_op_parser.py # Uses JsonOutputParser for dictionary-like parsing


---

##  Tech Stack

- **LLM**: Gemini 1.5 Flash (`google/gemini-pro`)
- **Framework**: LangChain
- **Validation**: Pydantic and JSON Schema
- **Prompt Handling**: `ChatPromptTemplate`, `Output Parsers`

---

## 📜 Scripts Overview

| Script | Description |
|--------|-------------|
| `using_pydantic.py` | Parses Gemini's output into a custom `Review` Pydantic model containing product, rating, and sentiment. |
| `schema.json` | Schema file describing fields like `name`, `email`, and `is_premium_user` for validating model responses. |
| `main_json_schema.py` | Loads `schema.json` and validates Gemini output using `.with_structured_output(schema=schema)`. |
| `str_op_parser.py` | Uses `StrOutputParser` to get plain text from the model with minimal formatting. |
| `json_op_parser.py` | Uses `JsonOutputParser` with a format instruction to get dictionary-formatted output. |

---



📌 How to Run

Make sure you're using a virtual environment with langchain and google.generativeai installed:

    pip install -r requirements.txt

Then run any script like:

    python json_op_parser.py

📌 Notes

    These scripts assume your GOOGLE_API_KEY is set as an environment variable.

    You can modify the prompt templates to experiment with different schemas or model behaviors.

    All outputs are validated before printing — any mismatch will throw a validation error.

📌 References

- LangChain Docs: https://docs.langchain.com/
- OpenAI API: https://platform.openai.com/docs/
- LangChain Output Parsers: https://docs.langchain.com/docs/components/output_parsers/
- Pydantic Documentation: https://docs.pydantic.dev/


📌 Author

Biswajit Nahak

    Final-Year B.Tech ETC Student @ IIIT Bhubaneswar


