# Import Libray
from fastapi import APIRouter, status

# Import File
from recommender_api.core.models import session_scope
from recommender_api.utils.recommend import recommend


router = APIRouter()


@router.get("/recommend/{user_id}", status_code=status.HTTP_200_OK, tags=["recommendation"])
async def user_recommend(user_id: int):
    with session_scope() as session:
        id_lst, url_lst = recommend(session=session, u_id=user_id)

        return {
            "recommend_1": [{"id": f"{id_lst[0]}"},
                            {"url": f"{url_lst[0]}"}],
            "recommend_2": [{"id": f"{id_lst[1]}"},
                            {"url": f"{url_lst[1]}"}],
            "recommend_3": [{"id": f"{id_lst[2]}"},
                            {"url": f"{url_lst[2]}"}],
            "recommend_4": [{"id": f"{id_lst[3]}"},
                            {"url": f"{url_lst[3]}"}],
            "recommend_5": [{"id": f"{id_lst[4]}"},
                            {"url": f"{url_lst[4]}"}],
            "recommend_6": [{"id": f"{id_lst[5]}"},
                            {"url": f"{url_lst[5]}"}]
        }