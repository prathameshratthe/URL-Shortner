from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import string, random

from . import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def generate_short_code(length: int = 6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.post("/shorten", response_model=schemas.URL)
def create_short_url(url: schemas.URLCreate, db: Session = Depends(database.get_db)):
    url.short_code = generate_short_code()
    return crud.create_url(db=db, url=url)

@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(database.get_db)):
    db_url = crud.get_url_by_code(db, short_code)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"long_url": db_url.long_url}
