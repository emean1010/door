from sqlalchemy import String, Column

from models.base import SQLMixin, db


class Topic(SQLMixin, db.Model):
    content = Column(String(50), nullable=False)
