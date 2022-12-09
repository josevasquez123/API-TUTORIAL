from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from .. import models, utils, schemas, oauth2

router = APIRouter(
    prefix="/login",
    tags=['Authentication']
    )

@router.post("/", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    access_token = oauth2.create_access_token(data={"user_id":user.id})

    return {"access_token": access_token, "token_type": "bearer"}