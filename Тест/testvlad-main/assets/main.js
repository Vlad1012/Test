(() => {
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const shutter = document.querySelector('.shutter');

  /* ---------- shutter: lift on arrival, drop on leave ---------- */
  function ready() { root.classList.add('ready'); }
  function lift() {
    if (!shutter || !root.classList.contains('arriving')) { ready(); return; }
    shutter.classList.add('cover');
    requestAnimationFrame(() => {
      root.classList.remove('arriving');
      shutter.classList.remove('cover');
      shutter.classList.add('up');
      setTimeout(ready, 260);
      setTimeout(() => shutter.classList.remove('up'), 900);
    });
  }
  const fontsReady = document.fonts ? Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, 600))]) : Promise.resolve();
  fontsReady.then(lift);

  document.addEventListener('click', e => {
    const a = e.target.closest('a');
    if (!a || reduce || !shutter) return;
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    if (a.target && a.target !== '_self') return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin) return;
    if (url.pathname === location.pathname && url.search === location.search) return; // same page / anchors
    if (!/(\.html|\/)$/.test(url.pathname)) return;
    e.preventDefault();
    document.body.classList.remove('menu-open');
    shutter.classList.remove('up', 'cover');
    shutter.classList.add('down');
    let gone = false;
    const go = () => { if (gone) return; gone = true; try { sessionStorage.setItem('vh-shutter', '1'); } catch (_) {} location.href = url.href; };
    shutter.addEventListener('transitionend', go, { once: true });
    setTimeout(go, 750);
  });
  addEventListener('pageshow', e => { if (e.persisted && shutter) { shutter.classList.remove('down'); ready(); } });
  try { sessionStorage.removeItem('vh-shutter'); } catch (_) {}

  /* ---------- header / menu / call bar ---------- */
  const hdr = document.querySelector('.hdr');
  const mbar = document.querySelector('.mbar');
  const onScroll = () => {
    const y = scrollY;
    hdr && hdr.classList.toggle('scrolled', y > 8);
    mbar && mbar.classList.toggle('show', y > 420);
  };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  const burger = document.querySelector('.burger');
  burger && burger.addEventListener('click', () => {
    const open = document.body.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', open);
    burger.setAttribute('aria-label', open ? 'Закрити меню' : 'Відкрити меню');
  });
  addEventListener('keydown', e => { if (e.key === 'Escape' && document.body.classList.contains('menu-open')) burger.click(); });

  /* ---------- services list: photo follows cursor ---------- */
  const peek = document.querySelector('.peek');
  if (peek && matchMedia('(hover:hover)').matches) {
    const img = peek.querySelector('img');
    let x = 0, y = 0, tx = 0, ty = 0, raf;
    const loop = () => { x += (tx - x) * .18; y += (ty - y) * .18; peek.style.left = x + 'px'; peek.style.top = y + 'px'; raf = requestAnimationFrame(loop); };
    document.querySelectorAll('.svc a[data-img]').forEach(a => {
      a.addEventListener('mouseenter', e => {
        img.src = a.dataset.img; tx = x = e.clientX + 150; ty = y = e.clientY;
        peek.classList.add('on'); cancelAnimationFrame(raf); loop();
      });
      a.addEventListener('mousemove', e => { tx = e.clientX + 150; ty = e.clientY; });
      a.addEventListener('mouseleave', () => { peek.classList.remove('on'); setTimeout(() => cancelAnimationFrame(raf), 300); });
    });
  }

  /* ---------- photo strip arrows ---------- */
  document.querySelectorAll('[data-strip]').forEach(nav => {
    const strip = document.getElementById(nav.dataset.strip);
    nav.querySelectorAll('button').forEach(b => b.addEventListener('click', () => {
      const step = strip.querySelector('figure').offsetWidth + 16;
      strip.scrollBy({ left: (b.dataset.dir === 'next' ? 1 : -1) * step * 2, behavior: reduce ? 'auto' : 'smooth' });
    }));
  });

  /* ---------- works: filter + lightbox ---------- */
  const works = [...document.querySelectorAll('.work')];
  const filters = document.querySelectorAll('.filters button');
  filters.forEach(b => b.addEventListener('click', () => {
    filters.forEach(x => x.setAttribute('aria-pressed', x === b));
    const f = b.dataset.f;
    works.forEach(w => w.classList.toggle('hide', f !== 'all' && w.dataset.cat !== f));
  }));
  const lb = document.querySelector('.lb');
  if (lb && works.length) {
    const lbImg = lb.querySelector('img'), lbCap = lb.querySelector('.lb-bar p');
    let i = 0, last;
    const visible = () => works.filter(w => !w.classList.contains('hide'));
    const show = n => {
      const v = visible(); i = (n + v.length) % v.length; const w = v[i];
      lbImg.src = w.dataset.full; lbImg.alt = w.querySelector('img').alt;
      lbCap.textContent = `${w.querySelector('figcaption').textContent} · ${i + 1} з ${v.length}`;
    };
    const open = w => { last = w; show(visible().indexOf(w)); lb.classList.add('open'); document.body.style.overflow = 'hidden'; lb.querySelector('.lb-x').focus(); };
    const close = () => { lb.classList.remove('open'); document.body.style.overflow = ''; last && last.focus(); };
    works.forEach(w => w.addEventListener('click', () => open(w)));
    lb.querySelector('.lb-x').addEventListener('click', close);
    lb.querySelector('[data-dir=prev]').addEventListener('click', () => show(i - 1));
    lb.querySelector('[data-dir=next]').addEventListener('click', () => show(i + 1));
    lb.addEventListener('click', e => { if (e.target === lb) close(); });
    addEventListener('keydown', e => {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(i - 1);
      if (e.key === 'ArrowRight') show(i + 1);
    });
    let sx = null;
    lb.addEventListener('touchstart', e => sx = e.touches[0].clientX, { passive: true });
    lb.addEventListener('touchend', e => { if (sx === null) return; const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) show(i + (dx < 0 ? 1 : -1)); sx = null; });
  }

  /* ---------- price estimator ---------- */
  const calc = document.querySelector('.calc');
  if (calc) {
    const out = calc.querySelector('.tot b'), expl = calc.querySelector('[data-expl]');
    const fmt = n => n.toLocaleString('uk-UA');
    const modes = {
      movers: { a: ['Скільки вантажників', 1, 6, 2, 'ос.'], b: ['Скільки годин', 1, 10, 2, 'год'], calc: (a, b) => a * b * 250, text: (a, b) => `${a} × ${b} год × 250 грн` },
      up:     { a: ['Скільки мішків чи одиниць', 5, 300, 40, 'шт'], b: ['На який поверх', 1, 25, 4, 'пов.'], calc: (a, b) => a * b * 10, text: (a, b) => `${a} шт × ${b} пов. × 10 грн` },
      down:   { a: ['Скільки мішків сміття', 5, 300, 30, 'шт'], b: ['З якого поверху', 1, 25, 5, 'пов.'], calc: (a, b) => a * b * 10, text: (a, b) => `${a} шт × ${b} пов. × 10 грн` },
    };
    const ra = calc.querySelector('#ra'), rb = calc.querySelector('#rb');
    const la = calc.querySelector('[data-la]'), lb2 = calc.querySelector('[data-lb]');
    const oa = calc.querySelector('[data-oa]'), ob = calc.querySelector('[data-ob]');
    let m = modes.movers;
    const setMode = key => {
      m = modes[key];
      [[ra, m.a, la], [rb, m.b, lb2]].forEach(([r, d, l]) => { l.textContent = d[0]; r.min = d[1]; r.max = d[2]; r.value = d[3]; r.setAttribute('aria-label', d[0]); });
      upd();
    };
    const upd = () => {
      const a = +ra.value, b = +rb.value;
      oa.textContent = a; ob.textContent = b;
      out.textContent = fmt(m.calc(a, b));
      expl.textContent = m.text(a, b);
    };
    calc.querySelectorAll('input[name=mode]').forEach(r => r.addEventListener('change', () => setMode(r.value)));
    ra.addEventListener('input', upd); rb.addEventListener('input', upd);
    setMode('movers');
  }

  /* ---------- reviews ---------- */
  const revBox = document.querySelector('[data-reviews]');
  if (revBox && window.VH_REVIEWS) {
    const limit = +revBox.dataset.reviews || 99;
    const star = '<svg viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path d="M10 1.5l2.6 5.5 6 .7-4.4 4.1 1.2 6L10 14.9 4.6 17.8l1.2-6L1.4 7.7l6-.7z"/></svg>';
    const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
    revBox.innerHTML = window.VH_REVIEWS.slice(0, limit).map(r => `
      <article class="rev">
        ${r.sample ? '<span class="sample" title="Замініть на справжній відгук клієнта">Зразок</span>' : ''}
        <div class="stars" aria-label="Оцінка ${r.stars} з 5">${star.repeat(r.stars)}</div>
        <q>${esc(r.text)}</q>
        <div class="who"><span class="av" aria-hidden="true">${esc(r.name[0])}</span><div><b>${esc(r.name)}</b><span>${esc(r.job)}</span></div></div>
      </article>`).join('');
  }

  /* ---------- forms (formsubmit.co) ---------- */
  const ENDPOINT = 'https://formsubmit.co/ajax/yurakovalskiy61@gmail.com';
  const params = new URLSearchParams(location.search);
  const sel = document.querySelector('#fService');
  if (sel && params.get('service')) {
    const want = params.get('service');
    [...sel.options].forEach(o => { if (o.value === want) sel.value = want; });
  }
  document.querySelectorAll('form[data-send]').forEach(form => {
    const msg = form.querySelector('.form-msg');
    const btn = form.querySelector('button[type=submit]');
    form.addEventListener('submit', async e => {
      e.preventDefault();
      const data = Object.fromEntries(new FormData(form));
      const req = [...form.querySelectorAll('[required]')].find(f => !f.value.trim());
      if (req) { msg.className = 'form-msg err'; msg.textContent = `Заповніть поле «${req.dataset.label}».`; req.focus(); return; }
      const label = btn.textContent;
      btn.disabled = true; btn.textContent = 'Надсилаємо…'; msg.textContent = '';
      try {
        const res = await fetch(ENDPOINT, {
          method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ _subject: form.dataset.send, _template: 'table', ...data })
        });
        if (!res.ok) throw new Error(res.status);
        form.reset();
        msg.className = 'form-msg ok';
        msg.textContent = form.dataset.ok;
      } catch (err) {
        msg.className = 'form-msg err';
        msg.textContent = 'Заявка не надіслалась. Зателефонуйте 050 243 06 40 — так навіть швидше.';
      } finally { btn.disabled = false; btn.textContent = label; }
    });
  });

  const y = document.querySelector('[data-year]'); if (y) y.textContent = new Date().getFullYear();
})();
