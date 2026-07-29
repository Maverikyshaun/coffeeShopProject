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
  return `£${Number(value).toFixed(0)}`;
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

function serviceRow(item, index, full = false) {
  if (full) {
    return `
      <article class="service-row" style="animation-delay:${index * 70}ms">
        <div class="top">
          <h3>${item.name}</h3>
          <span class="price">${money(item.price)}</span>
        </div>
        <p class="summary">${item.summary}</p>
        <p class="description">${item.description}</p>
        <p class="meta">${item.duration}</p>
      </article>`;
  }

  return `
    <article class="service-row" style="animation-delay:${index * 70}ms">
      <div>
        <h3>${item.name}</h3>
        <p class="meta">${item.duration}</p>
      </div>
      <p class="summary">${item.summary}</p>
      <span class="price">${money(item.price)}</span>
    </article>`;
}

async function loadFeaturedServices() {
  const root = document.querySelector("[data-featured-services]");
  if (!root) return;
  try {
    const items = await api("/services/featured");
    root.innerHTML = items.map((item, i) => serviceRow(item, i)).join("");
  } catch {
    root.innerHTML = `<p class="loading">Unable to load services.</p>`;
  }
}

async function loadServices() {
  const root = document.querySelector("[data-services]");
  if (!root) return;
  try {
    const items = await api("/services");
    root.innerHTML = items.map((item, i) => serviceRow(item, i, true)).join("");
  } catch {
    root.innerHTML = `<p class="loading">Unable to load services.</p>`;
  }
}

async function loadLookbook() {
  const root = document.querySelector("[data-lookbook]");
  if (!root) return;
  try {
    const items = await api("/lookbook");
    root.innerHTML = items
      .map(
        (item, i) => `
      <figure class="look-item" style="animation-delay:${i * 80}ms">
        <img src="${item.image_url}" alt="${item.title}" />
        <figcaption>
          <h3>${item.title}</h3>
          <p>${item.caption}</p>
        </figcaption>
      </figure>`
      )
      .join("");
  } catch {
    root.innerHTML = `<p class="loading">Unable to load lookbook.</p>`;
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
        <cite>${item.client_name}${item.role ? ` · ${item.role}` : ""}</cite>
      </article>`
      )
      .join("");
  } catch {
    root.innerHTML = `<p class="loading">Unable to load notes.</p>`;
  }
}

async function loadStudio() {
  const blurb = document.querySelector("[data-studio-blurb]");
  const meta = document.querySelector("[data-studio-meta]");
  if (!blurb && !meta) return;
  try {
    const info = await api("/studio");
    if (blurb) blurb.textContent = info.description;
    if (meta) meta.textContent = `${info.location} · ${info.email}`;
  } catch {
    /* keep static copy */
  }
}

async function initBookingForm() {
  const form = document.querySelector("[data-book-form]");
  const select = document.querySelector("[data-service-select]");
  const message = document.querySelector("[data-book-message]");
  if (!form) return;

  try {
    const services = await api("/services");
    if (select) {
      select.innerHTML =
        `<option value="">Select a service</option>` +
        services.map((s) => `<option value="${s.slug}">${s.name}</option>`).join("");
    }
  } catch {
    /* optional */
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const data = new FormData(form);
    try {
      const booking = await api("/bookings", {
        method: "POST",
        body: JSON.stringify({
          name: data.get("name"),
          email: data.get("email"),
          phone: data.get("phone") || null,
          service_slug: data.get("service_slug") || null,
          occasion: data.get("occasion") || null,
          message: data.get("message"),
        }),
      });
      form.reset();
      if (message) {
        message.hidden = false;
        message.classList.remove("is-error");
        message.textContent = `Inquiry #${booking.id} received. Pearl will be in touch.`;
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
  loadFeaturedServices();
  loadServices();
  loadLookbook();
  loadTestimonials();
  loadStudio();
  initBookingForm();
});
