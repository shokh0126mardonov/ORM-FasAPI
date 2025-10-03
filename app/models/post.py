from sqlalchemy import (
    Column,String,Integer,Text,ForeignKey
)

from ..db import Base

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    description= Column(Text)
    user_id = Column(ForeignKey('users.id',ondelete='CASCADE'),nullable=False)
    
    def __repr__(self):
        return f"Post(id={self.id}, title={self.title}, description={self.description[:20]})"