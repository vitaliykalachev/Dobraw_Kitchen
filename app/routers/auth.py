from fastapi import APIRouter, Depends, status, HTTPException, Response, Request, responses
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])



@router.post('/login', response_model=schemas.Token)
async def login(response: Response, user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    { 
     "username": "bla",
     "password": "bla"
    }
    
    user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    #create a token
    #return token
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    # return templates.TemplateResponse("login.html", {"request": request, "message": message, "access_token" : access_token, "token_type": "bearer"})
    return {"access_token" : access_token, "token_type": "bearer"}

    # access_token = oauth2.create_access_token(data = {"sub": user.email})
    # response = responses.RedirectResponse("/?message=Succesfully Registered", status_code=status.HTTP_302_FOUND)
    # response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    