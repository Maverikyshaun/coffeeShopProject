from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class MenuItemOut(BaseModel):
    id: int
    name: str
    slug: str
    summary: str
    description: str
    category: str
    price: float
    is_featured: bool
    sort_order: int

    model_config = {"from_attributes": True}


class GalleryItemOut(BaseModel):
    id: int
    title: str
    caption: str
    image_url: str
    category: str
    sort_order: int

    model_config = {"from_attributes": True}


class TestimonialOut(BaseModel):
    id: int
    customer_name: str
    quote: str
    role: Optional[str] = None
    sort_order: int

    model_config = {"from_attributes": True}


class ReservationCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    phone: Optional[str] = Field(default=None, max_length=40)
    party_size: Optional[int] = Field(default=None, ge=1, le=100)
    occasion: Optional[str] = Field(default=None, max_length=200)
    message: str = Field(min_length=5, max_length=3000)


class ReservationOut(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    party_size: Optional[int] = None
    occasion: Optional[str] = None
    message: str
    created_at: datetime

    model_config = {"from_attributes": True}


class CafeInfoOut(BaseModel):
    brand: str
    owner: str
    tagline: str
    description: str
    location: str
    email: str
