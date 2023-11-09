from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Env
from decouple import config


url = URL.create(
    drivername=config('DRIVER_NAME'),
    username=config('DB_USER'),
    host=config('DB_HOST'),
    database=config('DB_NAME'),
    password=config('DB_PASS'),
    port=config('DB_PORT')
)


engine = create_engine(url)
connection = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()