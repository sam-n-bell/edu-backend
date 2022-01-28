from pydantic import BaseModel
from typing import List


class MultipleChoiceProblem(BaseModel):
    question: str
    correct_answer: str
    answer_choices: List[str]
