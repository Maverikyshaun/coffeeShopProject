from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories import (
    ServiceRepository,
    LookbookRepository,
    TestimonialRepository,
    BookingRepository,
)
from app.schemas import (
    ServicePackageOut,
    LookbookItemOut,
    TestimonialOut,
    BookingCreate,
    BookingOut,
    StudioInfoOut,
)
from app.services import (
    StudioService,
    PackageService,
    LookbookService,
    TestimonialService,
    BookingService,
)

router = APIRouter()


@router.get("/studio", response_model=StudioInfoOut)
def get_studio():
    return StudioService().get_info()


@router.get("/services", response_model=list[ServicePackageOut])
def get_services(db: Session = Depends(get_db)):
    return PackageService(ServiceRepository(db)).list_packages()


@router.get("/services/featured", response_model=list[ServicePackageOut])
def get_featured_services(db: Session = Depends(get_db)):
    return PackageService(ServiceRepository(db)).list_featured()


@router.get("/lookbook", response_model=list[LookbookItemOut])
def get_lookbook(db: Session = Depends(get_db)):
    return LookbookService(LookbookRepository(db)).list_items()


@router.get("/testimonials", response_model=list[TestimonialOut])
def get_testimonials(db: Session = Depends(get_db)):
    return TestimonialService(TestimonialRepository(db)).list_quotes()


@router.post("/bookings", response_model=BookingOut)
def create_booking(payload: BookingCreate, db: Session = Depends(get_db)):
    return BookingService(BookingRepository(db)).submit(payload)
