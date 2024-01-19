# app/api/projects/controllers.py
from app.api.projects.models import Project
from app import db

def get_project():
    projects = db.session.execute(db.select(Project)).scalars()
    return [project.serialize() for project in projects]

def get_projects(project_id):
    project = db.get_or_404(Project, project_id)
    return project.serialize()

def create_project(data):
    new_project = Project(**data)
    db.session.add(new_project)
    db.session.commit()
    return new_project.serialize()

def update_project(project_id, data):
    project = db.get_or_404(Project, project_id)
    for k, v in data.items():
        setattr(project, k, v)

    db.session.commit()
    return project.serialize()

def delete_project(project_id):
    project = db.get_or_404(Project, project_id)
    db.session.delete(project)
    db.session.commit()
    return True

  