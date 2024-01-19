# tasks/models.py
from sqlalchemy import String, Integer, DateTime, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from sqlalchemy import Table, Column, ForeignKey

from app import db
from app.utils import date_format
from app.api.projects.models import Project
from datetime import datetime

projects_status_m2m = Table(
    "projects_status_m2m",
    db.metadata,
    Column("project_id", ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True),
    Column("task_status_id", ForeignKey("task_status.id", ondelete="CASCADE"), primary_key=True)
)

#TODO: not allow repeated status names
class TaskStatus(db.Model):
    __tablename__ = "task_status"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    tasks: Mapped[List["Task"]] = relationship(back_populates="status")
    projects: Mapped[List["Project"]] = relationship(back_populates="task_status", secondary="projects_status_m2m")


    def __init__(self, name, project=None) -> None:
        self.name = name
        self.projects = project

    def serialize(self, relationship=True):
        serialized_data = {
            "id": self.id,
            "name": self.name,
        }
        if relationship:
            serialized_data["tasks"] = [task.serialize(False) for task in self.tasks]
            serialized_data["projects"] = [project.serialize(False) for project in self.projects]
        
        return serialized_data

    


# TODO: make status column for Task model
class Task(db.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String)
    importance: Mapped[str] = mapped_column(String)
    creation_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    due_date: Mapped[datetime] = mapped_column(DateTime)
    status_id: Mapped[int] = mapped_column(ForeignKey("task_status.id"), onupdate="CASCADE")
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"))
    status: Mapped["TaskStatus"] = relationship()
    project: Mapped["Project"] = relationship(back_populates="tasks")

    
    def __init__(self, name, description=None, importance=None,
                 due_date=None, project_id=None, status_id=None):
        self.name = name
        self.description = description
        self.importance = importance
        self.creation_date = datetime.now()
        self.set_due_date(due_date)
        self.project_id = project_id
        self.status_id = status_id

    def serialize(self, relationship=True):
        serialized_data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "importance": self.importance,
            "creation_date": self.creation_date,
            "due_date": self.due_date,
        }
        if relationship:
            serialized_data["project"] = self.project.serialize(False)
            serialized_data["status"] = self.status.serialize(False)
        else:
            serialized_data["project_id"] = self.project_id
            serialized_data["status_id"] = self.project_id
        
        return serialized_data


    def set_due_date(self, due_date:str):
        self.due_date = datetime.strptime(due_date, date_format)


    def get_due_date(self):
        return self.due_date
