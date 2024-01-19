from app import db
from app.api.groups.models import Group
from app.api.users.models import User


def get_groups():
    groups = db.session.execute(db.select(Group)).scalars()
    return [group.serialize() for group in groups]

def get_group(group_id):
    group = db.get_or_404(Group, group_id)
    return group.serialize()

def create_group(data):
    users_mail = data.get("users")
    data["users"] = list(db.session.execute(db.select(User).where(User.email.in_(users_mail))).scalars())
    new_group = Group(**data)
    db.session.add(new_group)
    db.session.commit() #

    # new_group.users.append(users)
    # db.session.commit()
    return new_group.serialize()

def update_group(group_id, data):
    users_mail = data.get("users")
    data["users"] = list(db.session.execute(db.select(User).where(User.email.in_(users_mail))).scalars())

    group = db.get_or_404(Group, group_id)
    for k, v in data.items():
        setattr(group, k, v)

    db.session.commit()
    return group.serialize()

def delete_group(group_id):
    group = db.get_or_404(Group, group_id)
    db.session.delete(group)
    db.session.commit()
    return True

  