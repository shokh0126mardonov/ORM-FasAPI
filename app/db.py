from sqlalchemy import URL,create_engine
from .config import setting
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

url_object = URL.create(
    'postgresql+psycopg2',
    username = setting.DB_USER,
    password = setting.DB_PASSWORD,
    port = setting.DB_PORT,
    host = setting.DB_HOST,
    database = setting.DB_NAME 
)

engine = create_engine(url_object)

LocalSesion = sessionmaker(bind=engine)

Base = declarative_base()

def initinal_db():
    from .models import User
    from .models import Post
    from .models import Comment

    Base.metadata.create_all(engine)

