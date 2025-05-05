from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI()

# Define the /sayHello route
@app.get("/sayHello")
def say_hello():
    return {"message": "Hello User"}
