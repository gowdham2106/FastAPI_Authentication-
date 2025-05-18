from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, database, hassing
from sqlalchemy.orm import Session
from ..repository import user
router = APIRouter(
    tags=['Users'],
    prefix='/user'
)

@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(database.get_db)):
    
    return user.create_user(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(database.get_db)): 
    return user.show(id,db)