#!/usr/bin/env python3
# ================================================
#       FRANKTOOL  v3.0 — MAX EDITION
#         by shizzafrank | nullstate
#   OSINT: username · teléfono · DNI · CVU · email
# ================================================

import sys
import time
import re
import requests
from urllib.parse import quote

# pip install requests phonenumbers
try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone as pn_timezone
    PHONENUMBERS_OK = True
except ImportError:
    PHONENUMBERS_OK = False

# ── COLORES ────────────────────────────────────
G     = "\033[92m"
C     = "\033[96m"
Y     = "\033[93m"
R     = "\033[91m"
W     = "\033[97m"
DIM   = "\033[2m"
BOLD  = "\033[1m"
RESET = "\033[0m"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    )
}

# ── BANNER ─────────────────────────────────────
def banner():
    print(f"""
{G}  ███████╗██████╗  █████╗ ███╗   ██╗██╗  ██╗
{G}  ██╔════╝██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
{C}  █████╗  ██████╔╝███████║██╔██╗ ██║█████╔╝
{C}  ██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗
{G}  ██║     ██║  ██║██║  ██║██║ ╚████║██║  ██╗
{G}  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
{C}     T O O L  v3.0  --  by shizzafrank{RESET}
{DIM}  OSINT · Username · Teléfono · DNI · CVU · Email{RESET}
{G}  ================================================{RESET}
""")

