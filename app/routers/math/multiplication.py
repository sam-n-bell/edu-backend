from fastapi import APIRouter
from models.formats.multiplechoice import MultipleChoiceProblem
from models.formats.flashcard import MultiplicationTable, FlashCard
from util.numbers import get_a_random_int, get_multiple_ints

router = APIRouter()


@router.get("/single-problem", response_model=MultipleChoiceProblem, tags=["math", "multiplication"])
def single_flash_card():
    one = get_a_random_int(highest=10)
    two = get_a_random_int(highest=10)
    correct_answer = f"{one * two}"
    # FIXME: choices that match answer
    choices = get_multiple_ints(3, True, int(correct_answer))
    choices.append(correct_answer)
    return MultipleChoiceProblem(
        question=f"{one} x {two} = ?",
        correct_answer=correct_answer,
        answer_choices=sorted(choices)
    )


@router.get("/table", response_model=MultiplicationTable, tags=["math", "multiplication", "informative"])
def multiplication_table(up_to_x=12, up_to_y=12):
    nums = []
    for i in range(1, int(up_to_x) + 1):
        for n in range(1, int(up_to_y) + 1):
            nums.append(
                FlashCard(
                    question=f"{i} x {n}",
                    correct_answer=f"{i * n}"
                )
            )
    return MultiplicationTable(numbers=nums)
