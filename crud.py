from sqlalchemy.orm import Session
from . import models, schemas

def get_url_by_code(db: Session, code: str):
    return db.query(models.URL).filter(models.URL.short_code == code).first()

def create_url(db: Session, url: schemas.URLCreate):
    db_url = models.URL(long_url=url.long_url, short_code=url.short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url
