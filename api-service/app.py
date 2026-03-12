from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Scalable Data Pipeline API Running"}