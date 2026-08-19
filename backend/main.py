from fastapi import FastAPI

app = FastAPI(title="SurakshaText")

@app.get("/")
def home():
    return {
        "message": "SurakshaText API is running!"
    }
