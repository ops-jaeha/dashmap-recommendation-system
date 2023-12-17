# Import Library
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import File
from recommender_api.config import SERVER_HOST, SERVER_PORT
from recommender_api.apps import recommend
from recommender_api.apps import lecture


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommend.router)
app.include_router(lecture.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host=SERVER_HOST, port=SERVER_PORT, reload=True)