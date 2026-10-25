import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Load the hidden variables from the .env file

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# 1. Create the SQLAlchemy engine that connects to MySQL
engine = create_engine(DATABASE_URL)

# 2. Create a Session factory to handle transactions
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)

# 3. Base class for our database models
Base = declarative_base()

# 4. Define your Database Table as a python class (ORM Model)

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    text = Column(String(255), nullable = False)
    completed = Column(Boolean, default = False)
    priority = Column(String(50), default = "Medium")
    due_date = Column(String(50), default = "None")

# Automatically create the table in MySQL if it doesn't exist

Base.metadata.create_all(bind=engine)

def load_tasks():
    """Reads all the tasks from MySQL using SQLAlchemy and returns a list of dicts."""

    db = SessionLocal()
    try:

        # Query all rows from the tasks table
        db_tasks = db.query(TaskModel).all()

        # Convert alchemy objects into standard Python dictionaries

        tasks_list = []
        for t in db_tasks:
            tasks_list.append({
                "text": t.text,
                "completed": t.completed,
                "priority": t.priority,
                "due_date": t.due_date
            })

        return tasks_list
    finally:
        db.close()

def save_tasks(tasks):

    """
    Overwrites the database table with the current active list of tasks.
    """

    db = SessionLocal()
    try:

        #1. Clear out existing rows
        db.query(TaskModel).delete()

        #2. Add each task from the Python list as a new SQLAlchemy model
        for t in tasks:
            new_task = TaskModel(
                text = t["text"],
                completed = t["completed"],
                priority = t["priority"],
                due_date = t["due_date"]
            )
            db.add(new_task)

        #3. Commit the transaction to MySQL
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error saving tasks: {e}")
    finally:
        db.close()