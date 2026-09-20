<div align="center">

```
███████╗██████╗  █████╗ ███╗   ██╗██╗  ██╗
██╔════╝██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
█████╗  ██████╔╝███████║██╔██╗ ██║█████╔╝
██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗
██║     ██║  ██║██║  ██║██║ ╚████║██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
  T O O L  —  LATAM OSINT ULTIMATE EDITION
```

**by shizzafrank | **



![Tools](https://img.shields.io/badge/Tools-1000%2B-brightgreen?style=for-the-badge)




![LATAM](https://img.shields.io/badge/Focus-Argentina%20%7C%20Uruguay%20%7C%20Peru-blue?style=for-the-badge)




![Platform](https://img.shields.io/badge/Platform-Kali%20%7C%20Termux-red?style=for-the-badge)




![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge)




![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)



> La toolkit de OSINT más completa para Argentina 🇦🇷, Uruguay 🇺🇾 y Perú 🇵🇪
> Un solo comando instala cientos de herramientas automáticamente.

</div>

---

## ⚡ Instalación — Un solo comando

```bash
git clone https://github.com/Shizzafrank233/franktool.git
cd franktool
chmod +x install.sh
sudo ./install.sh
```

---

## 🇦🇷 franktool — OSINT Interactivo LATAM

La herramienta principal del repo. Busca info de personas
en Argentina, Uruguay y Perú por username, teléfono, DNI, CVU y email.

```bash
pip install requests phonenumbers
python3 franktool.py
```

### Módulos disponibles

| Módulo | Qué hace |
|--------|----------|
| 👤 Username | Busca en 48+ plataformas activas |
| 📱 Teléfono | Operadora, región, zona horaria, dorks |
| 🪪 DNI/CI/DNI-PE | Estimación edad, CUIL/RUT/DNI-PE, 13+ dorks por país |
| 💳 CVU / Alias MP | Detecta entidad bancaria y posible titular |
| 📧 Email | Gravatar, HaveIBeenPwned, dorks |
| 🔎 Nombre real | 17 dorks + directorios AR/UY/PE |
| 💥 Combo Full | Todo junto en un formulario |

---

<details>
<summary>🇦🇷 OSINT Argentina (100+ recursos)</summary>

### Herramientas y recursos específicos AR

| Recurso | Descripción | Tipo |
|---------|-------------|------|
| franktool.py | OSINT interactivo AR/UY/PE | Python |
| Dateas | Directorio de personas AR | Web |
| AFIP CUIT | Consulta contribuyentes | Web |
| BCRA Deudores | Central de deudores bancarios | Web |
| NOSIS | Informes crediticios AR | Web |
| ANSES CUIL | Consulta CUIL/beneficios | Web |
| Boletín Oficial | Publicaciones oficiales AR | Web |
| DNRPA | Registro automotor AR | Web |
| InfoLeg | Legislación argentina | Web |
| Registro Civil AR | Datos civiles | Web |
| MercadoLibre OSINT | Vendedores y compradores AR | Dork |
| OLX Argentina | Clasificados AR | Dork |
| Properati | Propiedades AR | Dork |
| Zonaprop | Inmuebles AR | Dork |
| InfoBusca | Búsqueda personas AR | Web |
| BuscarPersonas AR | Directorio personas AR | Web |
| Clarin / Infobae | Noticias y menciones | Dork |
| La Nacion | Noticias AR | Dork |
| Paginas Amarillas AR | Directorio comercial | Web |
| WhatsApp AR | +549 dorks y búsqueda | Dork |

</details>

<details>
<summary>🇺🇾 OSINT Uruguay (80+ recursos)</summary>

### Herramientas y recursos específicos UY

| Recurso | Descripción | Tipo |
|---------|-------------|------|
| BPS Uruguay | Banco de Previsión Social | Web |
| DGI Uruguay | Dirección General Impositiva | Web |
| BCU | Banco Central Uruguay | Web |
| Registro Civil UY | Datos civiles Uruguay | Web |
| SICE Uruguay | Sistema info comercio exterior | Web |
| Catastro UY | Registro de propiedades | Web |
| El País UY | Noticias Uruguay | Dork |
| La Diaria | Noticias Uruguay | Dork |
| Subrayado | Noticias Uruguay | Dork |
| Gallito | Clasificados UY | Dork |
| MercadoLibre UY | Vendedores Uruguay | Dork |
| InfoCif UY | Empresas Uruguay | Web |
| Páginas Amarillas UY | Directorio UY | Web |
| Poder Judicial UY | Causas judiciales | Web |
| AUF | Asociación Uruguaya Fútbol | Dork |
| RUT Uruguay | Registro único tributario | Web |
| AGESIC | Agencia e-gobierno UY | Web |
| Presidencia UY | Gobierno UY | Dork |

</details>

<details>
<summary>🇵🇪 OSINT Perú (80+ recursos)</summary>

### Herramientas y recursos específicos PE

| Recurso | Descripción | Tipo |
|---------|-------------|------|
| RENIEC | Registro nac. identificación PE | Web |
| SUNAT RUC | Registro contribuyentes PE | Web |
| SUNARP | Registros públicos PE | Web |
| Poder Judicial PE | Consulta causas PE | Web |
| OSCE | Contrataciones estado PE | Web |
| INFOCORP PE | Central de riesgos PE | Web |
| El Comercio PE | Noticias Perú | Dork |
| RPP Noticias | Radio Perú | Dork |
| La República PE | Noticias PE | Dork |
| OLX Peru | Clasificados PE | Dork |
| MercadoLibre PE | Vendedores PE | Dork |
| Urbania | Inmuebles PE | Dork |
| A Dónde Vamos | Directorio PE | Web |
| Páginas Amarillas PE | Directorio PE | Web |
| MIDIS | Min. desarrollo social PE | Dork |
| SBS Perú | Superintendencia bancaria | Web |
| INDECOPI | Propiedad intelectual PE | Web |
| Consulado PE | Datos consulares | Dork |

</details>

<details>
<summary>🔍 Social Media Investigation (120+ tools)</summary>

| Tool | Descripción | Install |
|------|-------------|---------|
| Sherlock | Username en 400+ sitios | pip |
| Maigret | OSINT por username 3000+ sitios | pip |
| Osintgram | OSINT Instagram | git |
| Twint | Twitter scraper sin API | pip |
| Social-Analyzer | Análisis perfiles sociales | pip |
| Instaloader | Descarga datos Instagram | pip |
| WhatsMyName | Username enum 600+ sitios | git |
| Holehe | Email en 120+ sitios | pip |
| GHunt | Investigación cuentas Google | pip |
| Blackbird | Username OSINT multi-plataforma | git |
| Snscrape | Scraper redes sociales | pip |
| Nexfil | Perfiles por username | pip |
| Userrecon | Recon de username | git |
| Spiderfoot | Framework OSINT automatizado | pip |
| theHarvester | Email/username harvester | apt |
| Photon | Web crawler OSINT | pip |
| Profil3r | OSINT redes sociales | git |
| Tinfoleak | Inteligencia Twitter | git |

</details>

<details>
<summary>🌐 Network Reconnaissance (150+ tools)</summary>

| Tool | Descripción | Install |
|------|-------------|---------|
| Nmap | Escáner de red | apt |
| Masscan | Escáner de puertos rápido | apt |
| Rustscan | Escáner moderno | git |
| Netdiscover | Escáner ARP | apt |
| Bettercap | Monitor/ataque de red | apt |
| Responder | Envenenador LLMNR | apt |
| Impacket | Protocolos Windows | pip |
| CrackMapExec | Pentesting de red | pip |
| Amass | Enumeración subdominios | apt |
| Subfinder | Descubrimiento subdominios | go |
| Assetfinder | Finder de subdominios | go |
| Dnsx | Toolkit DNS | go |
| Dnsrecon | Reconocimiento DNS | apt |
| Shodan CLI | API Shodan | pip |
| Censys CLI | API Censys | pip |
| BBOT | Escáner OSINT recursivo | pip |
| Httpx | Toolkit HTTP | go |
| Nuclei | Escáner vulnerabilidades | go |
| Ffuf | Fuzzer web rápido | go |

</details>

<details>
<summary>🕵️ Dark Web & Tor (50+ tools)</summary>

| Tool | Descripción | Install |
|------|-------------|---------|
| Tor | Red de anonimato | apt |
| Torsocks | Rutear apps por Tor | apt |
| OnionScan | Escaneo dark web | git |
| DarkDump | Búsqueda dark web | git |
| TorBot | OSINT dark web | git |
| Onioff | Inspector URLs .onion | git |
| H8mail | Búsqueda brechas email | pip |
| Pwndb | Búsqueda credenciales filtradas | git |
| Proxychains | Rutear tráfico por proxies | apt |

</details>

<details>
<summary>📍 Geolocation & Image OSINT (80+ tools)</summary>

| Tool | Descripción | Install |
|------|-------------|---------|
| ExifTool | Extractor metadata imágenes | apt |
| Sherloq | Forense de imágenes | git |
| Stegoveritas | Detección esteganografía | pip |
| Steghide | Herramienta esteganografía | apt |
| Binwalk | Análisis firmware | apt |
| Creepy | OSINT geolocalización | git |
| Foremost | Recuperación archivos | apt |

</details>

<details>
<summary>💥 Data Breach & Credential Analysis (100+ tools)</summary>

| Tool | Descripción | Install |
|------|-------------|---------|
| H8mail | Verificador brechas email | pip |
| Holehe | Cuentas registradas con email | pip |
| Buster | OSINT email | git |
| Infoga | Info recopilación email | git |
| theHarvester | Cosechador emails | apt |
| Breach-Parse | Parsear dumps credenciales | git |
| Pwndb | Búsqueda DB filtradas | git |
| LeakLooker | Buscador de filtraciones | git |
| Mosint | OSINT email | go |
| Phoneinfoga | OSINT números telefónicos | go |
| Ignorant | OSINT teléfono | pip |

</details>

<details>
<summary>📱 Phone Number OSINT (40+ tools)</summary>

| Tool | Descripción | Install |
|------|-------------|---------|
| Phoneinfoga | Escáner números telefónicos | go |
| Ignorant | OSINT teléfono | pip |
| Moriarty-Project | Recon telefónico | git |
| PhoneNumber-OSINT | Recopilación info teléfono | git |
| Truecaller CLI | Búsqueda Truecaller | pip |
| franktool.py | Módulo teléfono AR/UY/PE | Python |

</details>

<details>
<summary>🔓 Password & Hash Cracking (80+ tools)</summary>

| Tool | Descripción | Install |
|------|-------------|---------|
| Hashcat | Crackeador GPU | apt |
| John the Ripper | Crackeador contraseñas | apt |
| Hydra | Brute-force login red | apt |
| Medusa | Brute-forcer paralelo | apt |
| Aircrack-ng | Crackeador WiFi | apt |
| Hash-identifier | Detector tipo hash | pip |
| Name-that-hash | Identificador hash | pip |
| CeWL | Generador wordlist custom | apt |
| Cupp | Perfilador contraseñas | pip |

</details>

<details>
<summary>🌍 Web Application Testing (200+ tools)</summary>

| Tool | Descripción | Install |
|------|-------------|---------|
| Burp Suite | Proxy/escáner web | apt |
| OWASP ZAP | Escáner apps web | apt |
| Nikto | Escáner servidor web | apt |
| Gobuster | Brute-force dirs/DNS | apt |
| Ffuf | Fuzzer web rápido | go |
| SQLmap | Herramienta inyección SQL | apt |
| XSStrike | Escáner XSS | pip |
| Dalfox | Finder XSS | go |
| Nuclei | Escáner vulnerabilidades | go |
| Katana | Web crawler | go |
| Arjun | Descubrimiento params HTTP | pip |
| Paramspider | Minería de parámetros | pip |
| Wpscan | Escáner WordPress | apt |
| Whatweb | Detector tecnología web | apt |
| Wafw00f | Detector WAF | pip |
| Sublist3r | Listado subdominios | pip |

</details>

<details>
<summary>📡 WiFi & Wireless (60+ tools)</summary>

| Tool | Descripción | Install |
|------|-------------|---------|
| Aircrack-ng | Suite seguridad WiFi | apt |
| Wifite | Crackeador WiFi auto | apt |
| Kismet | Detector wireless | apt |
| Reaver | Ataque WPS | apt |
| Wifiphisher | Framework AP falso | apt |
| Fluxion | Ataque phishing WiFi | git |
| Bettercap | Monitor/ataque red | apt |

</details>

<details>
<summary>🖥️ Privilege Escalation (80+ tools)</summary>

| Tool | Descripción | Install |
|------|-------------|---------|
| LinPEAS | Script privesc Linux | git |
| WinPEAS | Script privesc Windows | git |
| Linux-exploit-suggester | Sugeridor exploits kernel | git |
| Pspy | Monitor de procesos | git |
| Mimikatz | Dumper credenciales Windows | git |
| LaZagne | Recuperación contraseñas | pip |
| Kerbrute | Brute-force Kerberos | go |
| Impacket | Suite protocolos Windows | pip |
| Evil-WinRM | Shell WinRM | apt |

</details>

<details>
<summary>🔎 OSINT Frameworks (50+ tools)</summary>

| Tool | Descripción | Install |
|------|-------------|---------|
| Spiderfoot | OSINT automatizado | pip |
| Recon-ng | Framework recon | apt |
| Maltego | OSINT visual | apt |
| Datasploit | Framework OSINT | git |
| IntelOwl | Plataforma OSINT | git |
| Sn0int | Framework OSINT | apt |
| Photon | Crawler OSINT rápido | pip |
| Gasmask | Herramienta OSINT | git |
| Striker | Recolección info ofensiva | git |
| Raccoon | Herramienta recon ofensiva | pip |
| OSRFramework | Framework OSINT | pip |
| OWASP Amass | Mapeo superficie ataque | apt |

</details>

---

## 📁 Estructura del proyecto

```
franktool/
├── README.md        ← este archivo
├── franktool.py     ← OSINT interactivo AR/UY/PE
├── install.sh       ← instalador automático 1000+ tools
└── tools.md         ← lista completa de referencias
```

---

<div align="center">

**made with 🖤 by shizzafrank | **

*"I just pass the gear, what you do with it is on you, chief."*

</div>
