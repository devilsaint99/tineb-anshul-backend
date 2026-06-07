from fastapi import FastAPI, Depends, Query
from fastapi.exceptions import HTTPException
from contextlib import asynccontextmanager
from app.db.models import Members
from app.db.session import get_db
from sqlalchemy.orm import Session



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Backend of TINEB starting")
    yield
    print("Backend of TINEB shutting down")


app = FastAPI(
    lifespan=lifespan,
    root_path="/api"
    )


@app.get("/")
def root():
    return "There is No Earth B"

@app.get("/members")
def get_members(page: int = Query(1, ge=1), limit: int|None = Query(None, ge=1), db: Session = Depends(get_db)):
    query = db.query(Members)
    if limit is not None:
        offset = (page-1)*limit
        query = query.offset(offset).limit(limit)
        
    return query.all()