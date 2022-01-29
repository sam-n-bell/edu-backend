from pydantic import BaseModel
from typing import List


class FlashCard(BaseModel):
    question: str
    correct_answer: str


class MultiplicationTable(BaseModel):
    numbers: List[FlashCard]
