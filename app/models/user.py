from sqlalchemy import (
    Column,String,Integer
)

from ..db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String)
    gender = Column(String,nullable=False)
    username = Column(String,nullable=False,unique=True)
    phone = Column(String,nullable=False)