from sqlalchemy import create_engine, select, func, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Date
import datetime
import pandas as pd

# SQLAlchemy==1.4.23 psycopg2==2.9.1 with postgresql 13
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/sa_test?sslmode=disable", echo=False)
Session = sessionmaker(engine)

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    name = Column(String, primary_key=True)
    age = Column(Integer)


class Report(Base):
    __tablename__ = 'report'

    id = Column(Integer, primary_key=True)
    publish_date = Column(Date)
    student_name = Column(String)
    score = Column(Integer)

Base.metadata.create_all(engine)