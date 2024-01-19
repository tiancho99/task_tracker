#users/models.py
from __future__ import annotations
from sqlalchemy import String, Integer, DateTime, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List

from app import db


users_groups_m2m = Table(
    "users_groups_m2m",
    db.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("group_id", ForeignKey("groups.id", ondelete="CASCADE"), primary_key=True)
)

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    lastname: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    groups: Mapped[List["Group"]] = relationship(back_populates="users", secondary="users_groups_m2m")

    def __init__(self, name, lastname, email, groups=[]):
        self.name = name
        self.lastname = lastname
        self.email = email
    
    def serialize(self, relationship=True):
        serialized_data = {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
        }
        if relationship:
            serialized_data["groups"] = [group.serialize(False) for group in self.groups]
            print(serialized_data["groups"])

        return serialized_data

    def set_password(self, password):
        pass

    def check_password(self, password):
        pass
