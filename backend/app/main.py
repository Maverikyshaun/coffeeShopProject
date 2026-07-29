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


@app.get("/services")
def serve_services_page():
    return FileResponse(frontend_dir / "services.html")


@app.get("/lookbook")
def serve_lookbook_page():
    return FileResponse(frontend_dir / "lookbook.html")


@app.get("/about")
def serve_about_page():
    return FileResponse(frontend_dir / "about.html")


@app.get("/book")
def serve_book_page():
    return FileResponse(frontend_dir / "book.html")


app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")
