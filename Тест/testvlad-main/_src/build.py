#!/usr/bin/env python3
"""Generates the static multi-page site into ../vh. Run: python3 build.py"""
import json, html, os
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DOMAIN = 'https://vantazhhub.lviv.ua/'
PHONE1, PHONE1_T = '050 243 06 40', '+380502430640'
PHONE2, PHONE2_T = '066 263 54 14', '+380662635414'
TG = 'https://t.me/yura03049'
WA = 'https://wa.me/380662635414'
TT = 'https://www.tiktok.com/@vantazh_hub'
VER = '3'

I = {
 'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
 'tg': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.4 4.2 2.9 11.3c-1.3.5-1.2 1.3-.2 1.6l4.7 1.5 1.8 5.6c.2.6.4.8.9.8.4 0 .6-.2.9-.4l2.3-2.2 4.7 3.5c.9.5 1.5.2 1.7-.8l3.1-14.6c.3-1.3-.5-1.9-1.4-1.5ZM9.6 14.6l-.4 4 -1.4-4.6 10.3-6.5-8.5 7.1Z"/></svg>',
 'wa': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.4-.2Z"/></svg>',
 'tt': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.6 2h-3.3v13.4a2.9 2.9 0 1 1-2.1-2.8V9.2a6.3 6.3 0 1 0 5.4 6.2V8.7a7.9 7.9 0 0 0 4.4 1.3V6.7a4.5 4.5 0 0 1-4.4-4.7Z"/></svg>',
 'l': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>',
 'r': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>',
 'x': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 'van': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M2 6h12v10H2zM14 9h4l3 3.5V16h-7z"/><circle cx="6" cy="17.5" r="1.8" fill="currentColor"/><circle cx="17" cy="17.5" r="1.8" fill="currentColor"/></svg>',
 'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
 'tag': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5" fill="currentColor"/></svg>',
 'hand': '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><path d="M6 22l8-8h8l4 4-4 3h-6M14 28h12l9-9-3-3-7 6"/><path d="M4 30l6-6"/></svg>',
 'box': '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l15-7 15 7v16l-15 7-15-7z"/><path d="M5 12l15 7 15-7M20 19v16"/></svg>',
 'talk': '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" aria-hidden="true"><path d="M5 8h22v15H14l-6 5v-5H5z"/><path d="M27 15h8v13h-3v4l-5-4h-9v-5"/></svg>',
}

SERVICES = [
 dict(id='vantazhni', name='Вантажні роботи', short='Переносимо меблі, техніку, матеріали — з квартири, з авто, між поверхами.', price='від 250 грн/год', img='second2',
      long='Коли треба перенести важке: шафу на п’ятий поверх, пральну машину в підвал, палети з машини на склад. Приїжджає стільки людей, скільки потребує задача.',
      incl=['Перенесення меблів і техніки', 'Завантаження й розвантаження машин', 'Робота на будь-якому поверсі, з ліфтом чи без']),
 dict(id='pidyom', name='Підйом будматеріалів', short='Мішки, плитка, блоки, гіпсокартон — на потрібний поверх.', price='від 10 грн/поверх', img='first1',
      long='Будматеріали привезли під під’їзд — далі наша справа. Піднімаємо суміші, плитку, газоблок, гіпсокартон і складаємо там, де скажете.',
      incl=['Сухі суміші, плитка, газоблок, гіпсокартон', 'Акуратне складання в приміщенні', 'Можемо розвантажити машину постачальника']),
 dict(id='smittya', name='Спуск і вивіз будсміття', short='Виносимо мішки після ремонту й вивозимо своїм бусом.', price='від 10 грн/поверх', img='down',
      long='Після ремонту лишаються гори мішків. Спускаємо їх з поверху, завантажуємо й вивозимо — ви отримуєте чисте приміщення.',
      incl=['Спуск мішків з будь-якого поверху', 'Завантаження й вивіз нашим транспортом', 'Великі обсяги — самоскидом']),
 dict(id='mebli', name='Утилізація меблів', short='Старі дивани, шафи, ліжка — винесемо й вивеземо.', price='ціна за домовленістю', img='second4',
      long='Старі меблі займають місце, а самому їх не винести. Розберемо, якщо треба, винесемо й вивеземо.',
      incl=['Дивани, шафи, ліжка, кухні', 'Розбирання громіздких меблів', 'Вивіз на утилізацію']),
 dict(id='demontazh', name='Демонтажні роботи', short='Демонтаж перегородок, підлоги, покриттів, конструкцій.', price='ціна за домовленістю', img='third2',
      long='Готуємо приміщення до ремонту: знімаємо покриття, розбираємо підлогу, демонтуємо конструкції. Сміття одразу виносимо й вивозимо.',
      incl=['Демонтаж підлоги, стяжки, покриттів', 'Розбирання конструкцій і перегородок', 'Винесення й вивіз сміття одразу']),
 dict(id='pereizd', name='Квартирні та офісні переїзди', short='Вантажники й транспорт в одному замовленні.', price='ціна за домовленістю', img='office',
      long='Переїзд — це і винести, і закріпити в машині, і занести на новому місці. Робимо все разом, бусом і своїми руками.',
      incl=['Вантажники та бус', 'Кріплення вантажу ременями в машині', 'Занесення й розстановка на новому місці']),
 dict(id='sklad', name='Складські та підсобні роботи', short='Завантаження, розвантаження, переміщення вантажів на складі.', price='від 250 грн/год', img='second1',
      long='Допомагаємо складам, магазинам і підприємствам: розвантажити фуру, перенести товар, допомогти на об’єкті на годину чи на кілька днів.',
      incl=['Розвантаження фур і контейнерів', 'Переміщення товару на складі', 'Підсобні роботи на об’єкті']),
 dict(id='taksi', name='Вантажне таксі', short='Перевеземо меблі, матеріали чи інший вантаж по Львову й області.', price='від 1600 грн', img='gallery3',
      long='Бус для перевезення по Львову та області. За потреби — з вантажниками, щоб вам не довелося нічого носити.',
      incl=['Перевезення по Львову й області', 'Можна з вантажниками', 'Меблі, матеріали, техніка']),
]
SVC_NAMES = [s['name'] for s in SERVICES]

