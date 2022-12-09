
from .. import schemas, models, utils
from fastapi import status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate,db: Session = Depends(get_db)):

    pwd_crypted = utils.hash(user.password)
    user.password = pwd_crypted

    #cursor.execute(""" INSERT INTO users(email, password) VALUES (%s,%s) RETURNING *""",(user.email,  user.password))
    #new_user = cursor.fetchone()
    #conn.commit()

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: str,db: Session = Depends(get_db)):
    #cursor.execute(""" SELECT * FROM users WHERE id = %s """, (str(id)))
    #user = cursor.fetchone()
    
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id: {id} was not found')

    return user