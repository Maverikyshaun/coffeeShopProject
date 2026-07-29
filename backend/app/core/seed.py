from app.core.database import SessionLocal, Base, engine
from app.models import ServicePackage, LookbookItem, Testimonial


PACKAGES = [
    {
        "name": "Wardrobe Edit",
        "slug": "wardrobe-edit",
        "summary": "A precise clear-out and rebuild of what you already own.",
        "description": (
            "Together we edit your closet piece by piece - keep, alter, release. "
            "You leave with a refined base and a short list of considered additions."
        ),
        "duration": "3 hours",
        "price": 420.0,
        "is_featured": True,
        "sort_order": 1,
    },
    {
        "name": "Personal Shopping Day",
        "slug": "personal-shopping",
        "summary": "A full day of guided shopping with a quiet, exacting eye.",
        "description": (
            "From fittings to final edits, Pearl leads a tailored shopping day "
            "across selected houses and ateliers - never rushed, never excess."
        ),
        "duration": "Full day",
        "price": 780.0,
        "is_featured": True,
        "sort_order": 2,
    },
    {
        "name": "Occasion Styling",
        "slug": "occasion-styling",
        "summary": "One look, fully resolved - events, travel, or first impressions.",
        "description": (
            "A focused session for a single moment that matters. Silhouette, "
            "fabric, and finish are chosen with restraint and polish."
        ),
        "duration": "2 hours",
        "price": 340.0,
        "is_featured": True,
        "sort_order": 3,
    },
    {
        "name": "Seasonal Capsule",
        "slug": "seasonal-capsule",
        "summary": "A slim seasonal wardrobe planned months ahead.",
        "description": (
            "Twelve to eighteen pieces that work in concert - proportion, palette, "
            "and longevity over trend."
        ),
        "duration": "Ongoing",
        "price": 1250.0,
        "is_featured": False,
        "sort_order": 4,
    },
    {
        "name": "Remote Consult",
        "slug": "remote-consult",
        "summary": "Video styling for clients anywhere.",
        "description": (
            "A refined remote session covering wardrobe direction, sourcing notes, "
            "and a written edit plan."
        ),
        "duration": "90 minutes",
        "price": 220.0,
        "is_featured": False,
        "sort_order": 5,
    },
]

LOOKBOOK = [
    {
        "title": "Pearl",
        "caption": "The face of the atelier - quiet, exact, considered.",
        "image_url": "/static/res/pearl-portrait.jpg",
        "category": "portrait",
        "sort_order": 1,
    },
    {
        "title": "Atelier Edit",
        "caption": "Thin silhouette. Soft structure. Nothing excess.",
        "image_url": "/static/res/pearl-lookbook.jpg",
        "category": "day",
        "sort_order": 2,
    },
    {
        "title": "Studio Line",
        "caption": "Black, pared back, and precisely proportioned.",
        "image_url": "/static/res/pearl-studio.jpg",
        "category": "studio",
        "sort_order": 3,
    },
    {
        "title": "In Person",
        "caption": "Pearl Mccaffrey - personal shopper.",
        "image_url": "/static/res/IMG_5351.jpeg",
        "category": "portrait",
        "sort_order": 4,
    },
    {
        "title": "City Tailoring",
        "caption": "Sharp through the waist. Nothing loud.",
        "image_url": "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1400&q=80",
        "category": "tailoring",
        "sort_order": 5,
    },
    {
        "title": "Travel Edit",
        "caption": "Four pieces. Infinite calm.",
        "image_url": "https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=1400&q=80",
        "category": "travel",
        "sort_order": 6,
    },
]

TESTIMONIALS = [
    {
        "client_name": "Amelia R.",
        "role": "Creative director",
        "quote": "Pearl edits until everything feels inevitable. My wardrobe has never been this quiet - or this exact.",
        "sort_order": 1,
    },
    {
        "client_name": "Helena V.",
        "role": "Founder",
        "quote": "No noise. No piles of almost. Just pieces that sit perfectly and earn their place.",
        "sort_order": 2,
    },
    {
        "client_name": "Sofia K.",
        "role": "Architect",
        "quote": "She understands proportion the way I understand space. Subtle, rigorous, beautiful.",
        "sort_order": 3,
    },
]


def seed_database() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(ServicePackage).count() == 0:
            for row in PACKAGES:
                db.add(ServicePackage(**row))

        db.query(LookbookItem).delete()
        for row in LOOKBOOK:
            db.add(LookbookItem(**row))

        if db.query(Testimonial).count() == 0:
            for row in TESTIMONIALS:
                db.add(Testimonial(**row))

        db.commit()
    finally:
        db.close()
