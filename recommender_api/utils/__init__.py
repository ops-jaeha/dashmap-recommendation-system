# Import Library
from sqlalchemy.orm import Session

# Import File
from recommender_api.core.models.watch_history import WatchHistory


def is_watched(session: Session, user_id: int):
    try:
        watch_bool = session.query(WatchHistory).filter(WatchHistory.user_id == f"{user_id}").first()
        return watch_bool.lecture_id
    except:
        return False