WORKS = [
 ('smittya','down','Бус, завантажений мішками після ремонту'),
 ('budmat','first1','Будматеріали біля під’їзду'),
 ('inshe','dinosaur','Переміщення скульптури динозавра маніпулятором'),
 ('demontazh','third2','Демонтаж підлоги'),
 ('smittya','gallery2','Уламки плитки в кузові'),
 ('pereizd','office','Меблі закріплені ременями в бусі'),
 ('budmat','gallery8','Газоблок, розвантажений у дворі'),
 ('smittya','down2','Самоскид із будсміттям'),
 ('budmat','first2','Плитка на об’єкті'),
 ('smittya','gallery7','Вивіз старих речей і сміття'),
 ('demontazh','third1','Демонтаж стелі'),
 ('smittya','slider2','Розвантаження мішків з кузова'),
 ('budmat','gallery6','Суміші та фарба біля входу'),
 ('pereizd','second4','Меблі на вивіз'),
 ('smittya','gallery5','Мішки з будсміттям у бусі'),
 ('inshe','second1','Складські роботи'),
 ('budmat','slider3','Будматеріали в квартирі'),
 ('smittya','second3','Дерев’яні залишки після демонтажу'),
 ('smittya','gallery1','Залишки ремонту в бусі'),
 ('inshe','gallery10','Робота на ділянці'),
 ('smittya','gallery4','Мішки та картон після ремонту'),
 ('smittya','slider4','Мішки, підготовлені до вивозу'),
 ('smittya','gallery3','Вивіз з приватного будинку'),
 ('inshe','second2','Переносимо по вулиці'),
]
CATS = [('all','Усі'),('smittya','Вивіз сміття'),('budmat','Будматеріали'),('demontazh','Демонтаж'),('pereizd','Меблі й переїзди'),('inshe','Інше')]

NAV = [('posluhy.html','Послуги'),('tsiny.html','Ціни'),('roboty.html','Наші роботи'),('vidguky.html','Відгуки'),('pro-nas.html','Про нас'),('kontakty.html','Контакти')]

def e(s): return html.escape(s, quote=True)

