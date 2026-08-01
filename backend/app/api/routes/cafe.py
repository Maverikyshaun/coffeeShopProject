from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories import (
    MenuRepository,
    GalleryRepository,
    TestimonialRepository,
    ReservationRepository,
)
from app.schemas import (
    MenuItemOut,
    GalleryItemOut,
    TestimonialOut,
    ReservationCreate,
    ReservationOut,
    CafeInfoOut,
)
from app.services import (
    CafeService,
    MenuService,
    GalleryService,
    TestimonialService,
    ReservationService,
)

router = APIRouter()


@router.get("/cafe", response_model=CafeInfoOut)
def get_cafe():
    return CafeService().get_info()


@router.get("/menu", response_model=list[MenuItemOut])
def get_menu(db: Session = Depends(get_db)):
    return MenuService(MenuRepository(db)).list_items()


@router.get("/menu/featured", response_model=list[MenuItemOut])
def get_featured_menu(db: Session = Depends(get_db)):
    return MenuService(MenuRepository(db)).list_featured()


@router.get("/gallery", response_model=list[GalleryItemOut])
def get_gallery(db: Session = Depends(get_db)):
    return GalleryService(GalleryRepository(db)).list_items()


@router.get("/testimonials", response_model=list[TestimonialOut])
def get_testimonials(db: Session = Depends(get_db)):
    return TestimonialService(TestimonialRepository(db)).list_quotes()


@router.post("/reservations", response_model=ReservationOut)
def create_reservation(payload: ReservationCreate, db: Session = Depends(get_db)):
    return ReservationService(ReservationRepository(db)).submit(payload)
