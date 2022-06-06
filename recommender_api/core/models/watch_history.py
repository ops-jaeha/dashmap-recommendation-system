# Import Library
from sqlalchemy import Column, INTEGER, ForeignKey
from recommender_api.core.models import Base


class WatchHistory(Base):
    __tablename__ = "watch_history"

    user_id = Column(INTEGER, ForeignKey("member.id"), nullable=True)
    lecture_id = Column(INTEGER, ForeignKey("lecture.id"), nullable=True)
    ratings = Column(INTEGER)