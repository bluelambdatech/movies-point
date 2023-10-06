from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles

from utils.azure_sql_database import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/imgs", StaticFiles(directory="imgs"), name='img_avatar2.jpg')


@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register")
async def register_response(request: Request,
                            lastname: str = Form(...),
                            firstname: str = Form(...),
                            email: str = Form(...),
                            username: str = Form(...),
                            dob = Form(...),
                            gender: str = Form(...),
                            psw: str = Form(...), psw_repeat: str = Form(...)
                            ):

    try:
        insert_into_table(lastname, firstname, email, username, dob, gender)

    except:
        return "User Already Exist"

    return


@app.get("/forgot_password", response_class=HTMLResponse)
def forgot_password(request:Request):
    return templates.TemplateResponse("forgot_password.html", {"request": request})


@app.post("/forgot_password")
async def password(request: Request, email: str = Form(...),
                   username: str = Form(...)):
    print(username, email)

    return read_from_table(username)
    #return "If your email is registered with us, a reset password email will be sent to you"


@app.get("/contact_us", response_class=HTMLResponse)
async def contact_us(request: Request):

    return templates.TemplateResponse("contact_us.html", {"request": request})


@app.post("/contact_us")
async def contact_us(request: Request, firstname: str = Form(...),
                     lastname: str = Form(...),
                     country: str = Form(...),
                     subject: str = Form(...)):
    print(firstname, lastname, country, subject)

    #return read_from_table(username)
