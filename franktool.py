#!/usr/bin/env python3
# ================================================
#     FRANKTOOL v4.0 — ARSENAL EDITION
#     by shizzafrank | nullstate
#     OSINT Launcher — AR / UY / PE
# ================================================

import sys
import os
import time
import re
import subprocess
import requests
from urllib.parse import quote

try:
    import phonenumbers
    from phonenumbers import geocoder, carrier
    from phonenumbers import timezone as pn_timezone
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
    os.system("clear")
    print(f"""
{G}  ███████╗██████╗  █████╗ ███╗   ██╗██╗  ██╗
{G}  ██╔════╝██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
{C}  █████╗  ██████╔╝███████║██╔██╗ ██║█████╔╝
{C}  ██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗
{G}  ██║     ██║  ██║██║  ██║██║ ╚████║██║  ██╗
{G}  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
{C}   v4.0 ARSENAL EDITION -- by shizzafrank{RESET}
{DIM}  OSINT · AR · UY · PE · 100+ tools integradas{RESET}
{G}  ================================================{RESET}
""")

# ── UTILS ───────────────────────────────────────
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

def tool_check(tool):
    """Verifica si una herramienta está instalada"""
    result = subprocess.run(
        ["which", tool],
        capture_output=True, text=True
    )
    return result.returncode == 0

def run_tool(cmd, desc=""):
    """Corre una herramienta externa y muestra output"""
    print(f"\n{G}  == {desc} =={RESET}\n")
    try:
        subprocess.run(cmd, shell=True)
    except KeyboardInterrupt:
        print(f"\n  {Y}[!] Interrumpido por el usuario{RESET}")

def save_output(filename, content):
    """Guarda resultados en archivo"""
    path = f"./resultados/{filename}"
    os.makedirs("./resultados", exist_ok=True)
    with open(path, "a") as f:
        f.write(content + "\n")
    print(f"  {G}[GUARDADO]{RESET} {DIM}{path}{RESET}")

# ════════════════════════════════════════════════
#  MÓDULO 1 — USERNAME (Sherlock + Maigret + Blackbird)
# ════════════════════════════════════════════════
SOCIAL_SITES = {
    "Instagram"      : "https://www.instagram.com/{}/",
    "Twitter/X"      : "https://x.com/{}",
    "TikTok"         : "https://www.tiktok.com/@{}",
    "Facebook"       : "https://www.facebook.com/{}",
    "LinkedIn"       : "https://www.linkedin.com/in/{}/",
    "YouTube"        : "https://www.youtube.com/@{}",
    "Pinterest"      : "https://www.pinterest.com/{}/",
    "Snapchat"       : "https://www.snapchat.com/add/{}",
    "BeReal"         : "https://bere.al/{}",
    "Threads"        : "https://www.threads.net/@{}",
    "Mastodon"       : "https://mastodon.social/@{}",
    "Steam"          : "https://steamcommunity.com/id/{}",
    "Twitch"         : "https://www.twitch.tv/{}",
    "Xbox"           : "https://account.xbox.com/en-US/profile?gamertag={}",
    "Roblox"         : "https://www.roblox.com/user.aspx?username={}",
    "Chess.com"      : "https://www.chess.com/member/{}",
    "GitHub"         : "https://github.com/{}",
    "GitLab"         : "https://gitlab.com/{}",
    "Replit"         : "https://replit.com/@{}",
    "HackerOne"      : "https://hackerone.com/{}",
    "SoundCloud"     : "https://soundcloud.com/{}",
    "Spotify"        : "https://open.spotify.com/user/{}",
    "Bandcamp"       : "https://{}.bandcamp.com",
    "Mixcloud"       : "https://www.mixcloud.com/{}/",
    "DeviantArt"     : "https://www.deviantart.com/{}",
    "Behance"        : "https://www.behance.net/{}",
    "ArtStation"     : "https://www.artstation.com/{}",
    "Tumblr"         : "https://{}.tumblr.com",
    "Medium"         : "https://medium.com/@{}",
    "Reddit"         : "https://www.reddit.com/user/{}",
    "Telegram"       : "https://t.me/{}",
    "Discord"        : "https://discord.com/users/{}",
    "Patreon"        : "https://www.patreon.com/{}",
    "OnlyFans"       : "https://onlyfans.com/{}",
    "Ko-fi"          : "https://ko-fi.com/{}",
    "Linktree"       : "https://linktr.ee/{}",
    "Fiverr"         : "https://www.fiverr.com/{}",
    "ProductHunt"    : "https://www.producthunt.com/@{}",
    "Gravatar"       : "https://en.gravatar.com/{}",
    "Substack"       : "https://{}.substack.com",
}

