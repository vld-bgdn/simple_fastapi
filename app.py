from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.routes import api_router

app = FastAPI(title="Movies App")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(api_router)


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Home Page"}
    )


@app.get("/about/", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {
            "request": request,
            "title": "About",
            "developer": "Vladimir Bogdanov",
            "developer_info": "The newbie python developer with experience in Ansible",
            "site_info": "This site is a simple FastAPI application showcasing both web pages and API endpoints.",
        },
    )
