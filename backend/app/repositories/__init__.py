from sqlalchemy.orm import Session

from app.models import MenuItem, GalleryItem, Testimonial, ReservationInquiry


class MenuRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_all(self) -> list[MenuItem]:
        return (
            self.db.query(MenuItem)
            .order_by(MenuItem.category.asc(), MenuItem.sort_order.asc(), MenuItem.name.asc())
            .all()
        )

    def list_featured(self) -> list[MenuItem]:
        return (
            self.db.query(MenuItem)
            .filter(MenuItem.is_featured.is_(True))
            .order_by(MenuItem.sort_order.asc())
            .all()
        )

    def get_by_slug(self, slug: str) -> MenuItem | None:
        return self.db.query(MenuItem).filter(MenuItem.slug == slug).first()


class GalleryRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_all(self) -> list[GalleryItem]:
        return (
            self.db.query(GalleryItem)
            .order_by(GalleryItem.sort_order.asc(), GalleryItem.id.asc())
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


class ReservationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, **kwargs) -> ReservationInquiry:
        row = ReservationInquiry(**kwargs)
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)
        return row
