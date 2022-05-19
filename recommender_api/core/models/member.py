# Import Library
from sqlalchemy import Column, BigInteger, VARCHAR
from recommender_api.config import Base


class Member(Base):
    __tablename__ = "member"

    id = Column(BigInteger, primary_key=True)
    email = Column(VARCHAR(255))
    name = Column(VARCHAR(255))
    profile_image_url = Column(VARCHAR(255))
    role = Column(VARCHAR(255))