# ── SPINNER ─────────────────────────────────────
def spinner(msg, duration=0.6):
    frames = ["[>  ]","[>> ]","[>>>]","[ >>]","[  >]","[   ]"]
    end_t = time.time() + duration
    i = 0
    while time.time() < end_t:
        print(f"\r{DIM}  {frames[i%len(frames)]}  {msg}{RESET}", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print(f"\r{G}  [OK] {msg}{RESET}              ")

def section(title):
    bar = "-" * (len(title) + 4)
    print(f"\n{G}  +{bar}+{RESET}")
    print(f"{G}  |  {W}{BOLD}{title}{RESET}{G}  |{RESET}")
    print(f"{G}  +{bar}+{RESET}\n")

def hit(label, value):
    print(f"  {G}[+]{RESET} {BOLD}{W}{label:<22}{RESET} {G}{value}{RESET}")

def info(label, value):
    print(f"  {C}[i]{RESET} {C}{label:<22}{RESET} {W}{value}{RESET}")

def miss(label):
    print(f"  {R}[-]{RESET} {DIM}{label:<22} no encontrado{RESET}")

def warn(label, value):
    print(f"  {Y}[?]{RESET} {DIM}{label:<22} {value}{RESET}")

def dork_line(label, url):
    print(f"  {Y}[D]{RESET} {W}{label:<26}{RESET}\n      {DIM}{url}{RESET}\n")

# ════════════════════════════════════════════════
#  MÓDULO 1 — USERNAME HUNT
# ════════════════════════════════════════════════
SOCIAL_SITES = {
    "Instagram"       : "https://www.instagram.com/{}/",
    "Twitter/X"       : "https://x.com/{}",
    "TikTok"          : "https://www.tiktok.com/@{}",
    "Facebook"        : "https://www.facebook.com/{}",
    "LinkedIn"        : "https://www.linkedin.com/in/{}/",
    "YouTube"         : "https://www.youtube.com/@{}",
    "Pinterest"       : "https://www.pinterest.com/{}/",
    "Snapchat"        : "https://www.snapchat.com/add/{}",
    "BeReal"          : "https://bere.al/{}",
    "Threads"         : "https://www.threads.net/@{}",
    "Mastodon"        : "https://mastodon.social/@{}",
    "Steam"           : "https://steamcommunity.com/id/{}",
    "Twitch"          : "https://www.twitch.tv/{}",
    "Xbox"            : "https://account.xbox.com/en-US/profile?gamertag={}",
    "Roblox"          : "https://www.roblox.com/user.aspx?username={}",
    "Chess.com"       : "https://www.chess.com/member/{}",
    "GitHub"          : "https://github.com/{}",
    "GitLab"          : "https://gitlab.com/{}",
    "Replit"          : "https://replit.com/@{}",
    "Codepen"         : "https://codepen.io/{}",
    "Dev.to"          : "https://dev.to/{}",
    "HackerNews"      : "https://news.ycombinator.com/user?id={}",
    "HackerOne"       : "https://hackerone.com/{}",
    "Leetcode"        : "https://leetcode.com/{}",
    "SoundCloud"      : "https://soundcloud.com/{}",
    "Spotify"         : "https://open.spotify.com/user/{}",
    "Bandcamp"        : "https://{}.bandcamp.com",
    "Mixcloud"        : "https://www.mixcloud.com/{}/",
    "DeviantArt"      : "https://www.deviantart.com/{}",
    "Behance"         : "https://www.behance.net/{}",
    "ArtStation"      : "https://www.artstation.com/{}",
    "Tumblr"          : "https://{}.tumblr.com",
    "Medium"          : "https://medium.com/@{}",
    "Substack"        : "https://{}.substack.com",
    "Reddit"          : "https://www.reddit.com/user/{}",
    "Telegram"        : "https://t.me/{}",
    "Discord"         : "https://discord.com/users/{}",
    "Patreon"         : "https://www.patreon.com/{}",
    "OnlyFans"        : "https://onlyfans.com/{}",
    "Ko-fi"           : "https://ko-fi.com/{}",
    "Linktree"        : "https://linktr.ee/{}",
    "About.me"        : "https://about.me/{}",
    "Fiverr"          : "https://www.fiverr.com/{}",
    "ProductHunt"     : "https://www.producthunt.com/@{}",
    "Poshmark"        : "https://poshmark.com/closet/{}",
    "Gravatar"        : "https://en.gravatar.com/{}",
}

FALSE_POSITIVES = [
    "page not found","user not found","this account doesn't exist",
    "profile not found","doesn't exist","no existe","sorry, this page",
    "isn't available","no encontrado",
]

def check_username(handle):
    section(f"USERNAME HUNT  >  @{handle}")
    found = []
    total = len(SOCIAL_SITES)
    for i, (platform, url_tpl) in enumerate(SOCIAL_SITES.items(), 1):
        url = url_tpl.format(handle)
        spinner(f"[{i}/{total}] {platform}", 0.4)
        try:
            r = requests.get(url, headers=HEADERS, timeout=7, allow_redirects=True)
            if r.status_code == 200:
                body = r.text.lower()
                if any(kw in body for kw in FALSE_POSITIVES):
                    miss(platform)
                else:
                    hit(platform, url)
                    found.append((platform, url))
            elif r.status_code == 404:
                miss(platform)
            else:
                warn(platform, f"STATUS {r.status_code}")
        except:
            print(f"  {DIM}[!] {platform:<22} timeout{RESET}")

    print(f"\n{G}  ================================================{RESET}")
    print(f"  {G}[+] Encontrado en {BOLD}{len(found)}{RESET}{G} / {total} plataformas{RESET}")
    print(f"{G}  ================================================{RESET}\n")
    if found:
        print(f"{G}  == RESUMEN HITS =={RESET}")
        for p, u in found:
            print(f"  {G}>>>{RESET} {W}{p:<20}{RESET} {DIM}{u}{RESET}")
    return found

# ════════════════════════════════════════════════
#  MÓDULO 2 — TELÉFONO
# ════════════════════════════════════════════════
CVU_ENTITIES = {
    "0000003": "Mercado Pago",
    "0000007": "Ualá",
    "0000014": "Brubank",
    "0000015": "Naranja X",
    "0000025": "Personal Pay",
    "0000026": "Modo",
    "0000072": "Banco Galicia",
    "0000011": "Banco Nación",
    "0000017": "BBVA Argentina",
    "0000034": "Santander Argentina",
}

def lookup_telefono(numero):
    section(f"TELÉFONO LOOKUP  >  {numero}")

    # limpiar número
    numero_limpio = re.sub(r"[^\d+]", "", numero)
    if not numero_limpio.startswith("+"):
        numero_limpio = "+54" + numero_limpio.lstrip("0")

    # phonenumbers
    if PHONENUMBERS_OK:
        spinner("Analizando con phonenumbers...", 0.8)
        try:
            parsed = phonenumbers.parse(numero_limpio)
            valido = phonenumbers.is_valid_number(parsed)
            region  = geocoder.description_for_number(parsed, "es")
            operadora = carrier.name_for_number(parsed, "es")
            zonas   = list(pn_timezone.time_zones_for_number(parsed))
            fmt_int = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            fmt_nac = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)

            info("Número internacional", fmt_int)
            info("Número nacional",      fmt_nac)
            info("Válido",               str(valido))
            info("Región / Ciudad",      region or "Desconocida")
            info("Operadora",            operadora or "Desconocida")
            info("Zona horaria",         ", ".join(zonas) if zonas else "Desconocida")
            info("Tipo de línea",        str(phonenumbers.number_type(parsed)))
        except Exception as e:
            warn("phonenumbers", f"Error: {e}")
    else:
        warn("phonenumbers", "No instalado — corré: pip install phonenumbers")

    # Numverify (API gratuita 250 req/mes)
    print(f"\n  {Y}[API]{RESET} {W}Numverify{RESET} {DIM}(necesita key gratis de numverify.com){RESET}")
    print(f"  {DIM}  -> Registro gratis en: https://numverify.com/{RESET}")
    print(f"  {DIM}  -> Devuelve: operadora, tipo línea, geolocalización{RESET}")

    # Google Dorks de teléfono
    spinner("Generando dorks de teléfono...", 0.6)
    num_plain = re.sub(r"[^\d]", "", numero)
    print(f"\n{G}  == Google Dorks — Teléfono =={RESET}\n")
    tel_dorks = [
        ("WhatsApp link directo",   f"https://wa.me/549{num_plain}"),
        ("Buscar en Google",        f"https://www.google.com/search?q={quote(num_plain)}+Argentina"),
        ("MercadoLibre vendedor",   f"https://www.google.com/search?q={quote(num_plain)}+site:mercadolibre.com.ar"),
        ("Facebook / grupos",       f"https://www.google.com/search?q={quote(num_plain)}+site:facebook.com"),
        ("OLX / clasificados",      f"https://www.google.com/search?q={quote(num_plain)}+site:olx.com.ar"),
        ("Telegram canales",        f"https://www.google.com/search?q={quote(num_plain)}+site:t.me"),
        ("Foros / communidades",    f"https://www.google.com/search?q={quote(num_plain)}+Argentina+foro"),
        ("TrueCaller búsqueda",     f"https://www.truecaller.com/search/ar/{num_plain}"),
        ("NumLookup",               f"https://www.numlookup.com/{num_plain}"),
        ("PhoneInfoga dork",        f"https://www.google.com/search?q=%2B54{num_plain}+OR+%220{num_plain}%22"),
    ]
    for label, url in tel_dorks:
        dork_line(label, url)

