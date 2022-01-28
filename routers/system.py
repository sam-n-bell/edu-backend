from fastapi import APIRouter
from models.system.responses import SystemCheck
router = APIRouter()


@router.get("/healthcheck", response_model=SystemCheck, tags=["system"])
def get_healthcheck():
    return SystemCheck(message="I'm still here")
