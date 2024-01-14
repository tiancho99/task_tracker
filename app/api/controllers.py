# app/api/controllers.py
from app.tasks.models import Task
from app import db
from flask import abort

def get_tasks():
    tasks = db.session.execute(db.select(Task)).scalars()
    return [{'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status} for task in tasks]

def get_task(task_id):
    task = db.get_or_404(Task, task_id)
    return {'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status}

def create_task(data):
    new_task = Task(title=data['title'], description=data['description'], status=data['status'])
    db.session.add(new_task)
    db.session.commit()
    return {'id': new_task.id, 'title': new_task.title, 'description': new_task.description, 'status': new_task.status}

def update_task(task_id, data):
    task = db.get_or_404(Task, task_id)
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)
    db.session.commit()
    return {'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status}

def delete_task(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    return True
  