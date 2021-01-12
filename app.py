import pathlib
import uuid
from pydantic import BaseModel
from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse
import requests as rq
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Text(BaseModel):
    text: str


@app.get("/status/")
def get_attempt_problem():
    return {"status": "alive"}


@app.post("/api/")
def post_attempt_problem(text: Text):
    body = {
      "text": text.text,
      "message_id": str(uuid.uuid4())
    }
    url = "http://localhost:5005/model/parse"
    return rq.post(url, json=body).json()


@app.get("/", response_class=HTMLResponse)
def index():
    return HTMLResponse(content=pathlib.Path("index.html").read_text(), status_code=200)
