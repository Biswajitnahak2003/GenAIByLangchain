
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


splitter = SemanticChunker(
    embeddings = embeddings,
    breakpoint_threshold_type = ""
    )

text = """
Beneath the sunlit surface, the deep sea is a realm of mystery. Strange creatures glow in the darkness, surviving under crushing pressure and near-freezing temperatures. Many of these species are still undiscovered, and scientists believe the ocean floor holds secrets that could change our understanding of life itself.
Humans have always looked to the stars with wonder. Space exploration has taken us to the Moon, sent rovers to Mars, and launched telescopes to peer into the far reaches of the universe. Each mission uncovers more about our cosmic neighborhood, bringing us closer to answering the biggest question—are we alone?
Baking bread is both science and art. Flour, water, yeast, and salt combine to create something far greater than their parts. The aroma of freshly baked bread can transform a home, and each loaf carries the story of its maker’s care. From crispy baguettes to soft, fluffy buns, bread connects cultures and comforts hearts.
"""

docs = splitter.create_documents([text])

print(len(docs))
print(docs[0])
