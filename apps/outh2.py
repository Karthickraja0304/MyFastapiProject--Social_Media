from jose import JWTError, jwt
from datetime import datetime, timedelta
import time
from . import schema, database, models
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



SECRET_KEY = settings.web_token_secret_key
ALGORITHM = settings.web_token_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.web_token_expiration_time

def create_access_token(data:dict):
    to_encode = data.copy()

    expire = time.time() + 600
    to_encode.update({"expiration":expire})

    

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)
    
    return encoded_jwt 

def verify_acces_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id:str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schema.TokenData(id=id)
    
    except JWTError:
        raise credentials_exception
    
    return token_data

def get_current_user(token:str = Depends(oauth2_scheme), db:Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, 
                                        detail= "Couldnot validate current credentials",
                                        headers={"WWW-Authenticate":"Bearer"})
    token =  verify_acces_token(token, credentials_exception) 
    #print(token.id)                                       
    #print(token)                                       
    user = db.query(models.Users).filter(models.Users.id == token.id).first()

    return user