# ════════════════════════════════════════════════
#  MÓDULO 3 — DNI
# ════════════════════════════════════════════════
def lookup_dni(dni, sexo=""):
    section(f"DNI LOOKUP  >  {dni}  {sexo}")

    spinner("Construyendo búsqueda por DNI...", 0.8)

    # Formato limpio
    dni_limpio = re.sub(r"[^\d]", "", dni)

    print(f"\n{G}  == Información del DNI =={RESET}\n")
    info("DNI ingresado",  dni_limpio)
    info("Dígitos",        str(len(dni_limpio)))

    # Rangos aproximados por generación
    dni_int = int(dni_limpio) if dni_limpio.isdigit() else 0
    if   dni_int < 4_000_000:
        rango = "Nacido aprox. antes de 1950"
    elif dni_int < 8_000_000:
        rango = "Nacido aprox. 1950-1965"
    elif dni_int < 14_000_000:
        rango = "Nacido aprox. 1965-1975"
    elif dni_int < 20_000_000:
        rango = "Nacido aprox. 1975-1983"
    elif dni_int < 28_000_000:
        rango = "Nacido aprox. 1983-1993"
    elif dni_int < 38_000_000:
        rango = "Nacido aprox. 1993-2003"
    elif dni_int < 50_000_000:
        rango = "Nacido aprox. 2003-2015"
    else:
        rango = "Nacido aprox. 2015+"
    info("Estimación de edad", rango)
    if sexo:
        info("Sexo declarado", sexo.upper())

    # Dorks
    print(f"\n{G}  == Google Dorks — DNI =={RESET}\n")
    dni_dorks = [
        ("Dateas AR (DNI)",         f"https://www.dateas.com/es/persona/{dni_limpio}"),
        ("AFIP CUIT por DNI",       f"https://www.google.com/search?q=CUIT+{dni_limpio}+AFIP+Argentina"),
        ("BCRA deudores",           f"https://www.bcra.gob.ar/BCRAyVos/Sitio_CentralDeDeudores.asp"),
        ("NOSIS (empresa)",         f"https://www.nosis.com/es/BusquedaPersonas/Busqueda?criteria={dni_limpio}"),
        ("Infobae / noticias",      f"https://www.google.com/search?q={dni_limpio}+site:infobae.com"),
        ("Clarin / noticias",       f"https://www.google.com/search?q={dni_limpio}+site:clarin.com"),
        ("MercadoLibre perfil",     f"https://www.google.com/search?q={dni_limpio}+site:mercadolibre.com.ar"),
        ("Documentos públicos",     f"https://www.google.com/search?q={dni_limpio}+filetype:pdf+Argentina"),
        ("Redes sociales",          f"https://www.google.com/search?q={dni_limpio}+Argentina+Instagram+OR+Facebook"),
        ("Boletín Oficial",         f"https://www.google.com/search?q={dni_limpio}+site:boletinoficial.gob.ar"),
        ("ANSES consulta",          f"https://www.anses.gob.ar/consulta/constancia-de-cuil"),
        ("Registro Automotor",      f"https://www.dnrpa.gov.ar/portal_dnrpa/"),
        ("Inhabilitados BCRA",      f"https://www.bcra.gob.ar/SistemasFinancieros/FinanciamientoSF.asp"),
    ]
    for label, url in dni_dorks:
        dork_line(label, url)

    # CUIL aproximado
    if sexo.upper() in ("M", "MASCULINO"):
        prefijo = "20"
    elif sexo.upper() in ("F", "FEMENINO"):
        prefijo = "27"
    else:
        prefijo = "20 o 27"

    print(f"  {C}[i]{RESET} {C}CUIL estimado:{RESET}  {W}{prefijo}-{dni_limpio}-?{RESET} {DIM}(verificar dígito verificador){RESET}\n")

