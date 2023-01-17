from fastapi import APIRouter, Depends, status, HTTPException, FastAPI
from sqlalchemy.orm import Session
from .. import schema, models, outh2, database
from . import post

router = APIRouter(tags=['votes'],prefix="/votes")
           



@router.post("/",status_code=status.HTTP_201_CREATED)
def voting(vote:schema.Voteschema, db:Session = Depends(database.get_db),
            current_user:int = Depends(outh2.get_current_user) ):
            
            check_post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
            if not check_post:            
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"The req post id : {vote.post_id} is not present")
            vote_query = db.query(models.Votes).filter(models.Votes.posts_id == vote.post_id, models.Votes.users_id == current_user.id)
            found_vote = vote_query.first()
            if (vote.vote_dir == 0):
                if found_vote:
                    vote_query.delete(synchronize_session=False)
                    db.commit()
                    return {"message":f"You have removed vote from post with id : {vote.post_id}"}
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                    detail=f'You have already removed vote from post id : {vote.post_id}')                
            else:
                if not found_vote:
                    new_vote = models.Votes(posts_id = vote.post_id, users_id = current_user.id)
                    db.add(new_vote)
                    db.commit()
                    return {"message":f"You have voted for the post id: {vote.post_id} successfully"}
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                    detail=f'You have already voted for post id : {vote.post_id}')                