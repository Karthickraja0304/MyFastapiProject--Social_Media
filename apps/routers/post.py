from fastapi import  FastAPI, status, Depends, HTTPException, Response, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schema, outh2
from ..database import get_db
from sqlalchemy import func


router = APIRouter(
    prefix= "/posts",
    tags= ["Posts"]     
)


@router.get("/",response_model= List [schema.Postoutvotes])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(outh2.get_current_user),
limit:int = 6, skip:int = 0, search: Optional[str]= ""):
    
    results = db.query(models.Post, func.count(models.Votes.posts_id).label("votes")).join(
                models.Votes, models.Votes.posts_id == models.Post.id, isouter= True).group_by(
                models.Post.id).filter(models.Post.content.contains(search)).limit(limit).offset(
                skip).all()
    
    return  results


@router.post('/',status_code=status.HTTP_201_CREATED,response_model= schema.PostRES)
def create_post(posts :schema.PostCreate ,db:Session = Depends(get_db), current_user: int = Depends(outh2.get_current_user)):
    print(current_user)
    new_post = models.Post(owner_id = current_user.id, **posts.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model= schema.Postoutvotes)
def get_one_post(id:int,db:Session = Depends(get_db), current_user: int = Depends(outh2.get_current_user)):
    
    
    target_post = db.query(models.Post, func.count(models.Votes.posts_id).label("votes")).join(
                models.Votes, models.Votes.posts_id == models.Post.id, isouter= True).group_by(
                models.Post.id).filter(models.Post.id == str(id)).first()
    print(target_post)

    if not target_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post iiid {id} is not found")
    
    
    if target_post.Post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="NOT AUTHORIZED TO PERFORM THIS OPERATION")


    return target_post




@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db),current_user: int = Depends(outh2.get_current_user)):
    del_post_query = db.query(models.Post).filter(models.Post.id == str(id))
    
    if not del_post_query.first() :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'The requested id {id} is not found')
    
    if del_post_query.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="NOT AUTHORIZED TO PERFORM THIS OPERATION")

    del_post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schema.PostRES)
def update_posts(id:int,post:schema.PostCreate,db:Session = Depends(get_db),current_user: int = Depends(outh2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    if not post_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'The requested id {id} is not found')
    
    if post_query.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="NOT AUTHORIZED TO PERFORM THIS OPERATION")

    
    post_query.update(post.dict(),synchronize_session = False)
    db.commit()
    return post_query.first()

