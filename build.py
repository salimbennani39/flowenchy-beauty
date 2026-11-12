"""Génère le site statique Flowenchy Beauty dans ./site.

Usage : python3 build.py
Toutes les pages partagent l'en-tête, le pied de page et les données ci-dessous.
Source des prix et durées : page Planity (novembre 2026).
"""

from pathlib import Path
from html import escape

OUT = Path(__file__).parent / "site"

BOOK = "https://www.planity.com/flowenchy-beauty-75004-paris"
INSTA = "https://www.instagram.com/flowenchybeauty/"
PHONE = "+33 6 52 77 11 41"
PHONE_LINK = "tel:+33652771141"
ADDRESS = "27 rue de Turenne, 75004 Paris"
MAPS = "https://www.google.com/maps/search/?api=1&query=Flowenchy+Beauty+27+Rue+de+Turenne+75004+Paris"

# Horaires Google Maps
HOURS = [
    ("Lundi", "10h – 20h"),
    ("Mardi", "10h – 20h"),
    ("Mercredi", "10h – 20h"),
    ("Jeudi", "10h – 20h"),
    ("Vendredi", "10h – 20h"),
    ("Samedi", "10h – 20h"),
    ("Dimanche", "Fermé"),
]

NAV_LEFT = [
    ("restructuration-sourcils.html", "Sourcils"),
    ("brow-lift.html", "Brow lift"),
    ("rehaussement-cils.html", "Lash lift"),
    ("microblading.html", "Microblading"),
]
NAV_RIGHT = [
    ("tarifs.html", "Tarifs"),
    ("la-maison.html", "La maison"),
    ("contact.html", "Contact"),
]


def arrow():
    return '<span class="arrow" aria-hidden="true"></span>'


def book_btn(label="Réserver", cls="btn"):
    return f'<a class="{cls}" href="{BOOK}" target="_blank" rel="noopener">{label} {arrow()}</a>'


def nav_links(items, current):
    out = []
    for href, label in items:
        cur = ' aria-current="page"' if href == current else ""
        out.append(f'<a href="{href}"{cur}>{label}</a>')
    return "".join(out)


def hours_list():
    return "".join(f"<li><span>{d}</span><span>{h}</span></li>" for d, h in HOURS)


def page(filename, title, description, body, current=None, extra_head=""):
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="assets/img/hero.jpg">
<meta name="theme-color" content="#f4efe9">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
{extra_head}
</head>
<body>
<div class="topbar"><span class="topbar__extra">Réservation en ligne 24h/24 · confirmation immédiate — </span><a href="{BOOK}" target="_blank" rel="noopener">Prendre rendez-vous</a></div>
<header class="header">
  <div class="wrap header__inner">
    <nav class="nav nav--left" aria-label="Prestations">{nav_links(NAV_LEFT, current)}</nav>
    <a class="wordmark" href="index.html" aria-label="Flowenchy Beauty, accueil">
      <span class="wordmark__name">FLOWENCHY</span>
      <span class="wordmark__sub">BEAUTY</span>
    </a>
    <div class="header__right">
      <nav class="nav" aria-label="Infos">{nav_links(NAV_RIGHT, current)}</nav>
      {book_btn()}
      <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
    </div>
  </div>
</header>
<nav class="mobile-menu" aria-label="Menu mobile">
  <a href="index.html">Accueil</a>
  {"".join(f'<a href="{h}">{l}</a>' for h, l in NAV_LEFT + NAV_RIGHT)}
  {book_btn("Réserver sur Planity")}
  <p class="mobile-menu__meta">{ADDRESS}<br>Lun – Sam · 10h – 20h</p>
</nav>

<main>
{body}
</main>

<footer class="footer">
  <div class="wrap">
    <div class="footer__top">
      <div>
        <a class="wordmark" href="index.html"><span class="wordmark__name">FLOWENCHY</span><span class="wordmark__sub">BEAUTY · PARIS</span></a>
        <p class="footer__tag">Experte du regard depuis plus de 12 ans, au cœur du Marais.</p>
      </div>
      <div>
        <h4>Prestations</h4>
        <ul>{"".join(f'<li><a href="{h}">{l}</a></li>' for h, l in [("restructuration-sourcils.html", "Restructuration sourcils"), ("brow-lift.html", "Brow lift"), ("rehaussement-cils.html", "Rehaussement de cils"), ("microblading.html", "Microblading"), ("tarifs.html", "Tous les tarifs")])}</ul>
      </div>
      <div>
        <h4>Le studio</h4>
        <ul>
          <li><a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS}</a></li>
          <li>Métro Saint-Paul (ligne 1)</li>
          <li>Lun – Sam · 10h – 20h</li>
          <li><a href="{PHONE_LINK}">{PHONE}</a></li>
        </ul>
      </div>
      <div>
        <h4>Suivre</h4>
        <ul>
          <li><a href="{INSTA}" target="_blank" rel="noopener">Instagram @flowenchybeauty</a></li>
          <li><a href="{BOOK}" target="_blank" rel="noopener">Réserver sur Planity</a></li>
          <li><a href="la-maison.html">La maison</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© 2026 Flowenchy Beauty · Paris 4e</span>
      <span>Brow lift · Lash lift · Restructuration · Microblading</span>
    </div>
  </div>
</footer>
<div class="sticky-book">{book_btn("Réserver")}</div>
<div class="sc-preview" role="note">Aperçu <a href="https://showcasecreativehouse.com" target="_blank" rel="noopener">SHOWCASE</a> · pas encore en ligne</div>
<script src="assets/main.js" defer></script>
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")


# ------------------------------------------------------------------ blocs communs

