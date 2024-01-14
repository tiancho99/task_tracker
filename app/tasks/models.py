from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app import db

class Task(db.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String)
    importance: Mapped[str] = mapped_column(String)
    creation_date: Mapped[datetime] = mapped_column(Date)
    due_date: Mapped[datetime] = mapped_column(Date)
    status_id = mapped_column(ForeignKey("status.id"), nullable=False)
    
    def __init__(self, id, name, description, importance,
                 creation_date, due_date, status_id):
        self.id = id
        self.name = name
        self.description = description
        self.importance = importance
        self.creation_date = creation_date
        self.due_date = due_date

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "importance": self.importance,
            "creation_date": self.creation_date,
            "due_date": self.due_date,
        }
