from fastapi import APIRouter
from models.formats.messages import TextMessage
from util.numbers import get_a_random_int, get_multiple_ints
from util.numbers_api import get_math_fact
router = APIRouter()


@router.get("/math", response_model=TextMessage, tags=["math"])
def get_fact_about_math(for_number=None):
    if not for_number:
        for_number = abs(get_a_random_int())
    trivia = get_math_fact(number=for_number)
    return TextMessage(message=trivia.text if trivia else "No Message Returned from API")
