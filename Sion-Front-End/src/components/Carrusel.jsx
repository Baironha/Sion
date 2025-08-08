import { useEffect, useRef, useState } from "react";
import "../style/Carrusel.css";

// IMPORTS LOCALES (desde src/Img)
import CategoriaAccesorios from "../Img/CategoriaAccesorios.jpg";
import CategoriaTecnologia from "../Img/CategoriaTecnologia.jpg";
import CategoriaElectrodomesticos from "../Img/categoriaElectrodomesticos.jpg";
import CategoriaHerramientasJardin from "../Img/CatHerramientas_Jardineria.png";

// Las dos primeras usan imports locales; las demás van desde /public/media
const demoItems = [
  { type: "image", src: CategoriaAccesorios, alt: "Accesorios" },
  { type: "image", src: CategoriaTecnologia, alt: "Tecnología" },
  { type: "video", src: CategoriaElectrodomesticos , poster: "/media/poster1.jpg", alt: "Video 1" },
  { type: "image", src: CategoriaElectrodomesticos, alt: "Promo 3" },
  { type: "image", src: CategoriaHerramientasJardin , alt: "Promo 4" },
  { type: "video", src: "/media/spot2.mp4", poster: "/media/poster2.jpg", alt: "Video 2" },
  { type: "image", src: "/media/slide5.jpg", alt: "Promo 5" },
];

function Carrusel({ items = demoItems, interval = 2000 }) {
  const [index, setIndex] = useState(0);
  const [paused, setPaused] = useState(false);
  const trackRef = useRef(null);
  const videoRefs = useRef([]);

  // Auto-advance
  useEffect(() => {
    if (paused || items.length <= 1) return;
    const id = setInterval(() => setIndex((i) => (i + 1) % items.length), interval);
    return () => clearInterval(id);
  }, [paused, items.length, interval]);

  // Play/pause videos según slide activo (sin ESLint no-unused-vars)
  useEffect(() => {
    videoRefs.current.forEach((vid, i) => {
      if (!vid) return;

      if (i === index) {
        vid.currentTime = 0;
        const p = vid.play();
        if (p && typeof p.catch === "function") p.catch(() => {});
      } else {
        try {
          vid.pause();
        } catch (e) {
          void e; // evita warning de "e no usado" en ESLint
        }
      }
    });
  }, [index]);

  const goTo = (i) => setIndex((i + items.length) % items.length);
  const next = () => goTo(index + 1);
  const prev = () => goTo(index - 1);

  // Touch swipe (móvil)
  const startX = useRef(0);
  const deltaX = useRef(0);

  const onTouchStart = (e) => {
    startX.current = e.touches[0].clientX;
    deltaX.current = 0;
    setPaused(true);
  };
  const onTouchMove = (e) => {
    deltaX.current = e.touches[0].clientX - startX.current;
  };
  const onTouchEnd = () => {
    if (deltaX.current > 50) prev();
    else if (deltaX.current < -50) next();
    setPaused(false);
  };

  return (
    <div
      className="mc-wrapper"
      onMouseEnter={() => setPaused(true)}
      onMouseLeave={() => setPaused(false)}
    >
      <button type="button" className="mc-arrow mc-left" onClick={prev} aria-label="Anterior">
        ‹
      </button>

      <div
        className="mc-viewport"
        onTouchStart={onTouchStart}
        onTouchMove={onTouchMove}
        onTouchEnd={onTouchEnd}
      >
        <div
          className="mc-track"
          ref={trackRef}
          style={{ transform: `translateX(-${index * 100}%)` }}
        >
          {items.map((item, i) => (
            <div className="mc-slide" key={i}>
              {item.type === "image" ? (
                <img src={item.src} alt={item.alt || `slide-${i}`} loading="lazy" />
              ) : (
                <video
                  ref={(el) => (videoRefs.current[i] = el)}
                  src={item.src}
                  muted
                  playsInline
                  preload="metadata"
                  poster={item.poster || undefined}
                />
              )}
              {item.caption && <div className="mc-caption">{item.caption}</div>}
            </div>
          ))}
        </div>
      </div>

      <button type="button" className="mc-arrow mc-right" onClick={next} aria-label="Siguiente">
        ›
      </button>

      <div className="mc-dots">
        {items.map((_, i) => (
          <button
            type="button"
            key={i}
            className={`mc-dot ${i === index ? "active" : ""}`}
            onClick={() => goTo(i)}
            aria-label={`Ir al slide ${i + 1}`}
          />
        ))}
      </div>
    </div>
  );
}

export default Carrusel;
