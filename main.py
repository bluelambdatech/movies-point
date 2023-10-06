from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import smtplib

from utils.azure_sql_database import *
from utils.credentials import *


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login_response(request: Request,
                            username: str = Form(...),
                            password: str = Form(...),
                            ):

    try:
        read_from_table(username,password)

    except:
        return "User Does Not Exist"

    return

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



@app.get("/forgot_password", response_class=HTMLResponse)
def forgot_password(request:Request):
    return templates.TemplateResponse("forgot_password.html", {"request": request})


@app.post("/forgot_password")
async def password(request: Request, Email: str = Form(...),
                   Username: str = Form(...)):
    """
    Info from User for authentication: username, email
    Query the database with these two info - send a reset password link to the email provided
        - look for how to send email with python
    :param request:
    :param email:
    :param username:
    :return:
    """
    print(Username, Email)

    sender_email = "n4naynay@gmail.com"
    receiver_email = Email
    subject = (" SUBJECT: Forgot Password to Movies Point")
    message = (
        " In response to your forgot password request, kindly click on this link for a password reset. Do ignore this email if you are not the requestor")
    text = f"subject : {subject} \n\n {message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, text)

    print("Email has been sent to " + receiver_email)

    # return read_from_table(Username , Email)
    # return "If your email is registered with us, a reset password email will be sent to you"