FALSE_POSITIVES = [
    "page not found","user not found","this account doesn't exist",
    "profile not found","doesn't exist","no existe","sorry, this page",
    "isn't available","no encontrado","not available",
]

def check_username(handle):
    section(f"USERNAME HUNT  >  @{handle}")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log = f"=== USERNAME: {handle} === {timestamp}\n"
    found = []

    # ── nuestro check propio ─────────────────────
    print(f"  {C}[1/3]{RESET} Chequeando plataformas propias...\n")
    total = len(SOCIAL_SITES)
    for i, (platform, url_tpl) in enumerate(SOCIAL_SITES.items(), 1):
        url = url_tpl.format(handle)
        spinner(f"[{i}/{total}] {platform}", 0.3)
        try:
            r = requests.get(url, headers=HEADERS, timeout=7, allow_redirects=True)
            if r.status_code == 200:
                body = r.text.lower()
                if any(kw in body for kw in FALSE_POSITIVES):
                    miss(platform)
                else:
                    hit(platform, url)
                    found.append((platform, url))
                    log += f"[+] {platform}: {url}\n"
            elif r.status_code == 404:
                miss(platform)
            else:
                warn(platform, f"STATUS {r.status_code}")
        except:
            print(f"  {DIM}[!] {platform:<22} timeout{RESET}")

    # ── Sherlock ─────────────────────────────────
    print(f"\n  {C}[2/3]{RESET} Corriendo Sherlock (400+ sitios)...")
    if tool_check("sherlock"):
        run_tool(f"sherlock {handle} --timeout 10", "Sherlock Results")
        log += f"\n[SHERLOCK] corrido para {handle}\n"
    else:
        warn("Sherlock", "no instalado — corré: pip install sherlock-project")

    # ── Maigret ──────────────────────────────────
    print(f"\n  {C}[3/3]{RESET} Corriendo Maigret (3000+ sitios)...")
    if tool_check("maigret"):
        run_tool(f"maigret {handle}", "Maigret Results")
        log += f"\n[MAIGRET] corrido para {handle}\n"
    else:
        warn("Maigret", "no instalado — corré: pip install maigret")

    # ── resumen ───────────────────────────────────
    print(f"\n{G}  ================================================{RESET}")
    print(f"  {G}[+] Encontrado en {BOLD}{len(found)}{RESET}{G} plataformas propias{RESET}")
    print(f"{G}  ================================================{RESET}")

    save_output(f"username_{handle}_{timestamp}.txt", log)

