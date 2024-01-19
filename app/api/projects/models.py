# projects/models.py
from sqlalchemy import String, Integer, DateTime, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import db
from app.utils import date_format
from datetime import datetime
from typing import Optional, List


class Project(db.Model):
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String)
    creation_date: Mapped[str] = mapped_column(DateTime)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), nullable=False)
    group: Mapped["Group"] = relationship(back_populates="projects")
    tasks: Mapped[List["Task"]] = relationship(back_populates="project")

    task_status: Mapped[List["TaskStatus"]] = relationship(back_populates="projects", secondary="projects_status_m2m")


    def __init__(self, name, description=None, group_id=None) -> None:
        self.name = name
        self.description = description
        self.creation_date = datetime.now()
        self.group_id = group_id
        # self.group = group
        # self.tasks = tasks
    

    def serialize(self, relationship=True):
        serialized_data =  {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
        }
        if relationship:
            serialized_data["group"] = self.group.serialize(False)
            serialized_data["tasks"] = [task.serialize(False) for task in self.tasks]
            serialized_data["task_status"] = [status.serialize(False) for status in self.task_status]
        
        return serialized_data

    

