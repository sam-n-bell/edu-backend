from fastapi import FastAPI
from routers.system import router as system_router
from routers.math.multiplication import router as multiplication_router

app = FastAPI()

app.include_router(system_router, prefix="/system")
app.include_router(multiplication_router, prefix="/multiplication")
