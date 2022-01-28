from pydantic import BaseModel


class SystemCheck(BaseModel):
    message: str
