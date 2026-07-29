from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ServicePackageOut(BaseModel):
    id: int
    name: str
    slug: str
    summary: str
    description: str
    duration: str
    price: float
    is_featured: bool
    sort_order: int

    model_config = {"from_attributes": True}


class LookbookItemOut(BaseModel):
    id: int
    title: str
    caption: str
    image_url: str
    category: str
    sort_order: int

    model_config = {"from_attributes": True}


class TestimonialOut(BaseModel):
    id: int
    client_name: str
    quote: str
    role: Optional[str] = None
    sort_order: int

    model_config = {"from_attributes": True}


class BookingCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    phone: Optional[str] = Field(default=None, max_length=40)
    service_slug: Optional[str] = Field(default=None, max_length=120)
    occasion: Optional[str] = Field(default=None, max_length=200)
    message: str = Field(min_length=5, max_length=3000)


class BookingOut(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    service_slug: Optional[str] = None
    occasion: Optional[str] = None
    message: str
    created_at: datetime

    model_config = {"from_attributes": True}


class StudioInfoOut(BaseModel):
    brand: str
    owner: str
    tagline: str
    description: str
    location: str
    email: str
