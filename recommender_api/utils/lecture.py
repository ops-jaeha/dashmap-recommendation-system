# Import Library
from sqlalchemy.orm import Session

# Import File
from recommender_api.core.models.watch_history import WatchHistory


def recode_lecture(session: Session, u_id: int, l_id: int, r: int = 5):
    session.add(
        WatchHistory(user_id=u_id, lecture_id=l_id, ratings=r)
    )
    session.commit()