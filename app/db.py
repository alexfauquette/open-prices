from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

url = URL.create(
    drivername="postgresql",
    database=settings.postgres_db,
    username=settings.postgres_user,
    password=settings.postgres_password,
    host=settings.postgres_host,
    port=settings.postgres_port,
)

engine = create_engine(url)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
