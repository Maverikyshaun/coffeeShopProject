const API = "/api";

async function api(path, options = {}) {
  const res = await fetch(`${API}${path}`, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    const detail = err.detail;
    throw new Error(typeof detail === "string" ? detail : "Request failed");
  }
  return res.json();
}

function money(value) {
  return `£${Number(value).toFixed(2)}`;
}

function initHeader() {
  const header = document.querySelector("[data-header]");
  const toggle = document.querySelector("[data-nav-toggle]");
  const nav = document.querySelector("[data-nav]");

  const onScroll = () => header?.classList.toggle("is-scrolled", window.scrollY > 12);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
  toggle?.addEventListener("click", () => nav?.classList.toggle("is-open"));
}

function menuRow(item, index, full = false) {
  if (full) {
    return `
      <article class="menu-row" style="animation-delay:${index * 70}ms">
        <div class="top">
          <h3>${item.name}</h3>
          <span class="price">${money(item.price)}</span>
        </div>
        <p class="summary">${item.summary}</p>
        <p class="description">${item.description}</p>
      </article>`;
  }

  return `
    <article class="menu-row" style="animation-delay:${index * 70}ms">
      <div>
        <h3>${item.name}</h3>
        <p class="meta">${item.category}</p>
      </div>
      <p class="summary">${item.summary}</p>
      <span class="price">${money(item.price)}</span>
    </article>`;
}

async function loadFeaturedMenu() {
  const root = document.querySelector("[data-featured-menu]");
  if (!root) return;
  try {
    const items = await api("/menu/featured");
    root.innerHTML = items.map((item, i) => menuRow(item, i)).join("");
  } catch {
    root.innerHTML = `<p class="loading">Unable to load the menu.</p>`;
  }
}

async function loadMenu() {
  const root = document.querySelector("[data-menu]");
  if (!root) return;
  try {
    const items = await api("/menu");
    const byCategory = new Map();
    for (const item of items) {
      if (!byCategory.has(item.category)) byCategory.set(item.category, []);
      byCategory.get(item.category).push(item);
    }
    let i = 0;
    root.innerHTML = Array.from(byCategory.entries())
      .map(
        ([category, rows]) => `
          <h3 class="menu-category">${category}</h3>
          <div class="menu-list menu-list--full">
            ${rows.map((row) => menuRow(row, i++, true)).join("")}
          </div>`
      )
      .join("");
  } catch {
    root.innerHTML = `<p class="loading">Unable to load the menu.</p>`;
  }
}

async function loadGallery() {
  const root = document.querySelector("[data-gallery]");
  if (!root) return;
  try {
    const items = await api("/gallery");
    root.innerHTML = items
      .map(
        (item, i) => `
      <figure class="gallery-item" style="animation-delay:${i * 80}ms">
        <img src="${item.image_url}" alt="${item.title}" />
        <figcaption>
          <h3>${item.title}</h3>
          <p>${item.caption}</p>
        </figcaption>
      </figure>`
      )
      .join("");
  } catch {
    root.innerHTML = `<p class="loading">Unable to load the gallery.</p>`;
  }
}

async function loadTestimonials() {
  const root = document.querySelector("[data-testimonials]");
  if (!root) return;
  try {
    const items = await api("/testimonials");
    root.innerHTML = items
      .map(
        (item, i) => `
      <article class="quote-item" style="animation-delay:${i * 90}ms">
        <blockquote>${item.quote}</blockquote>
        <cite>${item.customer_name}${item.role ? ` · ${item.role}` : ""}</cite>
      </article>`
      )
      .join("");
  } catch {
    root.innerHTML = `<p class="loading">Unable to load reviews.</p>`;
  }
}

async function loadCafe() {
  const blurb = document.querySelector("[data-cafe-blurb]");
  const meta = document.querySelector("[data-cafe-meta]");
  if (!blurb && !meta) return;
  try {
    const info = await api("/cafe");
    if (blurb) blurb.textContent = info.description;
    if (meta) meta.textContent = `${info.location} · ${info.email}`;
  } catch {
    /* keep static copy */
  }
}

async function initVisitForm() {
  const form = document.querySelector("[data-visit-form]");
  const message = document.querySelector("[data-visit-message]");
  if (!form) return;

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const data = new FormData(form);
    try {
      const reservation = await api("/reservations", {
        method: "POST",
        body: JSON.stringify({
          name: data.get("name"),
          email: data.get("email"),
          phone: data.get("phone") || null,
          party_size: data.get("party_size") ? Number(data.get("party_size")) : null,
          occasion: data.get("occasion") || null,
          message: data.get("message"),
        }),
      });
      form.reset();
      if (message) {
        message.hidden = false;
        message.classList.remove("is-error");
        message.textContent = `Thanks, ${reservation.name.split(" ")[0]} - inquiry #${reservation.id} received. We'll be in touch shortly.`;
      }
    } catch (error) {
      if (message) {
        message.hidden = false;
        message.classList.add("is-error");
        message.textContent = error.message;
      }
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initHeader();
  loadFeaturedMenu();
  loadMenu();
  loadGallery();
  loadTestimonials();
  loadCafe();
  initVisitForm();
});
