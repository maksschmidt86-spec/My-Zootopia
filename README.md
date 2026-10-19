# 🐾 My-Zootopia - Animal Repository

Ein Python-Projekt, das Tierdaten aus einer JSON-Datei liest und dynamisch eine formatierte HTML-Webseite generiert.

##  Über das Projekt

Dieses Projekt wurde im Rahmen des MSIT-Studiums erstellt. Es demonstriert folgende Konzepte:
- **Templating**: Dynamisches Einfügen von Daten in HTML-Vorlagen
- **JSON-Verarbeitung**: Lesen und Verarbeiten strukturierter Daten
- **Git & GitHub**: Versionskontrolle und Code-Management
- **Python Best Practices**: PEP 8-konformer Code mit Funktionen

##  Features

- Liest Tierdaten aus `animals_data.json`
- Generiert eine formatierte HTML-Seite mit Karten-Layout
- Filtert Tiere nach Hauttyp (Bonus-Feature)
- Saubere Code-Struktur mit separaten Funktionen
- UTF-8-Encoding für korrekte Darstellung von Sonderzeichen

## ️ Voraussetzungen

- Python 3.6+
- Keine externen Bibliotheken erforderlich (nur die Standardbibliothek `json`)

##  Projektstruktur

```text
My-Zootopia/
├── animals_data.json          # Tierdaten im JSON-Format
├── animals_template.html      # HTML-Vorlage mit CSS
├── animals_web_generator.py   # Python-Skript zur HTML-Generierung
├── animals.html               # Generierte HTML-Ausgabe
└── README.md                  # Diese Datei