# Import Library
from sqlalchemy import Column, VARCHAR, BIGINT
from recommender_api.core.models import Base


class Lecture(Base):
    __tablename__ = "lecture"

    id = Column(BIGINT, primary_key=True)
    field = Column(VARCHAR)
    url = Column(VARCHAR)