def price_rows(rows):
    out = []
    for name, desc, dur, eur, *badge in rows:
        b = f'<span class="badge">{badge[0]}</span>' if badge else ""
        d = f"<p>{desc}</p>" if desc else ""
        out.append(
            f'<div class="price-row"><div><h4>{name}{b}</h4>{d}</div>'
            f'<span class="dur">{dur}</span><span class="eur">{eur}</span></div>'
        )
    return f'<div class="price-list">{"".join(out)}</div>'


def faq(items):
    return '<div class="faq">' + "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items
    ) + "</div>"


def ba(figs, dark=False):
    return '<div class="ba-grid">' + "".join(
        f'<figure class="reveal"><img src="assets/img/{src}" alt="{escape(alt)}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
        for src, alt, cap in figs
    ) + "</div>"


def info_band():
    return f"""
<section class="section section--sand">
  <div class="wrap info-band">
    <div class="reveal">
      <h4>Le studio</h4>
      <p>{ADDRESS}<br>Le Marais · Métro Saint-Paul</p>
      <p style="margin-top:18px"><a class="link" href="{MAPS}" target="_blank" rel="noopener">Itinéraire</a></p>
    </div>
    <div class="reveal">
      <h4>Horaires</h4>
      <ul class="hours">{hours_list()}</ul>
    </div>
    <div class="reveal">
      <h4>Rendez-vous</h4>
      <p>Uniquement sur réservation, en ligne 24h/24.</p>
      <p style="margin:18px 0 24px"><a href="{PHONE_LINK}">{PHONE}</a></p>
      {book_btn("Réserver sur Planity")}
    </div>
  </div>
</section>"""


def cta(title="Offrez à votre regard <em>l'attention</em> qu'il mérite."):
    return f"""
<section class="section--paper cta">
  <div class="wrap">
    <img class="cta__medal reveal" src="assets/img/logo-medaillon.png" alt="Flowenchy Beauty" width="120" height="120">
    <span class="eyebrow reveal">Sur rendez-vous</span>
    <h2 class="reveal">{title}</h2>
    <div class="reveal">{book_btn("Prendre rendez-vous")}</div>
  </div>
</section>"""


SERVICES = [
    ("restructuration-sourcils.html", "restructuration.jpg", "Restructuration", "Un tracé pensé pour votre visage, une ligne nette et naturelle.", "dès 50 €"),
    ("brow-lift.html", "browlift.jpg", "Brow lift", "Des sourcils disciplinés, fournis et brossés vers le haut.", "dès 90 €"),
    ("rehaussement-cils.html", "lashlift-3.jpg", "Lash lift", "Une courbure naturelle qui ouvre le regard, sans mascara.", "dès 90 €"),
    ("microblading.html", "portrait-boucles.jpg", "Microblading", "Des poils dessinés un à un pour combler et restructurer.", "dès 450 €"),
]


def others(exclude):
    cards = []
    for href, img, name, _, price in SERVICES:
        if href == exclude:
            continue
        cards.append(
            f'<a class="other reveal" href="{href}"><img src="assets/img/{img}" alt="{name}" loading="lazy">'
            f"<div><h3>{name}</h3><span>{price}</span></div></a>"
        )
    return f"""
<section class="section">
  <div class="wrap">
    <div class="section__head"><div><span class="eyebrow">À découvrir aussi</span><h2>Les autres <em>signatures</em></h2></div></div>
    <div class="others">{"".join(cards)}</div>
  </div>
</section>"""


def service_page(filename, *, title, desc, crumb, eyebrow, h1, lead, facts, hero_img, hero_alt,
                 intro_title, intro_text, steps, ba_figs, prices, care_title, care, faqs):
    facts_html = "".join(f"<div><span>{k}</span><strong>{v}</strong></div>" for k, v in facts)
    steps_html = "".join(f'<div class="step reveal"><h3>{t}</h3><p>{p}</p></div>' for t, p in steps)
    care_html = "".join(f"<li>{c}</li>" for c in care)
    body = f"""
<section class="page-hero">
  <div class="wrap page-hero__grid">
    <div>
      <p class="crumbs"><a href="index.html">Accueil</a> / {crumb}</p>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <div class="facts">{facts_html}</div>
      <div style="display:flex;gap:14px;flex-wrap:wrap">{book_btn()}<a class="btn btn--ghost" href="tarifs.html">Voir les tarifs</a></div>
    </div>
    <div class="page-hero__img"><img src="assets/img/{hero_img}" alt="{escape(hero_alt)}" fetchpriority="high"></div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap two-col">
    <div><span class="eyebrow reveal">La prestation</span><h2 class="reveal">{intro_title}</h2></div>
    <div class="reveal"><p class="lead">{intro_text}</p></div>
  </div>
  <div class="wrap" style="margin-top:clamp(56px,7vw,96px)"><div class="steps">{steps_html}</div></div>
</section>

<section class="section section--ink">
  <div class="wrap">
    <div class="section__head"><div><span class="eyebrow">Avant · Après</span><h2>Le résultat, <em>sans filtre</em></h2></div>
    <p class="lead">Des clientes du studio, photographiées juste après leur rendez-vous.</p></div>
    {ba(ba_figs)}
  </div>
</section>

<section class="section">
  <div class="wrap two-col">
    <div><span class="eyebrow reveal">Tarifs</span><h2 class="reveal">Les <em>formules</em></h2>
      <p class="reveal" style="margin-top:24px;color:var(--ink-soft)">Prix TTC. Réservation et paiement sur place, via Planity.</p></div>
    <div class="reveal">{price_rows(prices)}<p style="margin-top:32px">{book_btn("Choisir ma formule")}</p></div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap two-col">
    <div><span class="eyebrow reveal">Avant &amp; après le rendez-vous</span><h2 class="reveal">{care_title}</h2></div>
    <div class="reveal"><ul class="checklist">{care_html}</ul></div>
  </div>
</section>

<section class="section">
  <div class="wrap two-col">
    <div><span class="eyebrow reveal">Questions fréquentes</span><h2 class="reveal">Vous vous <em>demandez</em>…</h2></div>
    <div class="reveal">{faq(faqs)}</div>
  </div>
</section>
{others(filename)}
{cta()}
"""
    page(filename, title, desc, body, current=filename)


