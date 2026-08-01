from app.core.database import SessionLocal, Base, engine
from app.models import MenuItem, GalleryItem, Testimonial


MENU = [
    {
        "name": "Espresso",
        "slug": "espresso",
        "summary": "Double shot, dark and syrupy.",
        "description": (
            "Our house blend, slow-roasted in small batches - notes of dark chocolate, "
            "toasted hazelnut, and a long, clean finish."
        ),
        "category": "Coffee",
        "price": 2.8,
        "is_featured": True,
        "sort_order": 1,
    },
    {
        "name": "Flat White",
        "slug": "flat-white",
        "summary": "Silky micro-foam over a double ristretto.",
        "description": (
            "Velvet-textured steamed milk poured over a double ristretto shot - "
            "smooth, strong, and balanced."
        ),
        "category": "Coffee",
        "price": 3.6,
        "is_featured": True,
        "sort_order": 2,
    },
    {
        "name": "Cortado",
        "slug": "cortado",
        "summary": "Equal parts espresso and warm milk.",
        "description": (
            "A short, strong pour cut with just enough steamed milk to soften the "
            "edge - no foam, no fuss."
        ),
        "category": "Coffee",
        "price": 3.4,
        "is_featured": False,
        "sort_order": 3,
    },
    {
        "name": "Caffè Latte",
        "slug": "caffe-latte",
        "summary": "Espresso, steamed milk, a whisper of foam.",
        "description": (
            "Our most approachable pour - mellow espresso rounded out with steamed "
            "milk, finished with a thin veil of foam."
        ),
        "category": "Coffee",
        "price": 3.7,
        "is_featured": True,
        "sort_order": 4,
    },
    {
        "name": "Affogato",
        "slug": "affogato",
        "summary": "Vanilla gelato drowned in hot espresso.",
        "description": (
            "A scoop of house-made vanilla gelato, served table-side and finished "
            "with a hot shot of espresso poured over the top."
        ),
        "category": "Coffee",
        "price": 4.8,
        "is_featured": False,
        "sort_order": 5,
    },
    {
        "name": "Cold Brew",
        "slug": "cold-brew",
        "summary": "Steeped 18 hours, poured over ice.",
        "description": (
            "Coarse-ground beans steeped cold overnight for a naturally sweet, "
            "low-acid cup, poured long over ice."
        ),
        "category": "Coffee",
        "price": 4.1,
        "is_featured": False,
        "sort_order": 6,
    },
    {
        "name": "Earl Grey",
        "slug": "earl-grey",
        "summary": "Loose-leaf, bergamot-bright.",
        "description": "A classic loose-leaf black tea, steeped to order with a bright citrus lift.",
        "category": "Tea",
        "price": 3.2,
        "is_featured": False,
        "sort_order": 7,
    },
    {
        "name": "Chai Latte",
        "slug": "chai-latte",
        "summary": "House-spiced, steamed with oat milk.",
        "description": (
            "Cardamom, cinnamon, clove, and ginger, brewed strong and steamed with "
            "oat milk by default."
        ),
        "category": "Tea",
        "price": 3.8,
        "is_featured": True,
        "sort_order": 8,
    },
    {
        "name": "Cornetto",
        "slug": "cornetto",
        "summary": "Flaky, butter-laminated, apricot-glazed.",
        "description": (
            "Baked in-house each morning - a classic Italian cornetto, glazed with "
            "apricot and dusted with sugar."
        ),
        "category": "Pastries",
        "price": 3.3,
        "is_featured": True,
        "sort_order": 9,
    },
    {
        "name": "Pistachio Croissant",
        "slug": "pistachio-croissant",
        "summary": "Twice-baked, filled with pistachio cream.",
        "description": (
            "Day-old croissants twice-baked with pistachio frangipane, topped with "
            "crushed pistachio and icing sugar."
        ),
        "category": "Pastries",
        "price": 4.5,
        "is_featured": True,
        "sort_order": 10,
    },
    {
        "name": "Almond Biscotti",
        "slug": "almond-biscotti",
        "summary": "Twice-baked, made for dunking.",
        "description": "Crisp, twice-baked almond biscotti - built to be dunked into a hot espresso.",
        "category": "Pastries",
        "price": 2.4,
        "is_featured": False,
        "sort_order": 11,
    },
    {
        "name": "Prosciutto & Fontina Panino",
        "slug": "prosciutto-fontina-panino",
        "summary": "Pressed ciabatta, melted fontina.",
        "description": (
            "Pressed ciabatta layered with prosciutto, melted fontina, and rocket - "
            "served warm."
        ),
        "category": "Food",
        "price": 7.9,
        "is_featured": False,
        "sort_order": 12,
    },
    {
        "name": "Burrata & Tomato Toast",
        "slug": "burrata-tomato-toast",
        "summary": "Sourdough, burrata, basil oil.",
        "description": (
            "Toasted sourdough topped with creamy burrata, slow-roasted tomatoes, "
            "and a drizzle of basil oil."
        ),
        "category": "Food",
        "price": 8.5,
        "is_featured": True,
        "sort_order": 13,
    },
]

GALLERY = [
    {
        "title": "First Pour",
        "caption": "Espresso in the first light of the morning.",
        "image_url": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1400&q=80",
        "category": "coffee",
        "sort_order": 1,
    },
    {
        "title": "The Bar",
        "caption": "Where every order begins.",
        "image_url": "https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=1400&q=80",
        "category": "interior",
        "sort_order": 2,
    },
    {
        "title": "Roast Notes",
        "caption": "Single-origin, roasted weekly in small batches.",
        "image_url": "https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=1400&q=80",
        "category": "beans",
        "sort_order": 3,
    },
    {
        "title": "Corner Table",
        "caption": "The quiet seat by the window, most mornings.",
        "image_url": "https://images.unsplash.com/photo-1481833761820-0509d3217039?w=1400&q=80",
        "category": "interior",
        "sort_order": 4,
    },
    {
        "title": "Latte Art",
        "caption": "Slow-poured, every single time.",
        "image_url": "https://images.unsplash.com/photo-1541167760496-1628856ab772?w=1400&q=80",
        "category": "coffee",
        "sort_order": 5,
    },
    {
        "title": "From the Oven",
        "caption": "Pastries, baked fresh before opening.",
        "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=1400&q=80",
        "category": "food",
        "sort_order": 6,
    },
]

TESTIMONIALS = [
    {
        "customer_name": "Daniel P.",
        "role": "Regular, weekday mornings",
        "quote": "Best flat white in the neighbourhood, hands down. I've tried. Nothing else comes close.",
        "sort_order": 1,
    },
    {
        "customer_name": "Marisol T.",
        "role": "Local designer",
        "quote": "It's the kind of place that makes a Tuesday feel a little more like a Sunday. Slow, warm, unhurried.",
        "sort_order": 2,
    },
    {
        "customer_name": "Oliver H.",
        "role": "Writer",
        "quote": "I've written half a book at that corner table. The espresso is honestly part of the process now.",
        "sort_order": 3,
    },
]


def seed_database() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        db.query(MenuItem).delete()
        for row in MENU:
            db.add(MenuItem(**row))

        db.query(GalleryItem).delete()
        for row in GALLERY:
            db.add(GalleryItem(**row))

        if db.query(Testimonial).count() == 0:
            for row in TESTIMONIALS:
                db.add(Testimonial(**row))

        db.commit()
    finally:
        db.close()
