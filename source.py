from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlite3

app = FastAPI()

templates = Jinja2Templates(directory="Templates")

# ---------- HOME ----------
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("sindex.html", {"request": request})

# ---------- ADD FORM ----------
@app.get("/add", response_class=HTMLResponse)
def add(request: Request):
    return templates.TemplateResponse("sadd.html", {"request": request})

# ---------- SAVE DETAILS ----------
@app.post("/savedetails", response_class=HTMLResponse)
def save_details(
    request: Request,
    name: str = Form(),
    email: str = Form(),
    address: str = Form(),
    number: str = Form(),
    college_name: str = Form(),
    city: str = Form(),
    state: str = Form()
):
    msg = ""
    try:
        with sqlite3.connect("senroll.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO ens (name,email,address,number,college_name,city,state) VALUES (?,?,?,?,?,?,?)",
                (name, email, address, number, college_name, city, state)
            )
            con.commit()
            msg = "Your Details have been Successfully Submitted"
    except Exception:
        msg = "Sorry! Please fill all the details in the form"

    return templates.TemplateResponse("ssuccess.html", {"request": request, "msg": msg})

# ---------- DISPLAY TABLE ----------
@app.get("/view", response_class=HTMLResponse)
def view(request: Request):
    con = sqlite3.connect("senroll.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM ens")
    rows = cur.fetchall()
    return templates.TemplateResponse("sview.html", {"request": request, "rows": rows})

# ---------- JSON DATA API ----------
@app.get("/data")
def data():
    con = sqlite3.connect("senroll.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM ens")
    rows = cur.fetchall()
    return JSONResponse({"students": [dict(row) for row in rows]})