# ------------------------------------------------------------------ accueil

def build_home():
    cards = "".join(
        f'<a class="service-card reveal" href="{href}"><div class="service-card__img"><img src="assets/img/{img}" alt="{name}" loading="lazy"></div>'
        f'<span class="service-card__num">0{i}</span><h3>{name}</h3><p>{txt}</p><span class="service-card__price">{price}</span></a>'
        for i, (href, img, name, txt, price) in enumerate(SERVICES, 1)
    )
    reviews = [
        ("Première visite pour une restructuration. Fadoua est à l'écoute et minutieuse. Le résultat est parfait. Je reviendrai, merci !", "Avis Planity · septembre 2026"),
        ("L'accueil est parfait, tout comme le déroulement de la prestation. Je suis toujours ravie de ce moment de détente. Je recommande mille fois.", "Avis Planity · août 2026"),
        ("Toujours aussi bien reçue par Fadoua ! La meilleure dans son domaine. Vous ressortez avec des sourcils magnifiques.", "Avis Planity · mai 2026"),
    ]
    rev_html = "".join(
        f'<div class="review reveal"><span class="review__stars">★★★★★</span><blockquote>« {q} »</blockquote><cite>{c}</cite></div>'
        for q, c in reviews
    )
    schema = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BeautySalon","name":"Flowenchy Beauty",
"image":"assets/img/hero.jpg","telephone":"+33652771141",
"address":{{"@type":"PostalAddress","streetAddress":"27 rue de Turenne","postalCode":"75004","addressLocality":"Paris","addressCountry":"FR"}},
"geo":{{"@type":"GeoCoordinates","latitude":48.8563856,"longitude":2.3641252}},
"openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"10:00","closes":"20:00"}}],
"sameAs":["{INSTA}"],"priceRange":"€€€"}}
</script>"""
    body = f"""
<section class="hero">
  <div class="wrap hero__grid">
    <div>
      <span class="eyebrow">Studio privé · Paris 4e — Le Marais</span>
      <h1>L'art du <em>regard</em>, au cœur du Marais.</h1>
      <p class="lead">Restructuration, brow lift, lash lift et microblading sur-mesure. Un geste précis, un résultat naturel, signé Fadoua.</p>
      <div class="hero__actions">{book_btn("Prendre rendez-vous")}<a class="btn btn--ghost" href="tarifs.html">Les prestations</a></div>
      <div class="hero__proof">
        <div><strong>4,9 / 5</strong>163 avis Google</div>
        <div><strong>5,0 / 5</strong>122 avis Planity</div>
        <div><strong>12 ans</strong>d'expertise du regard</div>
      </div>
    </div>
    <div class="hero__media">
      <img src="assets/img/hero.jpg" alt="Cliente aux sourcils restructurés par Flowenchy Beauty" fetchpriority="high">
      <div class="hero__badge"><div><strong>5,0</strong><span>Accueil &amp;<br>propreté</span></div></div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap">
    <div class="section__head">
      <div><span class="eyebrow reveal">Beauté du regard</span><h2 class="reveal">Quatre <em>signatures</em>,<br>un seul regard.</h2></div>
      <p class="lead reveal">Chaque prestation commence par une analyse de votre visage. La forme se décide ensemble, jamais au hasard.</p>
    </div>
    <div class="services">{cards}</div>
  </div>
</section>

<section class="section">
  <div class="wrap editorial">
    <div class="editorial__media reveal">
      <img src="assets/img/studio-mur.jpg" alt="Le studio Flowenchy Beauty, rue de Turenne" loading="lazy">
      <img class="inset" src="assets/img/outils.jpg" alt="Pince et brosse à sourcils" loading="lazy">
    </div>
    <div class="reveal">
      <span class="eyebrow">La maison</span>
      <h2>Un studio privé, <em>pensé</em> pour vous.</h2>
      <p class="lead">À cinq minutes du métro Saint-Paul, le studio vous reçoit dans un cadre blanc et bois, calme et intime. Une seule cliente à la fois, le temps qu'il faut.</p>
      <p class="quote">« Une jolie ligne de sourcils peut transformer tout un regard. »</p>
      <a class="link" href="la-maison.html">Découvrir la maison</a>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="wrap">
    <div class="section__head">
      <div><span class="eyebrow">Avant · Après</span><h2>Le résultat parle <em>de lui-même</em>.</h2></div>
      <p class="lead">Des sourcils structurés, des cils recourbés. Un regard plus ouvert, qui reste le vôtre.</p>
    </div>
    {ba([
        ("ba-restructuration.jpg", "Avant et après une restructuration des sourcils", "Restructuration"),
        ("ba-browlift-2.jpg", "Avant et après un brow lift", "Brow lift"),
        ("ba-lashlift.jpg", "Avant et après un lash lift", "Lash lift + teinture"),
        ("ba-microblading.jpg", "Avant et après un microblading", "Microblading"),
    ])}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section__head">
      <div><span class="eyebrow reveal">Elles en parlent</span><h2 class="reveal">La confiance <em>se mérite</em>.</h2></div>
      <div class="scores reveal" style="margin-left:auto">
        <div class="score"><strong>4,9</strong><span>Google · 163 avis</span></div>
        <div class="score"><strong>5,0</strong><span>Planity · 122 avis</span></div>
      </div>
    </div>
    <div class="reviews">{rev_html}</div>
  </div>
