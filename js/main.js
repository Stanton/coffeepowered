(function () {
    const quoteText = document.getElementById("homepage-quote-text");
    const quoteAttribution = document.getElementById("homepage-quote-attribution");
    const homepageQuotes = [
        {
            text: "For everything that is really great and inspiring is created by the individual who can labour in freedom",
            attribution: "Albert Einstein",
        },
        {
            text: "Complexity is your enemy. Any fool can make something complicated. It is hard to keep things simple.",
            attribution: "Richard Branson",
        },
    ];

    if (quoteText && quoteAttribution) {
        const selected = homepageQuotes[Math.floor(Math.random() * homepageQuotes.length)];
        quoteText.textContent = `“${selected.text}”`;
        quoteAttribution.textContent = selected.attribution;
    }

    const navLinks = Array.from(document.querySelectorAll(".top-nav-links a[href^='#']"));
    const nav = document.querySelector(".top-nav-links");
    const brandLink = document.querySelector(".brand[href='#top']");
    if (!navLinks.length) {
        return;
    }

    const sections = navLinks
        .map((link) => {
            const id = link.getAttribute("href");
            const el = id ? document.querySelector(id) : null;
            return el ? { id, el, link } : null;
        })
        .filter(Boolean);

    if (!sections.length) {
        return;
    }

    let clickLockedId = null;
    let hasUserScrolled = false;

    const clearActive = () => {
        for (const item of sections) {
            item.link.classList.remove("is-active");
            item.link.removeAttribute("aria-current");
        }
        if (nav) {
            nav.classList.remove("has-active");
        }
    };

    const positionPill = (link) => {
        if (!nav || !link) {
            return;
        }
        const navRect = nav.getBoundingClientRect();
        const linkRect = link.getBoundingClientRect();
        nav.style.setProperty("--pill-x", `${linkRect.left - navRect.left}px`);
        nav.style.setProperty("--pill-y", `${linkRect.top - navRect.top}px`);
        nav.style.setProperty("--pill-w", `${linkRect.width}px`);
        nav.style.setProperty("--pill-h", `${linkRect.height}px`);
        nav.classList.add("has-active");
    };

    const setActive = (id) => {
        let activeLink = null;
        for (const item of sections) {
            const active = item.id === id;
            item.link.classList.toggle("is-active", active);
            if (active) {
                item.link.setAttribute("aria-current", "page");
                activeLink = item.link;
            } else {
                item.link.removeAttribute("aria-current");
            }
        }
        positionPill(activeLink);
    };

    for (const item of sections) {
        item.link.addEventListener("click", () => {
            clickLockedId = item.id;
            setActive(item.id);
        });
    }

    const observer = new IntersectionObserver(
        (entries) => {
            if (clickLockedId || !hasUserScrolled) {
                return;
            }
            let topMost = null;
            for (const entry of entries) {
                if (!entry.isIntersecting) {
                    continue;
                }
                if (!topMost || entry.boundingClientRect.top < topMost.boundingClientRect.top) {
                    topMost = entry;
                }
            }
            if (!topMost) {
                return;
            }
            const item = sections.find((s) => s.el === topMost.target);
            if (item) {
                setActive(item.id);
            }
        },
        {
            root: null,
            rootMargin: "-20% 0px -62% 0px",
            threshold: 0,
        }
    );

    for (const item of sections) {
        observer.observe(item.el);
    }

    clearActive();

    const releaseClickLock = () => {
        hasUserScrolled = true;
        if (!clickLockedId) {
            return;
        }
        clickLockedId = null;
    };

    window.addEventListener("wheel", releaseClickLock, { passive: true });
    window.addEventListener("touchmove", releaseClickLock, { passive: true });
    window.addEventListener("keydown", (event) => {
        if (
            event.key === "ArrowDown" ||
            event.key === "ArrowUp" ||
            event.key === "PageDown" ||
            event.key === "PageUp" ||
            event.key === "Home" ||
            event.key === "End" ||
            event.key === " " ||
            event.key === "Spacebar"
        ) {
            releaseClickLock();
        }
    });

    if (brandLink) {
        brandLink.addEventListener("click", (event) => {
            event.preventDefault();
            clickLockedId = "__top__";
            clearActive();
            if (window.location.hash) {
                history.replaceState(null, "", window.location.pathname + window.location.search);
            }
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    window.addEventListener("resize", () => {
        const active = sections.find((s) => s.link.classList.contains("is-active"));
        if (active) {
            positionPill(active.link);
        }
    });
})();
