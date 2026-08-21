## database.py
from sqlalchemy import create_engine    # needed to create a connection to the database
from sqlalchemy.orm import DeclarativeBase, sessionmaker 
# DeclarativeBase is needed to create a base class for our models, 
# sessionmaker is needed to create a session factory for interacting with the database

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    with SessionLocal() as db:
        yield db