</section>
{info_band()}
{cta()}
"""
    page("index.html",
         "Flowenchy Beauty · Brow lift, lash lift & microblading à Paris 4e",
         "Studio privé au cœur du Marais : restructuration des sourcils, brow lift, lash lift et microblading sur-mesure. 4,9/5 sur Google. Réservation en ligne 24h/24.",
         body, current="index.html", extra_head=schema)


# ------------------------------------------------------------------ prestations

def build_services():
    service_page(
        "restructuration-sourcils.html",
        title="Restructuration des sourcils à Paris 4e · Flowenchy Beauty",
        desc="Restructuration des sourcils sur-mesure dans le Marais : analyse du visage, tracé précis, épilation à la pince. Dès 50 €. Henné végétal et teinture disponibles.",
        crumb="Restructuration",
        eyebrow="Sourcils · La signature",
        h1="Restructu&shy;ration <em>des sourcils</em>",
        lead="La prestation qui a fait la réputation de Flowenchy. Une analyse de votre visage, un tracé précis et une épilation à la pince pour une ligne nette, symétrique et naturelle.",
        facts=[("Durée", "40 min"), ("À partir de", "50 €"), ("Entretien", "35 €")],
        hero_img="restructuration.jpg", hero_alt="Sourcils restructurés chez Flowenchy Beauty",
        intro_title="Une forme qui vous <em>ressemble</em>.",
        intro_text="Pensée pour une première visite ou pour redéfinir complètement vos sourcils. Le tracé suit la morphologie de votre visage : l'objectif est un sourcil plus net et plus équilibré, jamais un sourcil « fait ». Ensuite, un entretien mensuel garde la ligne parfaite.",
        steps=[
            ("Analyse", "Étude de votre visage, de vos sourcils actuels et de ce que vous aimez."),
            ("Tracé", "Le dessin de la forme idéale, validé avec vous avant toute épilation."),
            ("Épilation", "À la pince, poil par poil, pour un résultat précis et doux."),
            ("Mise en beauté", "Teinture ou henné en option, et nos conseils pour l'entretien."),
        ],
        ba_figs=[
            ("ba-restructuration.jpg", "Avant et après restructuration", "Restructuration"),
            ("ba-restructuration-2.jpg", "Avant et après restructuration", "Symétrie retrouvée"),
            ("restructuration-2.jpg", "Cliente après restructuration", "Résultat naturel"),
            ("henne.jpg", "Sourcils au henné végétal", "Henné végétal"),
        ],
        prices=[
            ("Restructuration sourcils by Flowenchy", "Première visite ou nouvelle forme complète. Analyse, tracé et mise en beauté.", "40 min", "50 €"),
            ("Entretien mensuel des sourcils", "Réservé aux clientes ayant fait une restructuration au studio il y a 1 mois maximum.", "30 min", "35 €"),
            ("Restructuration + teinture", "", "30 min", "50 €"),
            ("Regard Signature · Restructuration + henné végétal", "Teinture naturelle qui colore aussi la peau pour combler les zones clairsemées. Tenue de 4 à 6 semaines.", "50 min", "90 €", "Signature"),
            ("Teinture des sourcils", "", "10 min", "25 €"),
        ],
        care_title="Pour un résultat <em>durable</em>",
        care=[
            "Laissez pousser vos sourcils 3 à 4 semaines avant une première restructuration.",
            "Évitez le maquillage des sourcils le jour du rendez-vous.",
            "Après un henné, ne mouillez pas les sourcils pendant 24 h.",
            "Brossez vos sourcils chaque matin pour garder la ligne.",
            "Ne retouchez pas à la pince entre deux rendez-vous.",
            "Revenez toutes les 4 semaines pour l'entretien.",
        ],
        faqs=[
            ("Quelle différence entre restructuration et entretien ?", "La restructuration crée ou redéfinit entièrement la forme. L'entretien, un mois plus tard maximum, garde cette forme intacte en retirant seulement la repousse."),
            ("Est-ce douloureux ?", "L'épilation à la pince reste très supportable. Elle est plus précise que la cire et plus douce pour la peau du visage."),
            ("Combien de temps tient le henné végétal ?", "De 4 à 6 semaines sur les poils selon votre type de peau et vos habitudes de soin. Sur la peau, la coloration s'estompe plus vite."),
            ("Mes sourcils sont très clairsemés, est-ce possible ?", "Oui. Le henné comble visuellement les zones vides. Pour un effet durable, le microblading peut être une option : on en parle lors du rendez-vous."),
        ],
    )

    service_page(
        "brow-lift.html",
        title="Brow lift (lamination des sourcils) à Paris 4e · Flowenchy Beauty",
        desc="Brow lift dans le Marais : des sourcils disciplinés, fournis et brossés vers le haut, sans gel au quotidien. 90 €. Forfaits brow lift + lash lift.",
        crumb="Brow lift",
        eyebrow="Sourcils · Effet fourni",
        h1="Brow <em>lift</em>",
        lead="Aussi appelé lamination des sourcils. Les poils sont redressés et fixés dans la bonne direction pour un sourcil plus dense, soigné et élégant, sans maquillage chaque matin.",
        facts=[("Durée", "50 min"), ("Prix", "90 €"), ("Tenue", "≈ 1 mois")],
        hero_img="ba-browlift-3.jpg", hero_alt="Avant et après brow lift",
        intro_title="L'effet <em>sourcils brossés</em>, toute la journée.",
        intro_text="Le brow lift donne du volume aux sourcils fins et discipline les poils rebelles. Associé à une restructuration et une teinture, il offre un sourcil complet et harmonieux. Plus besoin de gel : la forme tient environ un mois.",
        steps=[
            ("Diagnostic", "Analyse de la densité, de la direction des poils et de la forme souhaitée."),
            ("Lift", "Application d'une lotion qui assouplit les poils pour les repositionner."),
            ("Fixation", "Les poils sont brossés et fixés dans leur nouvelle direction."),
            ("Finition", "Soin nourrissant, et restructuration ou teinture selon la formule."),
        ],
        ba_figs=[
            ("ba-browlift.jpg", "Avant et après brow lift", "Brow lift"),
            ("ba-browlift-2.jpg", "Avant et après brow lift et teinture", "Lift + teinture"),
            ("ba-browlift-3.jpg", "Avant et après brow lift et restructuration", "Lift + restructuration"),
            ("browlift.jpg", "Sourcils après brow lift", "Effet brossé"),
        ],
        prices=[
            ("Brow lift · Brow lamination", "Discipline et densifie les sourcils pour un effet fourni et soigné.", "50 min", "90 €"),
            ("Brow lift complet", "Brow lift + restructuration + teinture, pour un fini harmonieux.", "50 min", "149 €", "Le plus choisi"),
            ("Regard parfait · Brow lift + lash lift", "Cils et sourcils disciplinés dans le même rendez-vous.", "50 min", "159 €"),
            ("Regard Couture", "Lash lift + brow lift + teinture + soin kératine.", "1 h 30", "180 €"),
            ("Duo sourcils · 2 brow lifts", "Un moment beauté à deux.", "1 h 20", "149 €"),
        ],
        care_title="Les bons <em>réflexes</em>",
        care=[
            "Ne mouillez pas vos sourcils pendant 24 h.",
            "Pas de sauna, hammam ni piscine pendant 48 h.",
            "Brossez vos sourcils vers le haut chaque matin.",
            "Appliquez une huile ou un soin nourrissant le soir.",
            "Évitez les gommages sur la zone la première semaine.",
            "Espacez deux brow lifts d'au moins 6 semaines.",
        ],
        faqs=[
            ("Combien de temps dure un brow lift ?", "Environ un mois, selon la pousse de vos poils et votre routine."),
            ("Le brow lift abîme-t-il les poils ?", "Non, s'il est bien réalisé et espacé. Un soin nourrissant est appliqué en fin de séance, et la formule Regard Couture inclut un soin à la kératine."),
            ("Brow lift ou restructuration ?", "La restructuration travaille la forme. Le brow lift travaille la direction et le volume. Les deux se combinent très bien : c'est le brow lift complet."),
            ("Puis-je me maquiller ensuite ?", "Attendez 24 h avant tout produit sur les sourcils. Ensuite, la plupart des clientes n'en ont plus besoin."),
        ],
    )

    service_page(
        "rehaussement-cils.html",
        title="Lash lift (rehaussement de cils) à Paris 4e · Flowenchy Beauty",
        desc="Rehaussement de cils dans le Marais : une courbure naturelle et une teinture pour un regard ouvert, sans mascara. 90 €. Forfaits lash lift + sourcils.",
        crumb="Lash lift",
        eyebrow="Cils · Effet naturel",
        h1="Lash <em>lift</em>",
        lead="Le rehaussement de cils donne à vos cils naturels une courbure parfaite. Associé à une teinture, il intensifie le regard comme un mascara, sans en porter.",
        facts=[("Durée", "50 min"), ("Prix", "90 €"), ("Teinture", "+ 25 €")],
        hero_img="lashlift.jpg", hero_alt="Cils recourbés après lash lift",
        intro_title="Adieu le <em>recourbe-cils</em>.",
        intro_text="Les cils sont relevés dès la racine pour ouvrir l'œil et allonger visuellement le regard. Le résultat est naturel, lumineux, et vous oubliez le recourbe-cils pendant environ un mois. Idéal avant les vacances ou un événement.",
        steps=[
            ("Préparation", "Nettoyage des cils et choix du bigoudi adapté à leur longueur."),
            ("Rehaussement", "Les cils sont posés sur le bigoudi et relevés à la racine."),
            ("Fixation", "La courbure est fixée, en douceur, pour un effet naturel."),
            ("Teinture", "En option, pour un effet mascara et plus de profondeur."),
        ],
        ba_figs=[
            ("ba-lashlift.jpg", "Avant et après lash lift", "Lash lift + teinture"),
            ("lashlift-2.jpg", "Cliente après lash lift", "Regard ouvert"),
            ("lashlift-3.jpg", "Cliente après lash lift", "Effet naturel"),
            ("lashlift.jpg", "Cils recourbés en gros plan", "Courbure parfaite"),
        ],
        prices=[
            ("Lash lift", "Courbure parfaite et naturelle des cils pour un regard intensifié et lumineux.", "50 min", "90 €"),
            ("Teinture des cils", "Intensité et profondeur, effet mascara naturel.", "10 min", "25 €"),
            ("Cils sublimes · Lash lift + restructuration", "Courbure des cils et restructuration des sourcils associées.", "1 h", "120 €", "Le plus choisi"),
            ("Regard parfait · Lash lift + brow lift", "", "50 min", "159 €"),
            ("Duo cils · 2 lash lifts", "Un rehaussement à deux, pour un regard sublimé en duo.", "1 h 20", "149 €"),
        ],
        care_title="Pour une courbure <em>qui dure</em>",
        care=[
            "Venez sans mascara ni lentilles de contact.",
            "Un soin pousse-cils les semaines d'avant donne un plus bel effet.",
            "Ne mouillez pas les cils pendant 24 h.",
            "Pas de mascara waterproof ni de démaquillant gras pendant 48 h.",
            "Évitez de dormir sur le visage la première nuit.",
            "Espacez deux lash lifts d'au moins 6 semaines.",
        ],
        faqs=[
            ("Combien de temps tient un lash lift ?", "Environ un mois, au rythme du renouvellement naturel de vos cils."),
            ("Est-ce adapté aux cils courts ?", "Oui. Le bigoudi est choisi selon la longueur de vos cils, et la teinture leur donne plus de présence."),
            ("Lash lift ou extensions ?", "Le lash lift travaille vos propres cils : pas d'entretien, pas de colle, un effet naturel. Les extensions ajoutent de la longueur artificielle."),
            ("Puis-je porter du mascara ensuite ?", "Oui, après 48 h. Mais la plupart des clientes n'en ressentent plus le besoin."),
        ],
    )

    service_page(
        "microblading.html",
        title="Microblading sur-mesure à Paris 4e · Flowenchy Beauty",
        desc="Microblading naturel dans le Marais : des poils dessinés un à un pour des sourcils restructurés et durables. 450 €, retouche fixatrice à 3–4 semaines.",
        crumb="Microblading",
        eyebrow="Sourcils · Longue tenue",
        h1="Micro&shy;blading <em>sur-mesure</em>",
        lead="Une pigmentation fine et précise qui imite le poil. Pour combler des sourcils clairsemés, corriger une asymétrie ou ne plus jamais les dessiner le matin.",
        facts=[("Durée", "1 h 20"), ("Prix", "450 €"), ("Retouche", "3–4 sem.")],
        hero_img="portrait-boucles.jpg", hero_alt="Cliente après microblading",
        intro_title="Des poils dessinés <em>un à un</em>.",
        intro_text="Le microblading dépose le pigment en traits très fins, dans le sens naturel de la pousse. Le résultat est structuré mais reste crédible de près. Une retouche fixatrice 3 à 4 semaines plus tard fixe et prolonge le résultat, puis une retouche tous les 6 à 12 mois ravive la couleur.",
        steps=[
            ("Consultation", "Forme, couleur du pigment et attentes : tout est décidé ensemble."),
            ("Tracé", "Le dessin des sourcils est réalisé et validé avant de commencer."),
            ("Pigmentation", "Les poils sont tracés un à un, avec un pigment adapté à votre carnation."),
            ("Retouche", "3 à 4 semaines après, pour fixer et parfaire le résultat."),
        ],
        ba_figs=[
            ("ba-microblading.jpg", "Avant et après microblading", "Microblading"),
            ("ba-microblading-2.jpg", "Avant et après microblading", "Densité retrouvée"),
            ("microblading.jpg", "Sourcils après microblading", "Après la séance"),
            ("atelier-microblading.jpg", "Séance de microblading au studio", "Au studio"),
        ],
        prices=[
            ("Microblading sur-mesure", "Pigmentation fine qui imite le poil, pour des sourcils restructurés et naturels.", "1 h 20", "450 €"),
            ("1re retouche fixatrice", "3 à 4 semaines après la première séance, pour fixer et prolonger le résultat.", "1 h", "180 €"),
            ("Retouche d'entretien (6 mois – 1 an)", "Ravive la couleur et la netteté des sourcils.", "1 h", "195 €"),
        ],
        care_title="Une cicatrisation <em>soignée</em>",
        care=[
            "Pas d'alcool ni d'anticoagulant (aspirine) 24 h avant.",
            "Ne mouillez pas les sourcils pendant 7 jours.",
            "Appliquez le baume conseillé, en couche fine.",
            "Ne grattez pas les petites croûtes : elles tombent seules.",
            "Pas de soleil, sauna ni piscine pendant 2 semaines.",
            "La couleur paraît plus foncée au début : c'est normal.",
        ],
        faqs=[
            ("Combien de temps dure un microblading ?", "Le résultat s'estompe progressivement. Une retouche tous les 6 à 12 mois garde des sourcils nets, selon votre peau et votre exposition au soleil."),
            ("Le résultat est-il naturel ?", "Oui, c'est tout l'intérêt de la technique poil à poil. La forme et la couleur sont choisies pour vous, jamais copiées d'une tendance."),
            ("La retouche est-elle obligatoire ?", "Elle est fortement recommandée. Certaines zones retiennent moins le pigment pendant la cicatrisation, la retouche les complète."),
            ("Y a-t-il des contre-indications ?", "Oui, par exemple grossesse, allaitement, certains traitements ou problèmes de peau sur la zone. Parlez-en avant de réserver : un avis est donné au cas par cas."),
        ],
    )


# ------------------------------------------------------------------ tarifs

def build_prices():
    groups = [
        ("Beauté du regard", "Sourcils &amp; <em>cils</em>",
         "Chaque service est pensé sur-mesure pour révéler l'élégance naturelle de vos sourcils et de vos cils.", [
            ("Restructuration sourcils by Flowenchy", "Première visite ou nouvelle forme. Analyse, tracé précis et mise en beauté.", "40 min", "50 €"),
            ("Entretien mensuel des sourcils", "Après une restructuration au studio, 1 mois maximum.", "30 min", "35 €"),
            ("Restructuration + teinture", "", "30 min", "50 €"),
            ("Restructuration + henné végétal", "Colore et densifie. Tenue de 4 à 6 semaines.", "50 min", "90 €"),
            ("Brow lift · Brow lamination", "Discipline et densifie, sans maquillage au quotidien.", "50 min", "90 €"),
            ("Lash lift", "Courbure parfaite et naturelle des cils.", "50 min", "90 €"),
            ("Teinture des cils", "", "10 min", "25 €"),
            ("Teinture des sourcils", "", "10 min", "25 €"),
            ("Microblading sur-mesure", "Pigmentation fine qui imite le poil.", "1 h 20", "450 €"),
            ("Microblading · 1re retouche fixatrice", "3 à 4 semaines après la première séance.", "1 h", "180 €"),
            ("Microblading · retouche 6 mois à 1 an", "", "1 h", "195 €"),
        ]),
        ("Forfaits exclusifs", "Les <em>combinaisons</em>",
         "Des formules pensées pour une expérience complète et un résultat harmonieux.", [
            ("Regard Signature · Restructuration + henné", "Restructuration complète et teinture naturelle durable.", "50 min", "90 €"),
            ("Cils sublimes · Lash lift + restructuration", "", "1 h", "120 €"),
            ("Brow lift complet", "Brow lift + restructuration + teinture.", "50 min", "149 €"),
            ("Regard parfait · Brow lift + lash lift", "", "50 min", "159 €"),
            ("Regard Couture", "Lash lift + brow lift + teinture + soin kératine.", "1 h 30", "180 €", "Signature"),
            ("Duo cils · 2 lash lifts", "", "1 h 20", "149 €"),
            ("Duo sourcils · 2 brow lifts", "", "1 h 20", "149 €"),
        ]),
        ("Maquillage &amp; mariage", "Mise en <em>beauté</em>",
         "Du maquillage événementiel à la mariée : une mise en beauté raffinée, lumineuse et longue tenue.", [
            ("Make-up invitée · soirée · événement · shooting", "Déplacement possible sur devis.", "1 h", "120 €"),
            ("Essai maquillage mariée", "Séance personnalisée pour définir le maquillage du jour J.", "1 h 30", "Sur devis"),
            ("Maquillage mariée", "", "1 h 30", "Sur devis"),
            ("Forfait mariage jour J · makeup + coiffure", "", "2 h", "400 €"),
            ("Cours d'auto-maquillage individuel", "Pensez à apporter vos pinceaux.", "1 h", "150 €"),
            ("Cours d'auto-maquillage en duo", "", "1 h 20", "250 €"),
            ("Cours d'auto-maquillage en groupe", "EVJF, anniversaire, entreprise.", "3 h 20", "Sur devis"),
        ]),
        ("Formations", "Transmettre <em>l'excellence</em>",
         "Des formations individuelles pour débutantes et professionnelles, avec pratique guidée.", [
            ("Brow artist · spécial brow lift", "Toutes les techniques du brow lift, pratique guidée.", "5 h", "354 €"),
            ("Brow lift + teinture + restructuration · intensive", "Programme complet avec pratique sur modèles.", "6 h 40", "850 €"),
            ("Makeup artist · 1 jour", "Les bases du maquillage professionnel.", "6 h 40", "550 €"),
            ("Makeup artist · intensive 4 jours", "Techniques avancées, programme personnalisé.", "13 h 20", "850 €"),
        ]),
    ]
    blocks = "".join(
        f'<div class="price-group reveal"><div class="price-group__head"><div><span class="eyebrow">{eb}</span><h2>{h}</h2></div><p>{p}</p></div>{price_rows(rows)}</div>'
        for eb, h, p, rows in groups
    )
    body = f"""
