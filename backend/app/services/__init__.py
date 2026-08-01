from app.core.config import settings
from app.repositories import (
    MenuRepository,
    GalleryRepository,
    TestimonialRepository,
    ReservationRepository,
)
from app.schemas import ReservationCreate, CafeInfoOut


class CafeService:
    def get_info(self) -> CafeInfoOut:
        return CafeInfoOut(
            brand=settings.app_name,
            owner=settings.owner_name,
            tagline=settings.tagline,
            description=(
                f"{settings.owner_name} is a small-batch coffee house and roastery. "
                "Slow-poured espresso, seasonal roasts, and a room built for lingering."
            ),
            location="14 Marchmont Lane, London",
            email="hello@caffebruno.com",
        )


class MenuService:
    def __init__(self, repository: MenuRepository):
        self.repository = repository

    def list_items(self):
        return self.repository.list_all()

    def list_featured(self):
        return self.repository.list_featured()


class GalleryService:
    def __init__(self, repository: GalleryRepository):
        self.repository = repository

    def list_items(self):
        return self.repository.list_all()


class TestimonialService:
    def __init__(self, repository: TestimonialRepository):
        self.repository = repository

    def list_quotes(self):
        return self.repository.list_all()


class ReservationService:
    def __init__(self, repository: ReservationRepository):
        self.repository = repository

    def submit(self, payload: ReservationCreate):
        return self.repository.create(
            name=payload.name,
            email=str(payload.email),
            phone=payload.phone,
            party_size=payload.party_size,
            occasion=payload.occasion,
            message=payload.message,
        )
