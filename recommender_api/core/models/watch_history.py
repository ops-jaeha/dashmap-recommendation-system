# Import Library
from sqlalchemy import Column, INTEGER, ForeignKey, BIGINT
from recommender_api.core.models import Base
from recommender_api.core.models.member import Member
from recommender_api.core.models.lecture import Lecture


class WatchHistory(Base):
    __tablename__ = "watch_history"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    user_id = Column(BIGINT, ForeignKey(Member.id), nullable=True)
    lecture_id = Column(BIGINT, ForeignKey(Lecture.id), nullable=True)
    ratings = Column(INTEGER)