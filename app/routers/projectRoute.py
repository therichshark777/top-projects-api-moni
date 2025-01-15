from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session

from ..utils import dependencies

from ..controllers import projectController
from ..models.projectModel import ProjectResponse, ProjectMentionResponse

router = APIRouter()

# Создать БД
get_db = dependencies.get_db

@router.get("/", response_model=list[ProjectMentionResponse])
def get_projects(limit: int = Query(50, ge=1, le=100),db: Session = Depends(get_db)):
    return projectController.get_projects(db, limit, '1 day')

@router.get("/7days", response_model=list[ProjectMentionResponse])
def get_projects(limit: int = Query(50, ge=1, le=100),db: Session = Depends(get_db)):
    return projectController.get_projects(db, limit, '7 days')

@router.get("/30days", response_model=list[ProjectMentionResponse])
def get_projects(limit: int = Query(50, ge=1, le=100),db: Session = Depends(get_db)):
    return projectController.get_projects(db, limit, '30 days')

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = projectController.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project