def head(page, title, desc):
    url = DOMAIN + ('' if page == 'index.html' else page)
    ld = {"@context":"https://schema.org","@type":"MovingCompany","name":"VANTAZH HUB","url":DOMAIN,
          "image":DOMAIN+"img/og.jpg","logo":DOMAIN+"img/logo.png","telephone":[PHONE1_T,PHONE2_T],
          "areaServed":[{"@type":"City","name":"Львів"},{"@type":"AdministrativeArea","name":"Львівська область"}],
          "address":{"@type":"PostalAddress","addressLocality":"Львів","addressCountry":"UA"},
          "priceRange":"від 250 грн/год","sameAs":[TT,TG],"openingHours":"Mo-Su 00:00-23:59"}
    return f'''<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#17203A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="VANTAZH HUB">
<meta property="og:locale" content="uk_UA">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="img/favicon.png">
<link rel="apple-touch-icon" href="img/favicon.png">
<link rel="preload" href="assets/fonts/unbounded.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="assets/fonts/onest.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="assets/style.css?v={VER}">
<script>try{{if(sessionStorage.getItem('vh-shutter')==='1'&&!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('arriving')}}catch(e){{}}</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-BR3HJHEDF2"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-BR3HJHEDF2');</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<div class="shutter" aria-hidden="true"><img src="img/mark.png" alt=""></div>
<a class="sr" href="#main">Перейти до змісту</a>
<header class="hdr">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="VANTAZH HUB — на головну"><img src="img/mark.png" alt="" width="62" height="38"><b>VANTAZH<span> </span>HUB</b></a>
    <nav class="nav" aria-label="Основне меню">{''.join(f'<a href="{h}"{" aria-current=page" if h==page else ""}>{t}</a>' for h,t in NAV)}</nav>
    <a class="hdr-call" href="tel:{PHONE1_T}"><span class="ic">{I['phone']}</span><span><small>Дзвоніть 24/7</small>{PHONE1}</span></a>
    <button class="burger" aria-label="Відкрити меню" aria-expanded="false" aria-controls="mnav"><i></i></button>
  </div>
</header>
<nav class="mnav" id="mnav" aria-label="Мобільне меню">
  <a href="index.html"{" aria-current=page" if page=="index.html" else ""}>Головна</a>
  {''.join(f'<a href="{h}"{" aria-current=page" if h==page else ""}>{t}</a>' for h,t in NAV)}
  <div class="mnav-phones"><a href="tel:{PHONE1_T}">{PHONE1}</a><a href="tel:{PHONE2_T}">{PHONE2}</a></div>
</nav>
<main id="main">
'''

def foot():
    return f'''</main>
<footer class="ftr">
  <div class="wrap">
    <div>
      <a class="brand" href="index.html"><img src="img/mark.png" alt="" width="56" height="34"><b>VANTAZH HUB</b></a>
      <p style="margin-top:18px">Вантажники, бус і підсобні роботи у Львові та Львівській області.</p>
    </div>
    <div><h4>Сторінки</h4><ul>{''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}</ul></div>
    <div><h4>Зв’язок</h4><ul>
      <li><a href="tel:{PHONE1_T}">{PHONE1}</a></li><li><a href="tel:{PHONE2_T}">{PHONE2}</a></li>
      <li><a href="{TG}" target="_blank" rel="noopener">Telegram</a></li><li><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
      <li><a href="{TT}" target="_blank" rel="noopener">TikTok @vantazh_hub</a></li></ul></div>
    <div class="copy"><span>© <span data-year>2026</span> VANTAZH HUB</span><span>Львів та область</span></div>
  </div>
</footer>
<div class="mbar" aria-label="Швидкий зв’язок">
  <a href="tel:{PHONE1_T}">{I['phone']} Подзвонити</a>
  <a href="{TG}" target="_blank" rel="noopener" aria-label="Telegram">{I['tg']} Telegram</a>
  <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{I['wa']} WhatsApp</a>
</div>
<div class="peek" aria-hidden="true"><img alt=""></div>
<script src="assets/reviews.js?v={VER}"></script>
<script src="assets/main.js?v={VER}"></script>
</body>
</html>
'''

def phead(crumb, lines, lead):
    return f'''<section class="phead">
  <img class="phead-mark" src="img/mark.png" alt="" aria-hidden="true">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Головна</a> / {crumb}</p>
    <h1>{''.join(f'<span class="ln"><span>{l}</span></span>' for l in lines)}</h1>
    <p class="lead">{lead}</p>
    {{extra}}
  </div>
</section>
'''

def cta(title='Розкажіть, що треба зробити', sub='Назвемо орієнтовну ціну ще під час розмови. Дзвоніть або пишіть у месенджер — відповідаємо швидко.'):
    return f'''<section class="sec inv cta">
  <div class="wrap">
    <div><h2>{title}</h2><p class="lead" style="margin-top:22px">{sub}</p></div>
    <div class="phones">
      <a class="phone-big" href="tel:{PHONE1_T}"><span><span>Основний номер</span><b>{PHONE1}</b></span><span class="ic">{I['phone']}</span></a>
      <a class="phone-big" href="tel:{PHONE2_T}"><span><span>Другий номер · WhatsApp</span><b>{PHONE2}</b></span><span class="ic">{I['phone']}</span></a>
      <div class="msgs"><a class="btn btn-w" href="{TG}" target="_blank" rel="noopener">{I['tg']} Telegram</a><a class="btn btn-g" href="{WA}" target="_blank" rel="noopener">{I['wa']} WhatsApp</a></div>
    </div>
  </div>
</section>
'''

