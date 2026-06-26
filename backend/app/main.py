from fastapi import FastAPI, Depends, Query
from fastapi.exceptions import HTTPException
from contextlib import asynccontextmanager
from app.db.models import Members
from app.db.session import get_db
from sqlalchemy.orm import Session
from sqlalchemy import or_
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Backend of TINEB starting")
    yield
    print("Backend of TINEB shutting down")


app = FastAPI(
    lifespan=lifespan,
    root_path="/api"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], #just for this assignement as I have not yet planned on the deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


@app.get("/search")
def search(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    
    results = (
        db.query(Members).filter(
            or_(
                Members.name.ilike(f"%{q}%"),
                Members.party.ilike(f"%{q}%"),
                Members.state.ilike(f"%{q}%"),
                Members.constituency.ilike(f"%{q}%"),
            )
        )
        .all()
    )

    return {
        "query": q,
        "length": len(q),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "results": results,
    }