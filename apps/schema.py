from pydantic import BaseModel, EmailStr, conint
from typing import Optional 
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr 
    password: str
    phone_number: str

class UserRES(BaseModel):
    id: int
    email : EmailStr
    created_at : datetime
    
    class Config:
        orm_mode = True
        
class Userlogin(BaseModel):
    email: EmailStr
    password : str

class token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None



class PostBase(BaseModel): 
    title : str
    content : str
    location : str
    published : bool =True

class PostCreate(PostBase):
    pass

class PostRES(PostBase):
    id: int
    owner_id : int
    owner : UserRES    

    class Config:
        orm_mode = True

class Postoutvotes(BaseModel):
    Post: PostRES
    votes:int
    
    class Config:
        orm_mode = True

class Voteschema(BaseModel):
    post_id : int
    vote_dir : conint(le=1)
 
