# Import Library
from sqlalchemy import Column, INTEGER, ForeignKey, BIGINT
from recommender_api.core.models import Base


class WatchHistory(Base):
    __tablename__ = "watch_history"

    id = Column(BIGINT, primary_key=True, nullable=True)
    user_id = Column(BIGINT, ForeignKey("member.id"), nullable=True)
    lecture_id = Column(BIGINT, ForeignKey("lecture.id"), nullable=True)
    ratings = Column(INTEGER)