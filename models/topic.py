from sqlalchemy import String, Column, Integer

from models.base import SQLMixin, db


class Topic(SQLMixin, db.Model):
    content = Column(String(50), nullable=False)
    status = Column(Integer, default=1)

    def switch(self):
        self.status = 0 if self.status == 1 else 1
        self.update()

    @classmethod
    def all(cls, **kwargs):
        return cls.query.filter_by(**kwargs).order_by(cls.status.desc(), cls.create_time).all()

    @classmethod
    def all_used(cls):
        return cls.query.filter(cls.status == 1).order_by(cls.create_time).all()
