# 📖 What are Chains in LangChain?

In LangChain, a chain is a sequence of calls to components like LLMs, tools, or data processing steps. They are the fundamental building blocks for creating more complex and powerful AI applications.

---

# ❓ Why Use Chains?

Chains allow us to connect multiple components together, where the output of one step becomes the input for the next. This enables you to build sophisticated logic that goes far beyond a single LLM call.

---

## 🧭 Table of Contents

- ⛓️ Sequential Chains
- 🧵 Parallel Chains
- 🔀 Conditional Chain(Branch)

---

## ⛓️ Sequential Chains

A sequential chain executes a series of steps in a specific order. This is the most common type of chain, perfect for workflows like generating text and then summarizing it. The modern way to create them is with the pipe (`|`) operator.

### ✅ Example

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt1 = ChatPromptTemplate.from_template("What is the capital of {country}?")
prompt2 = ChatPromptTemplate.from_template("What is a fun fact about {capital}?")

# The output of the first chain (`capital`) is passed to the second
chain = (
    {"capital": prompt1 | llm | StrOutputParser()}
    | prompt2
    | llm
    | StrOutputParser()
)
chain.invoke({"country": "France"})
```

## 🧵 Parallel Chains

A parallel chain executes multiple chains simultaneously and returns their outputs combined in a dictionary. This is useful for running independent tasks on the same input.
### ✅ Example
```
# Assumes 'llm' and 'parser' are defined
prompt1 = ChatPromptTemplate.from_template("Tell me a joke about {topic}.")
prompt2 = ChatPromptTemplate.from_template("Write a haiku about {topic}.")

chain = {
    "joke": prompt1 | llm | parser,
    "haiku": prompt2 | llm | parser,
}
chain.invoke({"topic": "a cat"})
```
## 🔀 Conditional (Branch) Chains

A conditional chain, built with RunnableBranch, acts like an if-elif-else statement. It dynamically chooses which chain to execute based on the input, allowing you to create intelligent routing logic.
### ✅ Example
```
from langchain_core.runnables import RunnableBranch

# Assumes 'math_chain', 'lang_chain', and 'general_chain' are defined
# This chain first classifies the input, then routes it to the correct chain
branch = RunnableBranch(
    (lambda x: "math" in x["class"], math_chain),
    (lambda x: "language" in x["class"], lang_chain),
    general_chain,  # Default
)

# The full chain would first run a classifier, then the branch
# full_chain = {"class": classifier_chain, "topic": ...} | branch
```
# 📘 Reference

- [📚 LangChain Docs](https://docs.langchain.com/)

# 🙋 Author

Biswajit Nahak | BTech ETC | @IIIT BBSR