def steps():
    return '''<ol class="steps">
  <li><h3>Ви пишете чи дзвоните</h3><p>Телефоном, у Telegram чи WhatsApp — як зручно.</p></li>
  <li><h3>Уточнюємо деталі</h3><p>Адреса, поверх, ліфт, обсяг. Фото задачі дуже допомагає.</p></li>
  <li><h3>Називаємо ціну</h3><p>Орієнтовну вартість ви знаєте ще до початку роботи.</p></li>
  <li><h3>Приїжджаємо й робимо</h3><p>У погоджений час. Розраховуєтесь, коли все готово.</p></li>
</ol>'''

def pic(name, alt, cls='', sizes='(max-width:760px) 100vw, 40vw', lazy=True):
    return f'<img{f" class={chr(34)}{cls}{chr(34)}" if cls else ""} src="img/{name}.webp" srcset="img/{name}-s.webp 640w, img/{name}.webp 1280w" sizes="{sizes}" alt="{e(alt)}"{" loading=lazy decoding=async" if lazy else ""}>'

pages = {}

# ---------------- HOME ----------------
def from_html(p):
    return '<span class="from"><b class="q">за домовленістю</b></span>' if 'домовлен' in p else f'<span class="from">від<b>{p.replace("від ","")}</b></span>'
svc_rows = ''.join(f'''<li><a href="posluhy.html#{s['id']}" data-img="img/{s['img']}-s.webp"><h3>{s['name']}</h3><p>{s['short']}</p>{from_html(s['price'])}</a></li>''' for s in SERVICES)

strip_pics = [('down','Бус із мішками після ремонту'),('dinosaur','Скульптура динозавра на маніпуляторі'),('third2','Демонтаж підлоги'),('first1','Будматеріали біля під’їзду'),('office','Меблі закріплені в бусі'),('gallery8','Газоблок у дворі'),('gallery2','Уламки плитки в кузові'),('slider2','Розвантаження мішків')]
strip = ''.join(f'<figure><div class="ph">{pic(n,c,sizes="340px")}</div><figcaption>{c}</figcaption></figure>' for n,c in strip_pics)

pages['index.html'] = (
 'Вантажники у Львові — вивіз сміття, підйом будматеріалів | VANTAZH HUB',
 'Вантажники та бус у Львові й області: підйом будматеріалів, спуск і вивіз будсміття, утилізація меблів, демонтаж, переїзди, вантажне таксі. Від 250 грн/год. 050 243 06 40.',
 f'''<section class="hero">
  <div class="hero-grid">
    <div class="hero-copy">
      <h1><span class="ln"><span>Винесемо.</span></span><span class="ln"><span>Піднімемо.</span></span><span class="ln"><span>Вивеземо.</span></span></h1>
      <p class="hero-sub">Вантажники та бус у Львові й області. Будматеріали на поверх, сміття після ремонту, старі меблі, переїзди — одна бригада на все.</p>
      <div class="btns">
        <a class="btn btn-o" href="tel:{PHONE1_T}">{I['phone']} {PHONE1}</a>
        <a class="btn btn-g" href="{TG}" target="_blank" rel="noopener">{I['tg']} Написати в Telegram</a>
      </div>
    </div>
    <div class="hero-ph">
      <img class="hero-img" src="img/down.webp" srcset="img/down-s.webp 640w, img/down.webp 1280w" sizes="(max-width:860px) 100vw, 40vw" alt="Бус VANTAZH HUB, завантажений мішками з будсміттям" fetchpriority="high">
      <div class="tag" aria-label="Вантажник від 250 гривень за годину"><small>Вантажник</small><strong>від 250 грн</strong><small>за годину</small></div>
    </div>
  </div>
</section>
<section class="facts" aria-label="Коротко про нас">
  <ul>
    <li>{I['clock']}<div><b>На зв’язку 24/7</b><span>Відповідаємо й у вихідні</span></div></li>
    <li>{I['van']}<div><b>Свій бус</b><span>Привеземо, вивеземо, перевеземо</span></div></li>
    <li>{I['pin']}<div><b>Львів і область</b><span>Виїжджаємо за місто</span></div></li>
    <li>{I['tag']}<div><b>Ціна до початку</b><span>Без сюрпризів після роботи</span></div></li>
  </ul>
</section>
<section class="sec">
  <div class="wrap">
    <div class="sec-head"><h2>Що беремо на себе</h2><p class="lead">Окремі вантажники на годину чи повний цикл разом із транспортом — оберіть, що потрібно. Ціни орієнтовні, точну назвемо після уточнення деталей.</p></div>
    <ul class="svc">{svc_rows}</ul>
    <div class="btns" style="margin-top:36px"><a class="btn btn-n" href="posluhy.html">Усі послуги детально</a><a class="btn btn-g" href="tsiny.html">Порахувати вартість</a></div>
  </div>
</section>
<section class="sec inv" style="padding-bottom:clamp(56px,7vw,96px)">
  <div class="wrap"><div class="sec-head"><div><h2>З останніх виїздів</h2></div><div style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap"><p class="lead">Наші фото з об’єктів — без стокових картинок.</p><div class="strip-nav" data-strip="strip1"><button class="rbtn" data-dir="prev" aria-label="Попередні фото">{I['l']}</button><button class="rbtn" data-dir="next" aria-label="Наступні фото">{I['r']}</button></div></div></div></div>
  <div class="strip" id="strip1" style="max-width:calc(var(--wrap) + 2*var(--gut));margin:0 auto">{strip}</div>
  <div class="wrap" style="margin-top:28px"><a class="btn btn-w" href="roboty.html">Дивитися всі роботи</a></div>
</section>
<section class="sec white">
  <div class="wrap story">
    {pic('dinosaur','Бригада VANTAZH HUB переміщує скульптуру динозавра за допомогою маніпулятора')}
    <div>
      <h2>Нестандартний вантаж? Розберемося</h2>
      <p class="lead" style="margin-top:22px">Одного разу ми переміщали скульптуру динозавра. Сейф, піаніно, важкий верстат чи щось, що не проходить у двері, — опишіть вантаж, і ми підкажемо, як його краще перенести або перевезти.</p>
      <div class="btns" style="margin-top:28px"><a class="btn btn-o" href="{TG}" target="_blank" rel="noopener">{I['tg']} Надіслати фото вантажу</a></div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="sec-head"><h2>Як замовити</h2><p class="lead">Чотири кроки. Зазвичай усе вирішуємо за один дзвінок.</p></div>
    {steps()}
  </div>
</section>
<section class="sec white">
  <div class="wrap">
    <div class="sec-head"><h2>Що кажуть клієнти</h2><p class="lead">Відгуки людей, яким ми вже допомогли з переїздом, ремонтом чи вивозом.</p></div>
    <div class="revs" data-reviews="3"></div>
    <div class="btns" style="margin-top:32px"><a class="btn btn-n" href="vidguky.html">Усі відгуки</a></div>
  </div>
</section>
''' + cta())

