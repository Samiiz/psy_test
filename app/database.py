from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# local = "postgresql+psycopg2://samiiz:Parkshghfh9801!@localhost/psy_test"
# db = "postgresql+psycopg2://samiiz:Parkshghfh9801!@db/psy_test"


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://samiiz:Parkshghfh9801!@db/psy_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()