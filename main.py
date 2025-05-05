from fastapi import FastAPI

app = FastAPI()

@app.get("/sayHello")
def say_hello():
    return {"message": "Hello User"}