# ════════════════════════════════════════════════
#  MÓDULO 2 — TELÉFONO (Phoneinfoga + phonenumbers)
# ════════════════════════════════════════════════
def lookup_telefono(numero):
    section(f"TELÉFONO LOOKUP  >  {numero}")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log = f"=== TELÉFONO: {numero} === {timestamp}\n"

    numero_limpio = re.sub(r"[^\d+]", "", numero)
    if not numero_limpio.startswith("+"):
        numero_limpio = "+54" + numero_limpio.lstrip("0")

    # ── phonenumbers ─────────────────────────────
    if PHONENUMBERS_OK:
        spinner("Analizando con phonenumbers...", 0.8)
        try:
            parsed = phonenumbers.parse(numero_limpio)
            valido   = phonenumbers.is_valid_number(parsed)
            region   = geocoder.description_for_number(parsed, "es")
            operadora= carrier.name_for_number(parsed, "es")
            zonas    = list(pn_timezone.time_zones_for_number(parsed))
            fmt_int  = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            fmt_nac  = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
            tipo     = str(phonenumbers.number_type(parsed))

            info("Internacional", fmt_int)
            info("Nacional",      fmt_nac)
            info("Válido",        str(valido))
            info("Región",        region or "Desconocida")
            info("Operadora",     operadora or "Desconocida")
            info("Zona horaria",  ", ".join(zonas) if zonas else "Desconocida")
            info("Tipo de línea", tipo)
            log += f"Internacional: {fmt_int}\nRegión: {region}\nOperadora: {operadora}\n"
        except Exception as e:
            warn("phonenumbers", f"Error: {e}")

    # ── Phoneinfoga ──────────────────────────────
    print(f"\n  {C}[TOOL]{RESET} Corriendo Phoneinfoga...")
    num_plain = re.sub(r"[^\d]", "", numero)
    if tool_check("phoneinfoga"):
        run_tool(
            f"phoneinfoga scan -n {numero_limpio}",
            "Phoneinfoga Results"
        )
        log += f"\n[PHONEINFOGA] corrido para {numero_limpio}\n"
    else:
        warn("Phoneinfoga", "no instalado — corré: go install github.com/sundowndev/phoneinfoga/v2/cmd/phoneinfoga@latest")

    # ── dorks ────────────────────────────────────
    spinner("Generando dorks...", 0.5)
    print(f"\n{G}  == Google Dorks =={RESET}\n")
    dorks = [
        ("WhatsApp directo",    f"https://wa.me/549{num_plain}"),
        ("Google general",      f"https://www.google.com/search?q={quote(num_plain)}+Argentina"),
        ("MercadoLibre",        f"https://www.google.com/search?q={quote(num_plain)}+site:mercadolibre.com.ar"),
        ("Facebook",            f"https://www.google.com/search?q={quote(num_plain)}+site:facebook.com"),
        ("OLX AR",              f"https://www.google.com/search?q={quote(num_plain)}+site:olx.com.ar"),
        ("Telegram",            f"https://www.google.com/search?q={quote(num_plain)}+site:t.me"),
        ("TrueCaller",          f"https://www.truecaller.com/search/ar/{num_plain}"),
        ("NumLookup",           f"https://www.numlookup.com/{num_plain}"),
        ("Foros AR",            f"https://www.google.com/search?q={quote(num_plain)}+Argentina+foro"),
    ]
    for label, url in dorks:
        dork_line(label, url)
        log += f"[DORK] {label}: {url}\n"

    save_output(f"telefono_{num_plain}_{timestamp}.txt", log)

# ════════════════════════════════════════════════
#  MÓDULO 3 — EMAIL (Holehe + GHunt + Gravatar)
# ════════════════════════════════════════════════
def lookup_email(email):
    section(f"EMAIL LOOKUP  >  {email}")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log = f"=== EMAIL: {email} === {timestamp}\n"

    dominio = email.split("@")[-1] if "@" in email else ""
    usuario = email.split("@")[0]  if "@" in email else email
    info("Usuario", usuario)
    info("Dominio", dominio)

    # ── Gravatar ─────────────────────────────────
    import hashlib
    gravatar_hash = hashlib.md5(email.strip().lower().encode()).hexdigest()
    gravatar_url  = f"https://www.gravatar.com/avatar/{gravatar_hash}?d=404"
    spinner("Chequeando Gravatar...", 0.5)
    try:
        r = requests.get(gravatar_url, timeout=5)
        if r.status_code == 200:
            hit("Gravatar", f"https://www.gravatar.com/{gravatar_hash}")
            log += f"[+] Gravatar encontrado\n"
        else:
            miss("Gravatar")
    except:
        warn("Gravatar", "timeout")

    # ── Holehe ───────────────────────────────────
    print(f"\n  {C}[TOOL]{RESET} Corriendo Holehe (120+ sitios)...")
    if tool_check("holehe"):
        run_tool(f"holehe {email}", "Holehe Results")
        log += f"\n[HOLEHE] corrido para {email}\n"
    else:
        warn("Holehe", "no instalado — corré: pip install holehe")

    # ── GHunt ────────────────────────────────────
    print(f"\n  {C}[TOOL]{RESET} Corriendo GHunt (Google OSINT)...")
    if tool_check("ghunt"):
        run_tool(f"ghunt email {email}", "GHunt Results")
        log += f"\n[GHUNT] corrido para {email}\n"
    else:
        warn("GHunt", "no instalado — corré: pip install ghunt")

    # ── theHarvester ─────────────────────────────
    print(f"\n  {C}[TOOL]{RESET} Corriendo theHarvester...")
    if tool_check("theHarvester"):
        run_tool(
            f"theHarvester -d {dominio} -b google,bing,yahoo",
            "theHarvester Results"
        )
        log += f"\n[THEHARVESTER] corrido para {dominio}\n"
    else:
        warn("theHarvester", "no instalado — corré: apt install theharvester")

    # ── dorks email ──────────────────────────────
    print(f"\n{G}  == Google Dorks — Email =={RESET}\n")
    email_dorks = [
        ("Google general",      f"https://www.google.com/search?q={quote(email)}"),
        ("LinkedIn",            f"https://www.google.com/search?q={quote(email)}+site:linkedin.com"),
        ("Facebook",            f"https://www.google.com/search?q={quote(email)}+site:facebook.com"),
        ("GitHub",              f"https://www.google.com/search?q={quote(email)}+site:github.com"),
        ("Brechas/leaks",       f"https://www.google.com/search?q={quote(email)}+leak+OR+breach"),
        ("Pastebin",            f"https://www.google.com/search?q={quote(email)}+site:pastebin.com"),
        ("IntelX",              f"https://intelx.io/?s={quote(email)}"),
        ("HaveIBeenPwned",      f"https://haveibeenpwned.com/account/{quote(email)}"),
    ]
    for label, url in email_dorks:
        dork_line(label, url)
        log += f"[DORK] {label}: {url}\n"

    save_output(f"email_{usuario}_{timestamp}.txt", log)

