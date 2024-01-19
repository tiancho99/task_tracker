# app/api/users/controllers.py
from app import db
from app.api.users.models import User

def get_users():
    users = db.session.execute(db.select(User)).scalars()
    return [user.serialize() for user in users]


def get_user(user_id):
    user = db.get_or_404(User, user_id)
    return user.serialize()


def create_user(data):
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()


def update_user(user_id, data):
    user = db.get_or_404(User, user_id)
    for k, v in data.items():
        setattr(user, k, v)
    db.session.commit()
    return user.serialize()

def delete_user(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()

    return True