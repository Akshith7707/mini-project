from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    print("AI Interview Bot Backend Running 🚀")
    return {"message": "AI Interview Bot Backend Running 🚀"}