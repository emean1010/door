import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime

db = SQLAlchemy()


class SQLMixin(object):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    create_time = Column(DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = Column(DateTime, default=datetime.datetime.now, comment='更新时间')

    @classmethod
    def new(cls, data):
        m = cls()
        for name, value in data.items():
            setattr(m, name, value)

        db.session.add(m)
        return m

    def update(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
        self.update_time = datetime.datetime.now()
        db.session.add(self)

    @classmethod
    def one(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def all(cls, **kwargs):
        return cls.query.filter_by(**kwargs).order_by(cls.update_time.desc()).all()

    @classmethod
    def columns(cls):
        return cls.__mapper__.c.items()

    def __repr__(self):
        name = self.__class__.__name__
        s = ''
        for attr, column in self.columns():
            if hasattr(self, attr):
                v = getattr(self, attr)
                s += '{}: ({})\n'.format(attr, v)
        return '< {}\n{} >\n'.format(name, s)

    def info(self):
        data = dict()
        for k, v in self.__dict__.items():
            if not k.startswith('_'):
                if k.endswith('time'):
                    data[k] = v.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    data[k] = v
        return data
