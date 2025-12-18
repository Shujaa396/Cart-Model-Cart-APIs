from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from routes import user_profile
from fastapi.middleware.cors import CORSMiddleware

# Create tables in DB
SQLModel.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_profile.router)

@app.get("/ping")
def ping():
    return {"msg": "pong"}
