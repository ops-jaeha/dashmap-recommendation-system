# Import Library
from sqlalchemy import Column, VARCHAR, BIGINT
from recommender_api.core.models import Base


class Member(Base):
    __tablename__ = "member"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    email = Column(VARCHAR)
    name = Column(VARCHAR)
    profile_image_url = Column(VARCHAR)
    role = Column(VARCHAR)