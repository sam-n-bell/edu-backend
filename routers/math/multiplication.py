from fastapi import APIRouter
from models.multiplechoice import MultipleChoiceProblem
from util.numbers import get_a_random_int, get_multiple_ints

router = APIRouter()


@router.get("/flash-card", response_model=MultipleChoiceProblem, tags=["math", "addition"])
def single_flash_card():
    one = get_a_random_int(highest=10)
    two = get_a_random_int(highest=10)
    correct_answer = f"{one * two}"
    choices = get_multiple_ints(3, True, int(correct_answer))
    choices.append(correct_answer)
    return MultipleChoiceProblem(
        question=f"{one} x {two} = ?",
        correct_answer=correct_answer,
        answer_choices=sorted(choices)
    )
