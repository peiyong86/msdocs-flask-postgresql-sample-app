from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import validates

from app import db


class Quota(db.Model):
    __tablename__ = 'quota'
    qid = Column(Integer, primary_key=True)
    user = Column(String(50))
    # date_month = Column(String(DateTime))
    date_month = Column(String(50))
    amount = Column(Integer)
    # qid = mapped_column(Integer, primary_key=True)
    # user = mapped_column(String, unique=False, nullable=False)
    # date_month = mapped_column(String)
    # amount = mapped_column(Integer)

    def serialize(self):
        return {
            'qid': self.qid,
            'user': self.user,
            'date_month': self.date_month,
            'amount': self.amount,
            # ... additional properties you want to include go here
        }

    def __str__(self):
        return self.name


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    street_address = Column(String(50))
    description = Column(String(250))

    def __str__(self):
        return self.name


class Woods(db.Model):
    __tablename__ = 'woods'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    street_address = Column(String(50))
    description = Column(String(250))

    def __str__(self):
        return self.name


# class Review(db.Model):
#     __tablename__ = 'review'
#     id = Column(Integer, primary_key=True)
#     restaurant = Column(Integer, ForeignKey('restaurant.id', ondelete="CASCADE"))
#     user_name = Column(String(30))
#     rating = Column(Integer)
#     review_text = Column(String(500))
#     review_date = Column(DateTime)
#
#     @validates('rating')
#     def validate_rating(self, key, value):
#         assert value is None or (1 <= value <= 5)
#         return value
#
#     def __str__(self):
#         return f"{self.user_name}: {self.review_date:%x}"