# ════════════════════════════════════════════════
#  MÓDULO 4 — CVU / ALIAS MERCADO PAGO
# ════════════════════════════════════════════════
def lookup_cvu(cvu_o_alias):
    section(f"CVU / ALIAS MP  >  {cvu_o_alias}")

    cvu_limpio = re.sub(r"[^\d]", "", cvu_o_alias)
    es_cvu = len(cvu_limpio) == 22 and cvu_limpio.isdigit()
    es_alias = not es_cvu and len(cvu_o_alias) > 4

    if es_cvu:
        spinner("Validando CVU...", 0.7)
        info("Longitud",  f"{len(cvu_limpio)} dígitos (correcto)")
        info("Tipo",      "CVU (Clave Virtual Uniforme)")

        # prefijo → entidad
        prefijo = cvu_limpio[3:10]
        entidad = CVU_ENTITIES.get(prefijo, "Entidad desconocida")
        info("Prefijo banco/fintech", prefijo)
        hit("Entidad detectada",     entidad)

        # segmento del CBU/CVU
        info("Primeros 8 dígitos",   cvu_limpio[:8])
        info("Número de cuenta",     cvu_limpio[8:])

    elif es_alias:
        spinner("Procesando alias...", 0.5)
        info("Tipo",  "Alias (texto)")
        info("Alias", cvu_o_alias)

        # parseo de alias tipo nombre.apellido.mp
        partes = cvu_o_alias.replace("-",".")
        palabras = partes.split(".")
        palabras_filtradas = [p for p in palabras if p.lower() not in ("mp","ag","bk","nb","pp","ux","ml")]
        if palabras_filtradas:
            posible_nombre = " ".join(palabras_filtradas).title()
            hit("Posible nombre del titular", posible_nombre)

    else:
        warn("Formato", "No es CVU (22 dígitos) ni alias válido")

    # Dorks CVU / Alias
    spinner("Generando dorks de CVU/Alias...", 0.6)
    print(f"\n{G}  == Google Dorks — CVU / Alias =={RESET}\n")

    termino = cvu_o_alias
    cvu_dorks = [
        ("Buscar CVU/alias en Google",    f"https://www.google.com/search?q={quote(termino)}+Argentina"),
        ("MercadoLibre (vendedor)",       f"https://www.google.com/search?q={quote(termino)}+site:mercadolibre.com.ar"),
        ("Facebook grupos de ventas",     f"https://www.google.com/search?q={quote(termino)}+site:facebook.com"),
        ("OLX / clasificados AR",         f"https://www.google.com/search?q={quote(termino)}+site:olx.com.ar"),
        ("Foros / pagos AR",              f"https://www.google.com/search?q={quote(termino)}+pago+Argentina"),
        ("Instagram cobros",              f"https://www.google.com/search?q={quote(termino)}+site:instagram.com"),
        ("Twitter/X cobros",              f"https://www.google.com/search?q={quote(termino)}+site:x.com"),
        ("Búsqueda general redes",        f"https://www.google.com/search?q={quote(termino)}+mercadopago"),
    ]
    for label, url in cvu_dorks:
        dork_line(label, url)

