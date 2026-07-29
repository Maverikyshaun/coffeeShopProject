from app.core.config import settings
from app.repositories import (
    ServiceRepository,
    LookbookRepository,
    TestimonialRepository,
    BookingRepository,
)
from app.schemas import BookingCreate, StudioInfoOut


class StudioService:
    def get_info(self) -> StudioInfoOut:
        return StudioInfoOut(
            brand=settings.app_name,
            owner=settings.owner_name,
            tagline=settings.tagline,
            description=(
                f"{settings.owner_name} is a personal shopper and stylist with a "
                "precise, unhurried eye. Wardrobes are edited to feel effortless - "
                "quiet luxury, considered proportion, and pieces that last."
            ),
            location="By appointment - London and remote",
            email="hello@pearlmccaffrey.com",
        )


class PackageService:
    def __init__(self, repository: ServiceRepository):
        self.repository = repository

    def list_packages(self):
        return self.repository.list_all()

    def list_featured(self):
        return self.repository.list_featured()


class LookbookService:
    def __init__(self, repository: LookbookRepository):
        self.repository = repository

    def list_items(self):
        return self.repository.list_all()


class TestimonialService:
    def __init__(self, repository: TestimonialRepository):
        self.repository = repository

    def list_quotes(self):
        return self.repository.list_all()


class BookingService:
    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def submit(self, payload: BookingCreate):
        return self.repository.create(
            name=payload.name,
            email=str(payload.email),
            phone=payload.phone,
            service_slug=payload.service_slug,
            occasion=payload.occasion,
            message=payload.message,
        )