<section class="page-hero">
  <div class="wrap page-hero__grid">
    <div>
      <p class="crumbs"><a href="index.html">Accueil</a> / Tarifs</p>
      <span class="eyebrow">La carte</span>
      <h1>Les <em>tarifs</em></h1>
      <p class="lead">Toutes les prestations du studio, du simple entretien au forfait complet. Prix TTC, réservation en ligne 24h/24.</p>
      <div style="margin-top:36px">{book_btn()}</div>
    </div>
    <div class="page-hero__img"><img src="assets/img/studio-lampe.jpg" alt="Le studio Flowenchy Beauty" fetchpriority="high"></div>
  </div>
</section>
<section class="section section--paper">
  <div class="wrap">{blocks}
    <p style="color:var(--ink-soft);font-size:14px">Devis maquillage et mariage : <a class="link" href="{PHONE_LINK}">{PHONE}</a></p>
  </div>
</section>
{cta()}
"""
    page("tarifs.html", "Tarifs · Flowenchy Beauty, Paris 4e",
         "Tous les tarifs Flowenchy Beauty : restructuration dès 50 €, brow lift et lash lift 90 €, microblading 450 €, forfaits, maquillage et formations.",
         body, current="tarifs.html")


# ------------------------------------------------------------------ la maison

def build_about():
    body = f"""