# ---------------- SERVICES ----------------
blocks = ''.join(f'''<article class="sblock" id="{s['id']}">
  <div class="sb-img">{pic(s['img'], s['name'])}</div>
  <div>
    <h2>{s['name']}</h2>
    <p class="lead">{s['long']}</p>
    <ul class="incl">{''.join(f'<li>{x}</li>' for x in s['incl'])}</ul>
    <div class="sb-price"><span class="p">Вартість<b>{s['price']}</b></span><a class="btn btn-o" href="kontakty.html?service={e(s['name'])}#form">Замовити</a></div>
  </div>
</article>''' for s in SERVICES)
ph = phead('Послуги', ['Вісім задач,', 'одна бригада'], 'Все, що пов’язано з важким: перенести, підняти, демонтувати, вивезти. Можна замовити окремо або разом.')
ph = ph.replace('{extra}', '<nav class="jump" aria-label="Перехід до послуги">' + ''.join(f'<a href="#{s["id"]}">{s["name"]}</a>' for s in SERVICES) + '</nav>')
pages['posluhy.html'] = (
 'Послуги вантажників у Львові — VANTAZH HUB',
 'Вантажні роботи, підйом будматеріалів, спуск і вивіз будсміття, утилізація меблів, демонтаж, переїзди, складські роботи та вантажне таксі у Львові та області.',
 ph + f'<section class="sec-tight" style="padding-top:0"><div class="wrap">{blocks}</div></section>' + cta())