# ════════════════════════════════════════════════
#  MÓDULO 4 — DNI (AR / UY / PE)
# ════════════════════════════════════════════════
def lookup_dni(dni, sexo="", pais="AR"):
    section(f"DNI LOOKUP  >  {dni}  [{pais}]")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log = f"=== DNI: {dni} [{pais}] === {timestamp}\n"

    dni_limpio = re.sub(r"[^\d]", "", dni)
    info("DNI ingresado", dni_limpio)
    info("País", pais)

    # estimación edad AR
    if pais == "AR":
        dni_int = int(dni_limpio) if dni_limpio.isdigit() else 0
        if   dni_int < 8_000_000:  rango = "Nacido aprox. antes de 1965"
        elif dni_int < 14_000_000: rango = "Nacido aprox. 1965-1975"
        elif dni_int < 20_000_000: rango = "Nacido aprox. 1975-1983"
        elif dni_int < 28_000_000: rango = "Nacido aprox. 1983-1993"
        elif dni_int < 38_000_000: rango = "Nacido aprox. 1993-2003"
        elif dni_int < 50_000_000: rango = "Nacido aprox. 2003-2015"
        else:                       rango = "Nacido aprox. 2015+"
        info("Estimación de edad", rango)

        if sexo.upper() in ("M", "MASCULINO"):
            prefijo = "20"
        elif sexo.upper() in ("F", "FEMENINO"):
            prefijo = "27"
        else:
            prefijo = "20 o 27"
        info("CUIL estimado", f"{prefijo}-{dni_limpio}-?")
        log += f"CUIL estimado: {prefijo}-{dni_limpio}-?\n"

    # dorks por país
    print(f"\n{G}  == Google Dorks — DNI [{pais}] =={RESET}\n")

    if pais == "AR":
        dorks = [
            ("Dateas AR",           f"https://www.dateas.com/es/persona/{dni_limpio}"),
            ("AFIP CUIT",           f"https://www.google.com/search?q=CUIT+{dni_limpio}+AFIP"),
            ("BCRA Deudores",       f"https://www.bcra.gob.ar/BCRAyVos/Sitio_CentralDeDeudores.asp"),
            ("NOSIS",               f"https://www.nosis.com/es/BusquedaPersonas/Busqueda?criteria={dni_limpio}"),
            ("ANSES CUIL",          f"https://www.anses.gob.ar/consulta/constancia-de-cuil"),
            ("Boletín Oficial",     f"https://www.google.com/search?q={dni_limpio}+site:boletinoficial.gob.ar"),
            ("MercadoLibre",        f"https://www.google.com/search?q={dni_limpio}+site:mercadolibre.com.ar"),
            ("Docs públicos",       f"https://www.google.com/search?q={dni_limpio}+filetype:pdf+Argentina"),
            ("Redes sociales",      f"https://www.google.com/search?q={dni_limpio}+Argentina+Instagram+OR+Facebook"),
            ("DNRPA automotor",     f"https://www.dnrpa.gov.ar/portal_dnrpa/"),
        ]
    elif pais == "UY":
        dorks = [
            ("BPS Uruguay",         f"https://www.google.com/search?q={dni_limpio}+site:bps.gub.uy"),
            ("DGI Uruguay",         f"https://www.google.com/search?q={dni_limpio}+site:dgi.gub.uy"),
            ("Poder Judicial UY",   f"https://www.google.com/search?q={dni_limpio}+site:poderjudicial.gub.uy"),
            ("Catastro UY",         f"https://www.google.com/search?q={dni_limpio}+catastro+Uruguay"),
            ("Presidencia UY",      f"https://www.google.com/search?q={dni_limpio}+site:presidencia.gub.uy"),
            ("Docs públicos UY",    f"https://www.google.com/search?q={dni_limpio}+filetype:pdf+Uruguay"),
        ]
    elif pais == "PE":
        dorks = [
            ("RENIEC Perú",         f"https://www.google.com/search?q={dni_limpio}+site:reniec.gob.pe"),
            ("SUNAT RUC",           f"https://www.google.com/search?q={dni_limpio}+site:sunat.gob.pe"),
            ("SUNARP",              f"https://www.google.com/search?q={dni_limpio}+site:sunarp.gob.pe"),
            ("Poder Judicial PE",   f"https://www.google.com/search?q={dni_limpio}+site:pj.gob.pe"),
            ("OSCE Perú",           f"https://www.google.com/search?q={dni_limpio}+site:osce.gob.pe"),
            ("Docs públicos PE",    f"https://www.google.com/search?q={dni_limpio}+filetype:pdf+Peru"),
        ]
    else:
        dorks = []

    for label, url in dorks:
        dork_line(label, url)
        log += f"[DORK] {label}: {url}\n"

    save_output(f"dni_{dni_limpio}_{pais}_{timestamp}.txt", log)

