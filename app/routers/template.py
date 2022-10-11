import email
from fastapi import FastAPI, APIRouter, Request, Depends, responses, status, Response
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from models import User
from jose import jwt
from config import settings
from sqlalchemy.orm import Session
from database import get_db
import utils
from . import auth


router = APIRouter(
    prefix='',
    tags=['templates']
)



# class Htmx_template(BaseModel):
#     firstName = str
#     lastName = str
#     email = str

# class Htmx_test(Base):
#     __tablename__ = "htmx_test"
#     id = Column(Integer, primary_key=True, nullable=False)
#     firstName = Column(String, nullable=False)
#     lastName = Column(String, nullable=False)
#     email = Column(String, nullable=False)

templates = Jinja2Templates(directory="templates")



@router.get("/")
async def index(request: Request, message: str = None):
    return templates.TemplateResponse("index.html", {"request": request, "message": message})

@router.get("/test")
async def index(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@router.get("/register")
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
async def register(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    errors = []
    
    if len(password) < 6:
        errors.append("Password should be > 6 character")
        return templates.TemplateResponse("register.html", {"request": request, "errors": errors})
    new_user = User(email=email, password=utils.hash(password))
    
    try: 
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return responses.RedirectResponse("/?message=Succesfully Registered", status_code=status.HTTP_302_FOUND)
    except IntegrityError:
        errors.append("Email already exists")
        return templates.TemplateResponse("register.html", {"request": request, "errors": errors})
    
@router.get("/login")
async def user_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# @router.post("/user_login")
# async def user_login(request: Request):
    
    
#     form = await request.form()
#     username = form.get("username")
#     password = form.get("password")
#     print(form.get("username"))
#     print(form.get("password"))
#     await auth.login(username, password)
    
#     access_token = oauth2.create_access_token(data = {"sub": user.email})
#     response = responses.RedirectResponse("/?message=Succesfully Registered", status_code=status.HTTP_302_FOUND)
#     response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    
    
#     return templates.TemplateResponse("login.html", {"request": request, "message": message})
    
    
    # try: 
    #     user = db.query(User).filter(User.email == user_credentials.username).first()
    #     auth.login()
    #     message = "Login Successful"
    #     return templates.TemplateResponse("login.html", {"request": request, "message": message})
    # except:
    #     pass
    # if not email:
    #     errors.append("Please enter valid email")
    # if not password or len(password) < 5:
    #     errors.append("Password should be > 5 character")
    # try:    
    #     user
    #     data = {"user_id": User.id}
    #     access_token = oauth2.create_access_token(data = {"user_id": User.id})
    #     jwt_token = jwt.encode(data, settings.secret_key, algorithm=settings.algorithm)
        # response.set_cookie(key="access_token", value=f"Bearer {access_token}")
    #     message = "Login Successful"
    #     return templates.TemplateResponse("user_login.html", {"request": request, "message": message}) 
    # except:
    #     pass
    # #     if not user:
    #         errors.append("Email does not exists")
    #         return templates.TemplateResponse("login.html", {"request": request, "errors": errors})
    #     if not utils.verify(user_credentials.password, user.password):
    #         errors.append("Invalid password")
    #         return templates.TemplateResponse("login.html", {"request": request, "errors": errors})
    #     else:
    #         access_token = oauth2.create_access_token(data = {"user_id": user.id})
    #         message = "Login Successful"
    #         return templates.TemplateResponse("login.html", {"request": request, "message": message}) 
    # except:
    #     errors.append("Something wrong") 
    #     return templates.TemplateResponse("login.html", {"request": request, "errors": errors})   
    #create a token
    #return token
    
    
    
    
    # return {"access_token" : access_token, "token_type": "bearer"}   
        
        
    # try:
    #     user = db.query(User).filter(
    #     User.email == user_credentials.username).first()
    #     if user is None:
    #         errors.append("Email does not exists")
    #         return templates.TemplateResponse("login.html", {"request": request, "errors": errors})
    #     else:
    #         if utils.verify(user_credentials.password, user.password):
    #             data = {"sub":email}
    #             jwt_token = jwt.encode(data, settings.secret_key, algorithm=settings.algorithm)
    #             response.set_cookie(key="access_token", value=f"Bearer {jwt_token}", httponly=True)
    #             message = "Login Successful"
    #             return templates.TemplateResponse("login.html", {"request": request, "message": message})
    #         else:
    #             errors.append("Invalid password")
    #             return templates.TemplateResponse("login.html", {"request": request, "errors": errors})
    # except:
    #     errors.append("Something wrong") 
    #     return templates.TemplateResponse("login.html", {"request": request, "errors": errors})











@router.get("/test2")
async def test2(request: Request):
    return templates.TemplateResponse("test2.html", {"request": request})

@router.put("/test2")
async def test2(request: Request):
    return templates.TemplateResponse("test2.html", {"request": request})

@router.get("/test1")
async def test1(request: Request):
    return templates.TemplateResponse("test1.html", {"request": request})


@router.get("/sweets/bakery")
async def bakery(request: Request):
    return templates.TemplateResponse("sweets/bakery.html", {"request": request})

@router.get("/sweets/candy")
async def candy(request: Request):
    return templates.TemplateResponse("sweets/candy.html", {"request": request})

@router.get("/sweets/frozen_dessert")
async def frozen_dessert(request: Request):
    return templates.TemplateResponse("sweets/frozen_dessert.html", {"request": request})

@router.get("/sweets/icecream")
async def icecream(request: Request):
    return templates.TemplateResponse("sweets/icecream.html", {"request": request})

@router.get("/sweets/other_sweet")
async def other_sweet(request: Request):
    return templates.TemplateResponse("sweets/other_sweet.html", {"request": request})

@router.get("/sweets/bakery/choco_cookie")
async def other_sweet(request: Request):
    return templates.TemplateResponse("sweets/bakery/choco_cookie.html", {"request": request})

@router.get("/sweets/bakery/coconut_keks")
async def other_sweet(request: Request):
    return templates.TemplateResponse("sweets/bakery/coconut_keks.html", {"request": request})

@router.get("/sweets/bakery/dzen")
async def other_sweet(request: Request):
    return templates.TemplateResponse("sweets/bakery/dzen.html", {"request": request})

@router.get("/sweets/bakery/evas_cookie")
async def other_sweet(request: Request):
    return templates.TemplateResponse("sweets/bakery/evas_cookie.html", {"request": request})

@router.get("/sweets/bakery/opera")
async def other_sweet(request: Request):
    return templates.TemplateResponse("sweets/bakery/opera.html", {"request": request})

@router.get("/sweets/bakery/shokobomba")
async def other_sweet(request: Request):
    return templates.TemplateResponse("sweets/bakery/shokobomba.html", {"request": request})

@router.get("/sweets/bakery/tartaten")
async def other_sweet(request: Request):
    return templates.TemplateResponse("sweets/bakery/tartaten.html", {"request": request})

@router.get("/sweets/bakery/tiramisu")
async def other_sweet(request: Request):
    return templates.TemplateResponse("sweets/bakery/tiramisu.html", {"request": request})

@router.get("/code")
async def other_sweet(request: Request):
    return templates.TemplateResponse("/code.html", {"request": request})

@router.get("/raw/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}



@router.get("/vegan_raw/example_vegan_raw")
async def vegan(request: Request):
    return templates.TemplateResponse("/vegan_raw/example_vegan_raw.html", {"request": request})