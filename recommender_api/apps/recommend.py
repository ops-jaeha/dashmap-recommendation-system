# Import Libray
from fastapi import APIRouter, status, Header
from typing import Optional
from datetime import datetime

# Import File
from utils import *
from utils.recommend import recommend


router = APIRouter()


@router.get("/recommend/{user_id}", status_code=status.HTTP_200_OK, tags=["recommendation"])
async def user_recommend(user_id: int):
    url_1, url_2, url_3, url_4, url_5, url_6 = recommend(user_id=user_id)
    return {
        "recommend_1": f"{url_1}",
        "recommend_2": f"{url_2}",
        "recommend_3": f"{url_3}",
        "recommend_4": f"{url_4}",
        "recommend_5": f"{url_5}",
        "recommend_6": f"{url_6}"
    }