# ════════════════════════════════════════════════
#  MÓDULO 5 — CVU / ALIAS MP
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
    "0000044": "Banco Macro",
    "0000016": "ICBC Argentina",
    "0000029": "Banco Ciudad",
    "0000032": "Banco Provincia",
}

def lookup_cvu(cvu_o_alias):
    section(f"CVU / ALIAS MP  >  {cvu_o_alias}")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log = f"=== CVU/ALIAS: {cvu_o_alias} === {timestamp}\n"

    cvu_limpio = re.sub(r"[^\d]", "", cvu_o_alias)
    es_cvu = len(cvu_limpio) == 22 and cvu_limpio.isdigit()

    if es_cvu:
        spinner("Validando CVU...", 0.7)
        info("Tipo",     "CVU (22 dígitos)")
        prefijo = cvu_limpio[3:10]
        entidad = CVU_ENTITIES.get(prefijo, "Entidad desconocida")
        info("Prefijo",  prefijo)
        hit("Entidad",   entidad)
        log += f"Entidad: {entidad}\n"
    else:
        spinner("Procesando alias...", 0.5)
        info("Tipo",  "Alias")
        partes   = cvu_o_alias.replace("-", ".").split(".")
        filtradas = [p for p in partes if p.lower() not in
                     ("mp","ag","bk","nb","pp","ux","ml","ar")]
        if filtradas:
            posible = " ".join(filtradas).title()
            hit("Posible titular", posible)
            log += f"Posible titular: {posible}\n"

    print(f"\n{G}  == Google Dorks — CVU/Alias =={RESET}\n")
    termino = cvu_o_alias
    cvu_dorks = [
        ("Google general",      f"https://www.google.com/search?q={quote(termino)}+Argentina"),
        ("MercadoLibre",        f"https://www.google.com/search?q={quote(termino)}+site:mercadolibre.com.ar"),
        ("Facebook ventas",     f"https://www.google.com/search?q={quote(termino)}+site:facebook.com"),
        ("OLX AR",              f"https://www.google.com/search?q={quote(termino)}+site:olx.com.ar"),
        ("Instagram cobros",    f"https://www.google.com/search?q={quote(termino)}+site:instagram.com"),
        ("Twitter/X cobros",    f"https://www.google.com/search?q={quote(termino)}+site:x.com"),
        ("Foros pagos AR",      f"https://www.google.com/search?q={quote(termino)}+mercadopago+pago"),
    ]
    for label, url in cvu_dorks:
        dork_line(label, url)
        log += f"[DORK] {label}: {url}\n"

    save_output(f"cvu_{timestamp}.txt", log)

