from sqlalchemy.orm import Session

from app.models import ServicePackage, LookbookItem, Testimonial, BookingInquiry


class ServiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_all(self) -> list[ServicePackage]:
        return (
            self.db.query(ServicePackage)
            .order_by(ServicePackage.sort_order.asc(), ServicePackage.name.asc())
            .all()
        )

    def list_featured(self) -> list[ServicePackage]:
        return (
            self.db.query(ServicePackage)
            .filter(ServicePackage.is_featured.is_(True))
            .order_by(ServicePackage.sort_order.asc())
            .all()
        )

    def get_by_slug(self, slug: str) -> ServicePackage | None:
        return self.db.query(ServicePackage).filter(ServicePackage.slug == slug).first()


class LookbookRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_all(self) -> list[LookbookItem]:
        return (
            self.db.query(LookbookItem)
            .order_by(LookbookItem.sort_order.asc(), LookbookItem.id.asc())
            .all()
        )


class TestimonialRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_all(self) -> list[Testimonial]:
        return (
            self.db.query(Testimonial)
            .order_by(Testimonial.sort_order.asc(), Testimonial.id.asc())
            .all()
        )


class BookingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, **kwargs) -> BookingInquiry:
        row = BookingInquiry(**kwargs)
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)
        return row