# ════════════════════════════════════════════════
#  MÓDULO 5 — EMAIL
# ════════════════════════════════════════════════
def lookup_email(email):
    section(f"EMAIL LOOKUP  >  {email}")
    spinner("Analizando email...", 0.6)

    dominio = email.split("@")[-1] if "@" in email else ""
    usuario = email.split("@")[0]  if "@" in email else email

    info("Usuario",  usuario)
    info("Dominio",  dominio)

    # Gravatar check (hash MD5)
    import hashlib
    gravatar_hash = hashlib.md5(email.strip().lower().encode()).hexdigest()
    gravatar_url  = f"https://www.gravatar.com/avatar/{gravatar_hash}?d=404"
    spinner("Chequeando Gravatar...", 0.5)
    try:
        r = requests.get(gravatar_url, timeout=5)
        if r.status_code == 200:
            hit("Gravatar", f"https://www.gravatar.com/{gravatar_hash}")
        else:
            miss("Gravatar")
    except:
        warn("Gravatar", "timeout")

    # HaveIBeenPwned
    print(f"\n  {Y}[API]{RESET} {W}HaveIBeenPwned{RESET}")
    hibp_url = f"https://haveibeenpwned.com/account/{quote(email)}"
    info("Revisar manualmente", hibp_url)
    info("API HIBP",            "https://haveibeenpwned.com/API/v3 (key gratuita)")

    # Dorks email
    print(f"\n{G}  == Google Dorks — Email =={RESET}\n")
    email_dorks = [
        ("Email en Google",         f"https://www.google.com/search?q={quote(email)}"),
        ("LinkedIn por email",      f"https://www.google.com/search?q={quote(email)}+site:linkedin.com"),
        ("Facebook por email",      f"https://www.google.com/search?q={quote(email)}+site:facebook.com"),
        ("GitHub commits",          f"https://www.google.com/search?q={quote(email)}+site:github.com"),
        ("Breaches / filtraciones", f"https://www.google.com/search?q={quote(email)}+leak+OR+breach+OR+dump"),
        ("Pastebin leaks",          f"https://www.google.com/search?q={quote(email)}+site:pastebin.com"),
        ("IntelX buscador",         f"https://intelx.io/?s={quote(email)}"),
        ("Hunter.io dominio",       f"https://hunter.io/search/{dominio}"),
    ]
    for label, url in email_dorks:
        dork_line(label, url)

# ════════════════════════════════════════════════
#  MÓDULO 6 — NOMBRE REAL + DORKS
# ════════════════════════════════════════════════
def lookup_nombre(nombre):
    section(f"NOMBRE REAL  >  {nombre}")
    spinner("Construyendo Google Dorks...", 0.8)

    print(f"\n{G}  == Google Dorks — Nombre Real =={RESET}\n")
    nombre_dorks = [
        ("LinkedIn Argentina",      f'"{nombre}" site:linkedin.com Argentina'),
        ("Instagram Argentina",     f'"{nombre}" Instagram Argentina'),
        ("Facebook perfil",         f'"{nombre}" site:facebook.com'),
        ("TikTok Argentina",        f'"{nombre}" TikTok Argentina'),
        ("Twitter/X",               f'"{nombre}" site:x.com'),
        ("YouTube canal",           f'"{nombre}" site:youtube.com'),
        ("Email/Correo",            f'"{nombre}" correo OR email Argentina'),
        ("Medios AR",               f'"{nombre}" site:infobae.com OR site:clarin.com OR site:lanacion.com.ar'),
        ("WhatsApp número",         f'"{nombre}" WhatsApp número Argentina'),
        ("Dateas",                  f'"{nombre}" site:dateas.com'),
        ("Fotos públicas",          f'"{nombre}" filetype:jpg OR filetype:png Argentina'),
        ("Docs públicos",           f'"{nombre}" filetype:pdf Argentina'),
        ("GitHub proyectos",        f'"{nombre}" site:github.com'),
        ("Foros / Comunidades",     f'"{nombre}" foro OR comunidad Argentina'),
        ("Reddit menciones",        f'"{nombre}" site:reddit.com'),
        ("MercadoLibre vendedor",   f'"{nombre}" site:mercadolibre.com.ar'),
        ("Boletín Oficial",         f'"{nombre}" site:boletinoficial.gob.ar'),
    ]
    for label, query in nombre_dorks:
        url = f"https://www.google.com/search?q={quote(query)}"
        dork_line(label, url)

    print(f"{G}  == Directorios Públicos AR =={RESET}\n")
    directorios = [
        ("Dateas AR",           f"https://www.dateas.com/es/persona/{quote(nombre)}"),
        ("InfoBusca AR",        f"https://infobusca.com.ar/buscar?q={quote(nombre)}"),
        ("BuscarPersonas AR",   f"https://www.buscarpersonas.com.ar/buscar?nombre={quote(nombre)}"),
        ("True People Search",  f"https://www.truepeoplesearch.com/results?name={quote(nombre)}"),
        ("Spokeo",              f"https://www.spokeo.com/search?q={quote(nombre)}"),
        ("PeekYou",             f"https://www.peekyou.com/{quote(nombre)}"),
        ("Webmii",              f"https://webmii.com/people?n={quote(nombre)}"),
        ("Pipl",                f"https://pipl.com/search/?q={quote(nombre)}"),
    ]
    for label, url in directorios:
        dork_line(label, url)

