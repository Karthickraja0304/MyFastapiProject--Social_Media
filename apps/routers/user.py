from fastapi import FastAPI, status, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .. import models, utils, schema
from ..database import get_db

router = APIRouter(
    prefix= "/users",
    tags= ["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schema.UserRES)
def new_user(user: schema.UserCreate, db:Session = Depends(get_db)):
    ##hatch password
    hashed_pass = utils.hash(user.password)
    user.password = hashed_pass
    
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schema.UserRES)
def get_user(id:int, db: Session = Depends(get_db)):
    target_user = db.query(models.Users).filter(models.Users.id == id).first()
    
    if not target_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user id {id} is not found")
    
    return target_user