from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///book_collection.db"
engine = create_engine(db_url)
base = declarative_base()

class Book_Details(base):
    __tablename__ = "Book Information"

    id = Column(Integer, primary_key=True)
    book_name = Column(String)
    author = Column(String)
    rating = Column(Integer)

base.metadata.create_all(engine)