from fastapi import FastAPI
from pydantic import BaseModel
from app.services.biogpt import generate_answer

class Query(BaseModel):
    question: str

app = FastAPI(title="BioGPT Chatbot")

@app.post("/ask")
def ask(q: Query):
    answer = generate_answer(q.question)
    return {"answer": answer}
