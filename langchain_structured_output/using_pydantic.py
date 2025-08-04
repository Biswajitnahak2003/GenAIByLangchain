from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field


load_dotenv()

model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2
)

class Review(BaseModel):
    key_theme: list[str] = Field(
        description="Key themes in the review")
    summary: str = Field(
        description="Summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="Sentiment of the review")
    pros: Optional[list[str]] = Field(
        default=None, description="List of pros mentioned in the review")
    cons: Optional[list[str]] = Field(
        default=None, description="List of cons mentioned in the review")
    name: Optional[str] = Field(
        default=None, description="Name of the reviewer")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""okay so i got these last week during the sale, i think for around 1199 or 1299 not sure but damn it was a steal at that price. sound is honestly good like for casual music and youtube or even calls it's fine. bass is punchy, almost too much sometimes lol but yeah it’s boAt so kind of expected that.

battery life is surprisingly solid. i charged it once and it lasted me like 3-4 days with medium usage. i mean i don’t use it all day just here and there. call quality is decent but in noisy areas it struggles a bit... mic picks up background sound too much. the touch controls are kinda hit or miss though. sometimes they work, sometimes i end up skipping tracks by mistake when i just wanted to pause.

fit is okay. not the best for long hours. hurts a bit after an hour or so. i got the black one btw, looks cool ngl. packaging was nice too. overall not a bad buy for the price, just don't expect premium stuff. perfect if you're a student or just want budget earbuds.""")

print(result)