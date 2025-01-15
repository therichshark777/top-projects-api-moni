from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from sqlalchemy.sql import text
from ..models.projectModel import Project, ProjectMention


def get_projects(db: Session, limit, interval):
    query = (
        db.query(
            Project.id,
            Project.username,
            Project.name,
            Project.profile_image_url,
            func.count().label("cnt"),
        )
        .select_from(ProjectMention)
        .join(
            Project,
            ProjectMention.mentioned_twitter_user_id == Project.twitter_user_id
        )
        .filter(
            ProjectMention.mention_created_at >= text(f"NOW() - INTERVAL '{interval}'")
        )
        .group_by(
            Project.id,
            Project.username,
            Project.name,
            Project.profile_image_url,
            ProjectMention.mentioned_twitter_user_id,
        )
        .order_by(desc("cnt"))
        .limit(limit)
    )
    return query.all()


def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()