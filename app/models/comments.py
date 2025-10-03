from sqlalchemy import (
    Column,String,Integer,Text,ForeignKey
)

from ..db import Base

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer,primary_key=True,index=True)
    text = Column(Text,nullable = False)

    user_id = Column(ForeignKey('users.id'),nullable=False)
    post_id = Column(ForeignKey('posts.id'),nullable=False)

    def __repr__(self):
        return f"Post(id={self.id})"