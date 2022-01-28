from fastapi import APIRouter

router = APIRouter()


@router.get("/healthcheck", tags=["health"])
def get_healthcheck():
    return {"Message": "I'm still here"}