# ════════════════════════════════════════════════
#  MÓDULO 6 — NOMBRE REAL + SOCMINT
# ════════════════════════════════════════════════
def lookup_nombre(nombre, pais="AR"):
    section(f"NOMBRE REAL  >  {nombre}  [{pais}]")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log = f"=== NOMBRE: {nombre} [{pais}] === {timestamp}\n"

    # ── theHarvester ─────────────────────────────
    print(f"  {C}[TOOL]{RESET} Corriendo theHarvester...")
    if tool_check("theHarvester"):
        run_tool(
            f'theHarvester -d "{nombre}" -b google,bing',
            "theHarvester — Nombre"
        )
    else:
        warn("theHarvester", "no instalado")

    # ── spiderfoot ───────────────────────────────
    print(f"\n  {C}[TOOL]{RESET} Spiderfoot disponible en: http://localhost:5009")
    if tool_check("spiderfoot"):
        info("Spiderfoot", "Corré: spiderfoot -l 127.0.0.1:5009")
    else:
        warn("Spiderfoot", "no instalado — pip install spiderfoot")

    # ── dorks por país ───────────────────────────
    print(f"\n{G}  == Google Dorks — Nombre [{pais}] =={RESET}\n")

    base_dorks = [
        ("LinkedIn",        f'"{nombre}" site:linkedin.com'),
        ("Instagram",       f'"{nombre}" Instagram'),
        ("Facebook",        f'"{nombre}" site:facebook.com'),
        ("TikTok",          f'"{nombre}" TikTok'),
        ("Twitter/X",       f'"{nombre}" site:x.com'),
        ("Email/Correo",    f'"{nombre}" correo OR email'),
        ("WhatsApp",        f'"{nombre}" WhatsApp número'),
        ("Fotos públicas",  f'"{nombre}" filetype:jpg OR filetype:png'),
        ("Docs PDF",        f'"{nombre}" filetype:pdf'),
        ("GitHub",          f'"{nombre}" site:github.com'),
        ("MercadoLibre",    f'"{nombre}" site:mercadolibre.com.ar'),
        ("YouTube",         f'"{nombre}" site:youtube.com'),
    ]

    if pais == "AR":
        extra = [
            ("Infobae/Clarín",  f'"{nombre}" site:infobae.com OR site:clarin.com'),
            ("Dateas AR",       f'"{nombre}" site:dateas.com'),
            ("Boletín Oficial", f'"{nombre}" site:boletinoficial.gob.ar'),
            ("OLX AR",          f'"{nombre}" site:olx.com.ar'),
        ]
    elif pais == "UY":
        extra = [
            ("El País UY",      f'"{nombre}" site:elpais.com.uy'),
            ("La Diaria UY",    f'"{nombre}" site:ladiaria.com.uy'),
            ("Presidencia UY",  f'"{nombre}" site:presidencia.gub.uy'),
            ("Gallito UY",      f'"{nombre}" site:gallito.com.uy'),
        ]
    elif pais == "PE":
        extra = [
            ("El Comercio PE",  f'"{nombre}" site:elcomercio.pe'),
            ("RPP Noticias",    f'"{nombre}" site:rpp.pe'),
            ("SUNAT PE",        f'"{nombre}" site:sunat.gob.pe'),
            ("OLX Peru",        f'"{nombre}" site:olx.com.pe'),
        ]
    else:
        extra = []

    for label, query in base_dorks + extra:
        url = f"https://www.google.com/search?q={quote(query)}"
        dork_line(label, url)
        log += f"[DORK] {label}: {url}\n"

    # ── directorios por país ──────────────────────
    print(f"{G}  == Directorios [{pais}] =={RESET}\n")
    if pais == "AR":
        dirs = [
            ("Dateas AR",           f"https://www.dateas.com/es/persona/{quote(nombre)}"),
            ("InfoBusca AR",        f"https://infobusca.com.ar/buscar?q={quote(nombre)}"),
            ("BuscarPersonas AR",   f"https://www.buscarpersonas.com.ar/buscar?nombre={quote(nombre)}"),
            ("Spokeo",              f"https://www.spokeo.com/search?q={quote(nombre)}"),
            ("PeekYou",             f"https://www.peekyou.com/{quote(nombre)}"),
            ("Webmii",              f"https://webmii.com/people?n={quote(nombre)}"),
        ]
    elif pais == "UY":
        dirs = [
            ("BPS Uruguay",         f"https://www.google.com/search?q={quote(nombre)}+site:bps.gub.uy"),
            ("DGI Uruguay",         f"https://www.google.com/search?q={quote(nombre)}+site:dgi.gub.uy"),
            ("Poder Judicial UY",   f"https://www.google.com/search?q={quote(nombre)}+poderjudicial.gub.uy"),
        ]
    elif pais == "PE":
        dirs = [
            ("RENIEC PE",           f"https://www.google.com/search?q={quote(nombre)}+site:reniec.gob.pe"),
            ("SUNAT PE",            f"https://www.google.com/search?q={quote(nombre)}+site:sunat.gob.pe"),
            ("SUNARP PE",           f"https://www.google.com/search?q={quote(nombre)}+site:sunarp.gob.pe"),
        ]
    else:
        dirs = []

    for label, url in dirs:
        dork_line(label, url)
        log += f"[DIR] {label}: {url}\n"

    save_output(f"nombre_{nombre.replace(' ','_')}_{pais}_{timestamp}.txt", log)

