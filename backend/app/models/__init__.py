from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, Text, Boolean, DateTime

from app.core.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    slug = Column(String(120), unique=True, nullable=False)
    summary = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(80), nullable=False)
    price = Column(Float, nullable=False)
    is_featured = Column(Boolean, default=False)
    sort_order = Column(Integer, default=0)


class GalleryItem(Base):
    __tablename__ = "gallery_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False)
    caption = Column(String(255), nullable=False, default="")
    image_url = Column(String(500), nullable=False)
    category = Column(String(80), nullable=False, default="cafe")
    sort_order = Column(Integer, default=0)


class Testimonial(Base):
    __tablename__ = "testimonials"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(120), nullable=False)
    quote = Column(Text, nullable=False)
    role = Column(String(120), nullable=True)
    sort_order = Column(Integer, default=0)


class ReservationInquiry(Base):
    __tablename__ = "reservation_inquiries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    email = Column(String(200), nullable=False)
    phone = Column(String(40), nullable=True)
    party_size = Column(Integer, nullable=True)
    occasion = Column(String(200), nullable=True)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
