from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from ..utils.database import Base
from datetime import datetime
from pydantic import BaseModel

class ProjectMention(Base):
    __tablename__ = "observed_mention_new"

    id = Column(Integer, primary_key=True, nullable=False)
    mentioned_twitter_user_id = Column(Integer, nullable=False)
    mention_created_at = Column(TIMESTAMP(timezone=True), nullable=False)

class Project(Base):
    __tablename__ = "observed"

    id = Column(Integer, primary_key=True, nullable=False)
    twitter_user_id = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    name = Column(String, nullable=False)
    profile_image_url = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

class ProjectResponse(BaseModel):
    id: int
    twitter_user_id: int
    username: str
    name: str
    profile_image_url: str
    created_at: datetime

    class Config:
        from_attributes = True

class ProjectMentionResponse(BaseModel):
    id: int
    username: str
    name: str
    profile_image_url: str
    cnt: int

    class Config:
        from_attributes = True