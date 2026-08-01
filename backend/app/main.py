from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import api_router
from app.core.config import settings
from app.core.seed import seed_database

seed_database()

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

frontend_dir = Path(settings.frontend_dir)


@app.get("/")
def serve_home():
    return FileResponse(frontend_dir / "index.html")


@app.get("/menu")
def serve_menu_page():
    return FileResponse(frontend_dir / "menu.html")


@app.get("/gallery")
def serve_gallery_page():
    return FileResponse(frontend_dir / "gallery.html")


@app.get("/about")
def serve_about_page():
    return FileResponse(frontend_dir / "about.html")


@app.get("/visit")
def serve_visit_page():
    return FileResponse(frontend_dir / "visit.html")


app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")
