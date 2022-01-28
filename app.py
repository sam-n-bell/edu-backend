from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def system_check():
    return {"Message": "I'm still here"}