# ════════════════════════════════════════════════
#  MÓDULO 7 — IP LOOKUP
# ════════════════════════════════════════════════
def lookup_ip(ip):
    section(f"IP LOOKUP  >  {ip}")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log = f"=== IP: {ip} === {timestamp}\n"

    spinner("Consultando ip-api.com...", 1.0)
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=8)
        data = r.json()
        if data.get("status") == "success":
            hit("IP",           data.get("query","?"))
            info("País",        data.get("country","?"))
            info("Región",      data.get("regionName","?"))
            info("Ciudad",      data.get("city","?"))
            info("ISP",         data.get("isp","?"))
            info("Organización",data.get("org","?"))
            info("ASN",         data.get("as","?"))
            info("Timezone",    data.get("timezone","?"))
            info("Lat/Lon",     f"{data.get('lat','?')}, {data.get('lon','?')}")
            maps_url = f"https://maps.google.com/?q={data.get('lat')},{data.get('lon')}"
            hit("Google Maps",  maps_url)
            log += f"País: {data.get('country')}\nCiudad: {data.get('city')}\nISP: {data.get('isp')}\n"
        else:
            warn("ip-api", "IP privada o error")
    except Exception as e:
        warn("ip-api", f"Error: {e}")

    # nmap básico
    print(f"\n  {C}[TOOL]{RESET} Corriendo Nmap básico...")
    if tool_check("nmap"):
        run_tool(f"nmap -sV -T4 --top-ports 20 {ip}", "Nmap Results")
        log += f"\n[NMAP] corrido para {ip}\n"
    else:
        warn("Nmap", "no instalado — apt install nmap")

    save_output(f"ip_{ip}_{timestamp}.txt", log)

# ════════════════════════════════════════════════
#  MENÚ
# ════════════════════════════════════════════════
def select_country():
    print(f"""
  {W}País objetivo:{RESET}
  {G}[1]{RESET} Argentina 🇦🇷
  {G}[2]{RESET} Uruguay 🇺🇾
  {G}[3]{RESET} Perú 🇵🇪
""")
    opt = input(f"  {G}>{RESET} ").strip()
    return {"1":"AR","2":"UY","3":"PE"}.get(opt, "AR")

