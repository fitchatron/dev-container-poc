import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import Base

# Define the database URL (replace with your actual database URL)
DATABASE_URL = "mssql+pyodbc:///?odbc_connect=%s"% urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};Server=db;Database=test_docker;Uid=sa;Pwd=Changem3;Connection Timeout=30;")

engine = create_engine(
    DATABASE_URL,
    # connect_args={"autocommit": True},
    echo=True,
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()