# ---------------- PRICES ----------------
ph = phead('Ціни', ['Ціни без', 'дрібного шрифту'], 'Базові тарифи та калькулятор, щоб прикинути бюджет. Точну суму назвемо після розмови: вона залежить від поверху, ліфта та обсягу.').replace('{extra}','')
pages['tsiny.html'] = (
 'Ціни на послуги вантажників у Львові — VANTAZH HUB',
 'Тарифи VANTAZH HUB: вантажники від 250 грн/год, підйом будматеріалів і спуск сміття від 10 грн/поверх, вантажне таксі від 1600 грн. Калькулятор вартості.',
 ph + f'''<section class="sec">
  <div class="wrap">
    <div class="prices">
      <div class="price hl"><h3>Вантажник</h3><p>Перенесення, завантаження, підсобні роботи</p><div class="amt"><small>від</small><b>250</b><i>грн/год</i></div></div>
      <div class="price"><h3>Підйом будматеріалів</h3><p>Мішки, плитка, блоки на поверх</p><div class="amt"><small>від</small><b>10</b><i>грн/поверх</i></div></div>
      <div class="price"><h3>Спуск будсміття</h3><p>Винесення мішків з поверху</p><div class="amt"><small>від</small><b>10</b><i>грн/поверх</i></div></div>
      <div class="price"><h3>Вантажне таксі</h3><p>Бус по Львову та області</p><div class="amt"><small>від</small><b>1600</b><i>грн</i></div></div>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><h2>Прикиньте вартість</h2><p class="lead">Калькулятор рахує за базовим тарифом. Це орієнтир, а не фінальна ціна.</p></div>
    <div class="calc">
      <div class="calc-in">
        <fieldset class="fld" style="border:0;padding:0;margin:0"><legend style="font-weight:600;margin-bottom:10px">Що потрібно</legend>
          <div class="seg">
            <label><input type="radio" name="mode" value="movers" checked><span>Вантажники</span></label>
            <label><input type="radio" name="mode" value="up"><span>Підйом матеріалів</span></label>
            <label><input type="radio" name="mode" value="down"><span>Спуск сміття</span></label>
          </div>
        </fieldset>
        <label class="fld"><span data-la>Скільки вантажників</span><span class="range-row"><input id="ra" type="range"><output data-oa>2</output></span></label>
        <label class="fld"><span data-lb>Скільки годин</span><span class="range-row"><input id="rb" type="range"><output data-ob>2</output></span></label>
      </div>
      <div class="calc-out" aria-live="polite">
        <span>Орієнтовно</span>
        <div class="tot"><b>1 000</b> <small>грн</small></div>
        <p data-expl></p>
        <p>Ціна може змінитися через відсутність ліфта, вагу, довге перенесення від машини або терміновість.</p>
        <a class="btn btn-o" href="tel:{PHONE1_T}">{I['phone']} Уточнити ціну</a>
      </div>
    </div>
    <div class="notes">
      <div><h3>Що впливає на ціну</h3><p>Поверх і наявність ліфта, вага та кількість, відстань від машини до під’єзду, складність демонтажу.</p></div>
      <div><h3>Коли ви дізнаєтесь суму</h3><p>До початку роботи. Надішліть фото чи опис — назвемо орієнтовну вартість ще в переписці.</p></div>
      <div><h3>Великі обсяги</h3><p>Для об’єктів, складів і довгих робіт домовляємося про окрему ціну.</p></div>
    </div>
  </div>
</section>
''' + cta('Хочете точну ціну?', 'Надішліть фото або опишіть задачу — порахуємо й відповімо.'))

# ---------------- WORKS ----------------
counts = {c: sum(1 for w in WORKS if w[0]==c) for c,_ in CATS}; counts['all'] = len(WORKS)
filters = ''.join(f'<button type="button" data-f="{c}" aria-pressed="{"true" if c=="all" else "false"}">{t}<span>{counts[c]}</span></button>' for c,t in CATS)
from PIL import Image
def dims(n):
    with Image.open(f'{OUT}/img/{n}-s.webp') as im: return im.size
works = ''.join((lambda w,h: f'<figure class="work" data-cat="{c}" data-full="img/{n}.webp" tabindex="0" role="button" aria-label="Відкрити фото: {e(cap)}"><img src="img/{n}-s.webp" width="{w}" height="{h}" alt="{e(cap)}" loading="lazy" decoding="async"><figcaption>{cap}</figcaption></figure>')(*dims(n)) for c,n,cap in WORKS)
ph = phead('Наші роботи', ['Фото', 'з об’єктів'], 'Знімаємо на телефон прямо під час роботи. Тут немає стокових картинок — лише реальні виїзди у Львові та області.').replace('{extra}','')
pages['roboty.html'] = (
 'Наші роботи — фото виконаних замовлень | VANTAZH HUB',
 'Фото реальних замовлень VANTAZH HUB у Львові: вивіз будсміття, підйом будматеріалів, демонтаж, перевезення меблів та нестандартних вантажів.',
 ph + f'''<section class="sec">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Фільтр робіт">{filters}</div>
    <div class="works">{works}</div>
    <p class="lead" style="margin-top:32px">Більше відео з роботи — у нашому <a href="{TT}" target="_blank" rel="noopener">TikTok @vantazh_hub</a>.</p>
  </div>
</section>
<div class="lb" role="dialog" aria-modal="true" aria-label="Перегляд фото">
  <button class="rbtn lb-x" aria-label="Закрити">{I['x']}</button>
  <img alt="">
  <div class="lb-bar"><button class="rbtn" data-dir="prev" aria-label="Попереднє фото">{I['l']}</button><p></p><button class="rbtn" data-dir="next" aria-label="Наступне фото">{I['r']}</button></div>
</div>
''' + cta())

