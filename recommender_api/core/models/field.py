# Import Library
from sqlalchemy import Column, BigInteger, BIGINT
from recommender_api.config import Base


class Field(Base):
    __tablename__ = "field"

    id = Column(BigInteger, primary_key=True)
    frontend = Column(BIGINT, nullable=True, default=0)
    backend = Column(BIGINT, nullable=True, default=0)
    android = Column(BIGINT, nullable=True, default=0)
    ios = Column(BIGINT, nullable=True, default=0)
    ai = Column(BIGINT, nullable=True, default=0)
    embedded = Column(BIGINT, nullable=True, default=0)