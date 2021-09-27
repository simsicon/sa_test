from sqlalchemy import select
from .model import engine, Session, Student, Report

import datetime
import pandas as pd


def prepare_test_data():

    with Session() as session:
        session.query(Report).delete()
        session.query(Student).delete()

        sa = Student(name="A", age=18)
        sb = Student(name="B", age=19)

        session.add(sa)
        session.add(sb)

        session.add(Report(publish_date=datetime.date(
            2021, 8, 15), student_name=sa.name, score=80))
        session.add(Report(publish_date=datetime.date(
            2021, 8, 15), student_name=sa.name, score=86))
        session.add(Report(publish_date=datetime.date(
            2021, 8, 18), student_name=sb.name, score=85))

        session.commit()


def test_distinct_on():
    prepare_test_data()

    stmt = select(
        Student.name, Report.publish_date, Report.score, Student.age
    ).distinct(
        Student.name, Report.publish_date
    ).join(
        Report, Student.name == Report.student_name
    ).order_by(
        Student.name, Report.publish_date, Report.score.desc()
    )

    df = pd.read_sql(stmt, con=engine)
    assert df.shape[0] == 2