<section class="page-hero">
  <div class="wrap page-hero__grid">
    <div>
      <p class="crumbs"><a href="index.html">Accueil</a> / La maison</p>
      <span class="eyebrow">Depuis plus de 12 ans</span>
      <h1>La <em>maison</em> Flowenchy</h1>
      <p class="lead">Derrière Flowenchy, il y a Fadoua. Elle commence dans la beauté à 18 ans et fait du regard sa spécialité. Aujourd'hui, elle reçoit ses clientes dans son studio privé du Marais.</p>
    </div>
    <div class="page-hero__img"><img src="assets/img/atelier-soin.jpg" alt="Fadoua au travail dans le studio" fetchpriority="high"></div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap editorial editorial--flip">
    <div class="editorial__media reveal">
      <img src="assets/img/studio-lampe.jpg" alt="Le studio Flowenchy Beauty" loading="lazy">
    </div>
    <div class="reveal">
      <span class="eyebrow">L'histoire</span>
      <h2>Du premier geste <em>au studio</em>.</h2>
      <p class="lead">« Quand j'ai commencé à 18 ans, j'étais complètement perdue. » Plus de dix ans plus tard, Fadoua a trouvé ce qui compte : prendre le temps, écouter, et révéler un regard plutôt que le transformer.</p>
      <p>Restructuration, brow lift, lash lift, microblading, mais aussi maquillage et formations : tout ce qui touche au regard passe par ses mains. Avec la même règle à chaque rendez-vous : un résultat qui vous ressemble.</p>
      <p class="quote">« Rien de plus gratifiant que de voir mes clientes repartir avec le sourire. »</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section__head"><div><span class="eyebrow reveal">Nos engagements</span><h2 class="reveal">Ce qui fait <em>la différence</em></h2></div></div>
    <div class="values">
      <div class="reveal"><span class="roman">i.</span><h3>Le sur-mesure</h3><p>Chaque forme part de votre visage. Le tracé est validé avec vous, toujours avant le premier geste.</p></div>
      <div class="reveal"><span class="roman">ii.</span><h3>Le naturel</h3><p>Des sourcils et des cils qui restent les vôtres, en mieux. Henné 100 % végétal, pigments adaptés à votre carnation.</p></div>
      <div class="reveal"><span class="roman">iii.</span><h3>Le temps</h3><p>Une cliente à la fois, dans un studio privé. Pas de chaîne, pas de précipitation.</p></div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap">
    <div class="section__head"><div><span class="eyebrow reveal">Le studio</span><h2 class="reveal">27, rue de <em>Turenne</em></h2></div>
      <p class="lead reveal">Un cocon blanc et bois au cœur du Marais, à cinq minutes à pied du métro Saint-Paul.</p></div>
    <div class="mosaic reveal">
      <img class="m1" src="assets/img/studio-mur.jpg" alt="Le mur Flowenchy du studio" loading="lazy">
      <img class="m2" src="assets/img/carte.jpg" alt="Carte de visite Flowenchy" loading="lazy">
      <img class="m3" src="assets/img/outils.jpg" alt="Outils de restructuration" loading="lazy">
      <img class="m4" src="assets/img/atelier-geste.jpg" alt="Prestation en cours au studio" loading="lazy">
      <img class="m5" src="assets/img/soin.jpg" alt="Cliente pendant un soin des sourcils" loading="lazy">
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="wrap editorial">
    <div class="editorial__media reveal"><img src="assets/img/maquillage.jpg" alt="Maquillage signé Flowenchy" loading="lazy"></div>
    <div class="reveal">
      <span class="eyebrow">Au-delà du regard</span>
      <h2>Maquillage, mariage <em>&amp; formations</em>.</h2>
      <p class="lead">Mise en beauté pour vos événements, maquillage de la mariée, cours d'auto-maquillage et formations professionnelles au brow lift et au maquillage.</p>
      <p style="margin-top:30px"><a class="btn btn--light" href="tarifs.html">Voir la carte {arrow()}</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap two-col">
    <div><span class="eyebrow reveal">Fidélité</span><h2 class="reveal">La carte de <em>fidélité</em></h2></div>
    <div class="reveal"><p class="lead">Vos visites sont récompensées. Demandez votre carte de fidélité lors de votre prochain rendez-vous au studio.</p></div>
  </div>