# ════════════════════════════════════════════════
#  MENÚ
# ════════════════════════════════════════════════
def menu():
    print(f"""
{G}  ================================================{RESET}
  {W}{BOLD}  Que queres buscar?{RESET}

  {G}[1]{RESET}  {C}Username / handle{RESET}      (redes sociales)
  {G}[2]{RESET}  {C}Número de teléfono{RESET}     (operadora, región, dorks)
  {G}[3]{RESET}  {C}DNI{RESET}                    (dorks, CUIL, directorios)
  {G}[4]{RESET}  {C}CVU / Alias MercadoPago{RESET}(entidad, titular)
  {G}[5]{RESET}  {C}Email{RESET}                  (Gravatar, HIBP, dorks)
  {G}[6]{RESET}  {C}Nombre real{RESET}            (dorks + directorios AR)
  {G}[7]{RESET}  {Y}COMBO FULL{RESET}             (todo junto)
  {R}[0]{RESET}  Salir
{G}  ================================================{RESET}
""")
    return input(f"  {G}franktool{RESET} {C}>{RESET} ").strip()

# ════════════════════════════════════════════════
#  MAIN
# ════════════════════════════════════════════════
def main():
    banner()
    while True:
        opcion = menu()

        if opcion == "0":
            print(f"\n  {R}Cerrando franktool... joya chief.{RESET}\n")
            sys.exit(0)

        if opcion == "1":
            h = input(f"\n  {C}Username (sin @):{RESET} ").strip()
            if h: check_username(h)

        elif opcion == "2":
            n = input(f"\n  {C}Teléfono (ej: 2235738120 o +542235738120):{RESET} ").strip()
            if n: lookup_telefono(n)

        elif opcion == "3":
            d = input(f"\n  {C}DNI (solo números):{RESET} ").strip()
            s = input(f"  {C}Sexo (M/F o Enter para saltar):{RESET} ").strip()
            if d: lookup_dni(d, s)

        elif opcion == "4":
            c = input(f"\n  {C}CVU (22 dígitos) o Alias MP:{RESET} ").strip()
            if c: lookup_cvu(c)

        elif opcion == "5":
            e = input(f"\n  {C}Email:{RESET} ").strip()
            if e: lookup_email(e)

        elif opcion == "6":
            nb = input(f"\n  {C}Nombre real (ej: Juan Perez):{RESET} ").strip()
            if nb: lookup_nombre(nb)

        elif opcion == "7":
            print(f"\n  {Y}-- MODO COMBO FULL --{RESET}")
            nb = input(f"  {C}Nombre real:{RESET} ").strip()
            h  = input(f"  {C}Username/handle:{RESET} ").strip()
            n  = input(f"  {C}Teléfono:{RESET} ").strip()
            d  = input(f"  {C}DNI:{RESET} ").strip()
            s  = input(f"  {C}Sexo (M/F):{RESET} ").strip()
            c  = input(f"  {C}CVU o Alias MP:{RESET} ").strip()
            e  = input(f"  {C}Email:{RESET} ").strip()
            print()
            if nb: lookup_nombre(nb)
            if h:  check_username(h)
            if n:  lookup_telefono(n)
            if d:  lookup_dni(d, s)
            if c:  lookup_cvu(c)
            if e:  lookup_email(e)

        else:
            print(f"  {R}Opción inválida chief{RESET}")

        print(f"\n{G}  ================================================{RESET}")
        input(f"  {DIM}Presioná Enter para volver al menú...{RESET}")
        print()

if __name__ == "__main__":
    main()