# ---------------- REVIEWS ----------------
ph = phead('Відгуки', ['Що кажуть', 'клієнти'], 'Відгуки людей, яким ми допомогли з переїздом, ремонтом чи вивозом. Працювали з нами? Залиште свій — нам це дуже допомагає.').replace('{extra}', '<div class="btns" style="margin-top:28px"><a class="btn btn-o" href="#leave">Залишити відгук</a></div>')
pages['vidguky.html'] = (
 'Відгуки клієнтів — VANTAZH HUB, вантажники у Львові',
 'Відгуки клієнтів про вантажників VANTAZH HUB у Львові та області. Залиште свій відгук про нашу роботу.',
 ph + f'''<section class="sec">
  <div class="wrap">
    <div class="revs" data-reviews></div>
  </div>
</section>
<section class="sec white" id="leave" style="scroll-margin-top:76px">
  <div class="wrap contact-grid">
    <div>
      <h2>Залиште відгук</h2>
      <p class="lead" style="margin-top:22px">Напишіть кілька речень: що замовляли і як усе пройшло. Ми опублікуємо відгук на сайті з вашого дозволу.</p>
      <p class="lead">Можна й простіше — надішліть голосове чи текст у <a href="{TG}" target="_blank" rel="noopener">Telegram</a>.</p>
    </div>
    <form class="form" data-send="Новий відгук з сайту" data-ok="Дякуємо! Відгук отримали — опублікуємо після перевірки." novalidate>
      <div class="row2">
        <label>Ваше ім’я<input name="Ім’я" data-label="Ваше ім’я" required autocomplete="given-name"></label>
        <label>Що замовляли<select name="Послуга">{''.join(f'<option>{n}</option>' for n in SVC_NAMES)}</select></label>
      </div>
      <label>Оцінка<select name="Оцінка"><option>5 — все чудово</option><option>4 — добре</option><option>3 — нормально</option><option>2 — є зауваження</option><option>1 — погано</option></select></label>
      <label>Відгук<textarea name="Відгук" data-label="Відгук" required></textarea></label>
      <label style="grid-template-columns:auto 1fr;align-items:start;font-weight:400"><input type="checkbox" name="Дозвіл на публікацію" value="так" style="width:20px;height:20px;margin-top:2px" checked> Дозволяю опублікувати відгук із моїм ім’ям</label>
      <button class="btn btn-o" type="submit">Надіслати відгук</button>
      <p class="form-msg" role="status"></p>
    </form>
  </div>
</section>
''' + cta())

# ---------------- ABOUT ----------------
ph = phead('Про нас', ['Бригада, яка', 'бере важке'], 'Ми — команда вантажників зі Львова. Понад рік щодня носимо, піднімаємо, демонтуємо й вивозимо по місту та області.').replace('{extra}','')
pages['pro-nas.html'] = (
 'Про нас — VANTAZH HUB, вантажні послуги у Львові',
 'VANTAZH HUB — команда вантажників зі Львова з власним бусом. Вантажні, підсобні та демонтажні роботи у Львові та області понад рік.',
 ph + f'''<section class="sec">
  <div class="wrap about-grid">
    <div class="about-text">
      <h2 style="margin-bottom:26px">Без зайвих клопотів для вас</h2>
      <p>Ми допомагаємо з підйомом будматеріалів, винесенням і вивозом сміття, утилізацією старих меблів, переїздами та іншою фізично важкою роботою.</p>
      <p>Можемо надати лише вантажників, а можемо приїхати разом із транспортом і закрити задачу повністю: від першого мішка до чистого під’їзду.</p>
      <p>Працюємо у Львові та по всій Львівській області. Здебільшого замовлення приходять від людей, які роблять ремонт, від бригад будівельників, магазинів і складів.</p>
      <div class="btns" style="margin-top:28px"><a class="btn btn-n" href="roboty.html">Подивитися наші роботи</a></div>
    </div>
    <div class="about-photos">{pic('second2','Вантажники несуть вантаж вулицею', sizes='25vw')}{pic('gallery10','Бригада на виїзді', sizes='25vw')}</div>
  </div>
</section>
<section class="sec inv">
  <div class="wrap">
    <h2 style="margin-bottom:clamp(36px,5vw,64px)">На чому тримається робота</h2>
    <div class="vals">
      <div>{I['talk']}<h3>Домовляємося наперед</h3><p>Ціну, час і обсяг погоджуємо до початку. Якщо щось змінюється на місці, спершу кажемо вам.</p></div>
      <div>{I['box']}<h3>Акуратно з вашим</h3><p>Меблі закріплюємо ременями в машині, під’їзд після себе не лишаємо в пилюці.</p></div>
      <div>{I['hand']}<h3>Все одним замовленням</h3><p>Вантажники, бус, вивіз сміття — не треба шукати трьох різних виконавців.</p></div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="sec-head"><h2>Як ми працюємо</h2><p class="lead">Простий порядок, який ми повторюємо на кожному замовленні.</p></div>
    {steps()}
  </div>
</section>
''' + cta())

