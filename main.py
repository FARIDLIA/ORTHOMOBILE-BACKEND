from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from db import models
from db.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "OrtoMobile API is running 🚀"}
