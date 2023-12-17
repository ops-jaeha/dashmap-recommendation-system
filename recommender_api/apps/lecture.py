# Import Libray
from fastapi import APIRouter, status

# Import File
from recommender_api.core.models import session_scope
from recommender_api.utils.lecture import *


router = APIRouter()


@router.post("/recommend/{user_id}/{lecture_id}", status_code=status.HTTP_200_OK, tags=["lecture"])
async def watch_lecture(user_id: int, lecture_id: int, ratings: int = 5):
    with session_scope() as session:
        recode_lecture(session=session, u_id=user_id, l_id=lecture_id, r=ratings)
        return {
            "message": "success"
        }