</section>
{cta()}
"""
    page("la-maison.html", "La maison · Fadoua & le studio Flowenchy Beauty",
         "Flowenchy Beauty, c'est Fadoua : plus de 12 ans d'expertise du regard et un studio privé au 27 rue de Turenne, Paris 4e.",
         body, current="la-maison.html")


# ------------------------------------------------------------------ contact

def build_contact():
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Accueil</a> / Contact</p>
    <span class="eyebrow">Nous trouver</span>
    <h1>Venir <em>au studio</em></h1>
  </div>
</section>
<section class="section section--paper" style="padding-top:clamp(56px,6vw,90px)">
  <div class="wrap contact-grid">
    <div>
      <div class="contact-block"><h4>Adresse</h4><p>{ADDRESS}</p><p class="note">Le Marais · Métro Saint-Paul (ligne 1), à 5 minutes à pied.</p></div>
      <div class="contact-block"><h4>Horaires</h4><ul class="hours" style="font-family:var(--serif)">{hours_list()}</ul><p class="note">Uniquement sur rendez-vous.</p></div>
      <div class="contact-block"><h4>Téléphone</h4><p><a href="{PHONE_LINK}">{PHONE}</a></p><p class="note">Pour les devis maquillage, mariage et formations.</p></div>
      <div class="contact-block"><h4>Instagram</h4><p><a href="{INSTA}" target="_blank" rel="noopener">@flowenchybeauty</a></p></div>
      <div style="margin-top:36px;display:flex;gap:14px;flex-wrap:wrap">{book_btn("Réserver sur Planity")}<a class="btn btn--ghost" href="{MAPS}" target="_blank" rel="noopener">Itinéraire</a></div>
    </div>
    <iframe class="map" title="Plan d'accès au studio Flowenchy Beauty" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://www.google.com/maps?q=Flowenchy+Beauty,+27+Rue+de+Turenne,+75004+Paris&amp;z=16&amp;output=embed"></iframe>
  </div>
</section>
{cta("À très vite <em>rue de Turenne</em>.")}
"""
    page("contact.html", "Contact & accès · Flowenchy Beauty, 27 rue de Turenne, Paris 4e",
         "Flowenchy Beauty, 27 rue de Turenne, 75004 Paris. Métro Saint-Paul. Ouvert du lundi au samedi, 10h–20h, sur rendez-vous.",
         body, current="contact.html")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    build_home()
    build_services()
    build_prices()
    build_about()
    build_contact()
    print("Pages générées :", ", ".join(sorted(p.name for p in OUT.glob("*.html"))))
