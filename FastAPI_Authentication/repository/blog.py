from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from ..import models,schemas

def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs
def create(db:Session,request):
    new_blog=models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
def destroy(id:int,db:Session):
     blog=db.query(models.Blog).filter(models.Blog.id==id)
     if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
     blog.delete(synchronize_session=False)
     db.commit()
     return True
def show(id,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
       #response.status_code=status.HTTP_404_NOT_FOUND
        #return {'details':f'Blog with id {id} is not available'}
    return blog
def update(id,request:schemas.Blog,db:Session):
   blog= db.query(models.Blog).filter(models.Blog.id==id)
   if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
   blog.update(request.dict())
   db.commit()