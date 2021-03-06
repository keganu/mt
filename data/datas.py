import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase

class Datas(SqlAlchemyBase):
    __tablename__ = 'datas'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    value = sqlalchemy.Column(sqlalchemy.Float, default=0)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)


    def __str__(self):
        return f'{self.id} {self.value} {self.created_date}'

