# app/api/tasks/controllers.py
from app.api.tasks.models import Task, TaskStatus
from app.api.projects.models import Project
from app import db

def get_tasks():
    tasks = db.session.execute(db.select(Task)).scalars()
    return [task.serialize() for task in tasks]

def get_task(task_id):
    task = db.get_or_404(Task, task_id)
    return task.serialize()

def create_task(data):
    new_task = Task(**data)
    Task.users = [new_task]
    db.session.add(new_task)
    db.session.commit()
    return new_task.serialize()

def update_task(task_id, data):
    task = db.get_or_404(Task, task_id)

    task.name = data.get("name", task.name)
    task.description = data.get("description", task.description)
    task.importance = data.get("importance", task.importance)
    task.set_due_date(data.get("due_date"))

    db.session.commit()
    return task.serialize()

def delete_task(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    return True

# Status methods
 
def get_status():
    status = db.session.execute(db.select(TaskStatus)).scalars()
    return [st.serialize() for st in status]

def get_st(status_id):
    status = db.get_or_404(TaskStatus, status_id)
    return status.serialize()

def create_status(data):
    project = db.session.execute(db.select(Project).where(Project.id == data.pop("project_id"))).scalars()
    data["project"] = list(project)
    new_status = TaskStatus(**data)
    Task.users = [new_status]
    db.session.add(new_status)
    db.session.commit()
    return new_status.serialize()

def update_status(status_id, data):
    status = db.get_or_404(TaskStatus, status_id)
    for k, v in data.items():
        setattr(status, k, v)

    db.session.commit()
    return status.serialize()

def delete_status(status_id):
    status = db.get_or_404(TaskStatus, status_id)
    db.session.delete(status)
    db.session.commit()
    return True