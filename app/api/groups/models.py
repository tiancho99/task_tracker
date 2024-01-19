# groups/models.py
from __future__ import annotations
from sqlalchemy import String, Integer, Date, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from app import db

from datetime import datetime

class Group(db.Model):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String)
    creation_date: Mapped[datetime] = mapped_column(Date)
    users: Mapped[List["User"]] = relationship(back_populates="groups", secondary="users_groups_m2m")
    projects: Mapped[List["Project"]] = relationship(back_populates="group")

    def __init__(self, name, description, users=[], projects=[]) -> None:
        self.name = name
        self.description = description
        self.creation_date = datetime.now()
        self.users = users
        self.projects = projects

    def serialize(self, relationship=True):
        serialized_data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
        }
        if relationship:
            serialized_data["users"] = [user.serialize(False) for user in self.users]
            serialized_data["projects"] = [project.serialize(False) for project in self.projects]

        return serialized_data

