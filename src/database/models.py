from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SearchResult(Base):
    __tablename__ = 'search_results'

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    title = Column(String)
    content = Column(Text)
    summary = Column(Text)
    relevance_score = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)