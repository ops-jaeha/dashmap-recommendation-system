# Import Library
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import File
from config import SERVER_HOST, SERVER_PORT
from apps import recommend


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommend.router)


if __name__ == '__main__':
    uvicorn.run("recommender_api.main:app", host=SERVER_HOST, port=SERVER_PORT, reload=True)