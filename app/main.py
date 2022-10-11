from ast import Str
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
import models
from database import engine
from routers import post, user, auth, vote, template
from fastapi.templating import Jinja2Templates
from config import settings
from pydantic import BaseModel
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
import schemas
from sqlalchemy.orm import Session
from database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
# app.include_router(template.router)


templates = Jinja2Templates(directory="templates")


@app.get("/")
def root(request: Request):
    return {"Hello": "Привет, заходите в гости!!!"}








@app.get("/{id}", response_class=JSONResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})

# @app.get("/", response_class=HTMLResponse, response_model=schemas.UserOut)
# def read_item(request: Request, user: str, db: Session = Depends(get_db)):
#     return templates.TemplateResponse(
#         "test.html", {"request": request, "name": user}
#    )

# from starlette.responses import HTMLResponse


# async def app(scope, receive, send):
#     assert scope['type'] == 'http'
#     response = HTMLResponse('<html><body><h1>Всё Пока</h1></body></html>')
#     await response(scope, receive, send)

# @app.get("/sweets/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str ):
    
#     return templates.TemplateResponse("candy.html", {"request": request, "id": id})

# @app.get("/sweets/candy")
# async def candy(request: Request):
#     return templates.TemplateResponse("sweets/candy.html", {"request": request})

# @app.get("/test")
# async def test(request: Request):
#  1   return templates.TemplateResponse("test.html", {"request": request})
