from langchain_core.prompts import PromptTemplate

## template
template = PromptTemplate(
    template = """
explain the topic "{topic}"
with the explaination style of "{style}"
within the length of "{length}"words.

""",
input_variables = ["topic", "style", "length"],
validate_template = True
)

template.save("template.json")
