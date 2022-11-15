import settings
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker


create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}
)

Session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)