def menu():
    print(f"""
{G}  ================================================{RESET}
  {W}{BOLD}  Que queres hacer?{RESET}

  {G}[1]{RESET}  {C}Username / handle{RESET}     Sherlock + Maigret + 40 plataformas
  {G}[2]{RESET}  {C}Número de teléfono{RESET}    Phoneinfoga + phonenumbers + dorks
  {G}[3]{RESET}  {C}Email{RESET}                 Holehe + GHunt + theHarvester + dorks
  {G}[4]{RESET}  {C}DNI / CI{RESET}              Dorks por país AR/UY/PE + CUIL
  {G}[5]{RESET}  {C}CVU / Alias MP{RESET}        Entidad bancaria + dorks
  {G}[6]{RESET}  {C}Nombre real{RESET}           theHarvester + dorks + directorios
  {G}[7]{RESET}  {C}IP Address{RESET}            ip-api + Nmap + geolocalización
  {G}[8]{RESET}  {Y}COMBO FULL{RESET}            Todo junto
  {R}[0]{RESET}  Salir
{G}  ================================================{RESET}
""")
    return input(f"  {G}franktool{RESET} {C}>{RESET} ").strip()

# ════════════════════════════════════════════════
#  MAIN
# ════════════════════════════════════════════════
def main():
    banner()

    # verificar tools instaladas al arrancar
    tools_check = {
        "sherlock":      tool_check("sherlock"),
        "maigret":       tool_check("maigret"),
        "holehe":        tool_check("holehe"),
        "ghunt":         tool_check("ghunt"),
        "phoneinfoga":   tool_check("phoneinfoga"),
        "theHarvester":  tool_check("theHarvester"),
        "nmap":          tool_check("nmap"),
        "spiderfoot":    tool_check("spiderfoot"),
    }

    print(f"{G}  == Tools disponibles =={RESET}")
    for t, ok in tools_check.items():
        status = f"{G}[OK]{RESET}" if ok else f"{R}[NO]{RESET}"
        print(f"  {status} {t}")
    print()

    while True:
        opcion = menu()

        if opcion == "0":
            print(f"\n  {R}Cerrando franktool... joya chief.{RESET}\n")
            sys.exit(0)

        elif opcion == "1":
            h = input(f"\n  {C}Username (sin @):{RESET} ").strip()
            if h: check_username(h)

        elif opcion == "2":
            n = input(f"\n  {C}Teléfono:{RESET} ").strip()
            if n: lookup_telefono(n)

        elif opcion == "3":
            e = input(f"\n  {C}Email:{RESET} ").strip()
            if e: lookup_email(e)

        elif opcion == "4":
            pais = select_country()
            d = input(f"\n  {C}DNI/CI:{RESET} ").strip()
            s = input(f"  {C}Sexo (M/F o Enter):{RESET} ").strip()
            if d: lookup_dni(d, s, pais)

        elif opcion == "5":
            c = input(f"\n  {C}CVU o Alias MP:{RESET} ").strip()
            if c: lookup_cvu(c)

        elif opcion == "6":
            pais = select_country()
            nb = input(f"\n  {C}Nombre real:{RESET} ").strip()
            if nb: lookup_nombre(nb, pais)

        elif opcion == "7":
            ip = input(f"\n  {C}IP Address:{RESET} ").strip()
            if ip: lookup_ip(ip)

        elif opcion == "8":
            print(f"\n  {Y}-- COMBO FULL --{RESET}")
            pais = select_country()
            nb = input(f"  {C}Nombre real:{RESET} ").strip()
            h  = input(f"  {C}Username:{RESET} ").strip()
            n  = input(f"  {C}Teléfono:{RESET} ").strip()
            d  = input(f"  {C}DNI/CI:{RESET} ").strip()
            s  = input(f"  {C}Sexo (M/F):{RESET} ").strip()
            c  = input(f"  {C}CVU o Alias MP:{RESET} ").strip()
            e  = input(f"  {C}Email:{RESET} ").strip()
            ip = input(f"  {C}IP Address:{RESET} ").strip()
            print()
            if nb: lookup_nombre(nb, pais)
            if h:  check_username(h)
            if n:  lookup_telefono(n)
            if d:  lookup_dni(d, s, pais)
            if c:  lookup_cvu(c)
            if e:  lookup_email(e)
            if ip: lookup_ip(ip)

        else:
            print(f"  {R}Opción inválida{RESET}")

        print(f"\n{G}  ================================================{RESET}")
        input(f"  {DIM}Enter para volver al menú...{RESET}")
        banner()

if __name__ == "__main__":
    main()
