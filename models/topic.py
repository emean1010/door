from sqlalchemy import String, Column, Integer

from models.base import SQLMixin, db


class Topic(SQLMixin, db.Model):
    content = Column(String(50), nullable=False)
    status = Column(Integer, default=1)
    pid = Column(String(10))

    pid_default = '1200650'

    @classmethod
    def new(cls, data):
        if not data.get('pid'):
            data.update(pid=cls.pid_default)
        return super().new(data)

    def update(self, **kwargs):
        if not kwargs.get('pid'):
            kwargs.update(pid=self.pid_default)
        super().update(**kwargs)

    def switch(self):
        self.status = 0 if self.status == 1 else 1
        self.update()

    @classmethod
    def all(cls, **kwargs):
        return cls.query.filter_by(**kwargs).order_by(cls.status.desc(), cls.create_time).all()

    @classmethod
    def all_used(cls):
        return cls.query.filter(cls.status == 1).order_by(cls.create_time).all()

    @property
    def format_pid(self):
        if not self.pid:
            return ''
        return self.pid[:2] + '**' + self.pid[4:7]