# ---------------- CONTACTS ----------------
ph = phead('Контакти', ['Зв’яжіться', 'з нами'], 'Найшвидше — подзвонити. Якщо незручно говорити, напишіть у месенджер або залиште номер, і ми перетелефонуємо.').replace('{extra}', f'<div class="btns" style="margin-top:28px"><a class="btn btn-o" href="tel:{PHONE1_T}">{I["phone"]} {PHONE1}</a><a class="btn btn-g" href="{TG}" target="_blank" rel="noopener">{I["tg"]} Telegram</a></div>')
pages['kontakty.html'] = (
 'Контакти — VANTAZH HUB, вантажники у Львові',
 'Замовити вантажників у Львові: 050 243 06 40, 066 263 54 14, Telegram, WhatsApp. Працюємо у Львові та Львівській області.',
 ph + f'''<section class="sec">
  <div class="wrap contact-grid">
    <div>
      <ul class="clist">
        <li><span>Телефон</span><div><a href="tel:{PHONE1_T}">{PHONE1}</a><br><a href="tel:{PHONE2_T}">{PHONE2}</a></div></li>
        <li><span>Telegram</span><a href="{TG}" target="_blank" rel="noopener">@yura03049</a></li>
        <li><span>WhatsApp</span><a href="{WA}" target="_blank" rel="noopener">{PHONE2}</a></li>
        <li><span>TikTok</span><a href="{TT}" target="_blank" rel="noopener">@vantazh_hub</a></li>
        <li><span>Де працюємо</span><div>Львів та Львівська область</div></li>
        <li><span>Коли</span><div>На зв’язку щодня, 24/7</div></li>
      </ul>
      <p class="lead" style="margin-top:28px">Порада: надішліть фото вантажу чи приміщення в месенджер — так ми назвемо ціну точніше.</p>
    </div>
    <form class="form" id="form" style="scroll-margin-top:96px" data-send="Заявка на дзвінок з сайту" data-ok="Дякуємо! Заявку отримали — перетелефонуємо найближчим часом." novalidate>
      <h2>Замовити дзвінок</h2>
      <div class="row2">
        <label>Ім’я<input name="Ім’я" data-label="Ім’я" required autocomplete="given-name" placeholder="Як до вас звертатися"></label>
        <label>Телефон<input name="Телефон" data-label="Телефон" type="tel" required autocomplete="tel" placeholder="+380"></label>
      </div>
      <label>Яка послуга потрібна<select id="fService" name="Послуга">{''.join(f'<option>{n}</option>' for n in SVC_NAMES)}</select></label>
      <label>Деталі (необов’язково)<textarea name="Деталі" placeholder="Адреса, поверх, чи є ліфт, обсяг роботи, бажаний час"></textarea></label>
      <button class="btn btn-o" type="submit">Замовити дзвінок</button>
      <p class="form-msg" role="status"></p>
      <p class="hint">Номер використовуємо лише щоб передзвонити вам щодо замовлення.</p>
    </form>
  </div>
</section>
''')

for fn,(t,d,body) in pages.items():
    with open(f'{OUT}/{fn}','w') as f: f.write(head(fn,t,d) + body + foot())

# sitemap / robots / CNAME / 404
today='2026-10-15'
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{DOMAIN}{"" if fn=="index.html" else fn}</loc><lastmod>{today}</lastmod><priority>{"1.0" if fn=="index.html" else "0.8"}</priority></url>\n' for fn in pages) + '</urlset>\n'
open(f'{OUT}/sitemap.xml','w').write(sm)
open(f'{OUT}/robots.txt','w').write(f'User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}sitemap.xml\n')
open(f'{OUT}/CNAME','w').write('vantazhhub.lviv.ua\n')
nf = phead('404', ['Цю сторінку', 'вже вивезли'], 'Такої сторінки немає. Поверніться на головну або одразу подзвоніть нам.').replace('{extra}', f'<div class="btns" style="margin-top:28px"><a class="btn btn-o" href="index.html">На головну</a><a class="btn btn-g" href="tel:{PHONE1_T}">{PHONE1}</a></div>')
open(f'{OUT}/404.html','w').write(head('404.html','Сторінку не знайдено — VANTAZH HUB','Сторінку не знайдено.').replace('<link rel="canonical" href="https://vantazhhub.lviv.ua/404.html">','<meta name="robots" content="noindex">') + nf + foot())
print('built', len(pages)+1, 'pages')
