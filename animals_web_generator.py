import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, 'r', encoding='utf-8') as handler:
        return json.load(handler)


def load_template(file_path):
    """Loads an HTML template file"""
    with open(file_path, 'r', encoding='utf-8') as handler:
        return handler.read()


def serialize_animal(animal_obj):
    """Serialisiert ein einzelnes Tierobjekt in HTML"""
    output = ''
    output += '<li class="cards__item">\n'

    # Name als Titel
    if 'name' in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    # Details in einem <p class="card__text"> mit <strong> Labels
    output += '  <p class="card__text">\n'

    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += f'    <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'

    if 'locations' in animal_obj:
        output += f'    <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f'    <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n\n'

    return output


def main():
    """Hauptfunktion: Lädt Daten und Template, generiert HTML"""
    # Daten und Template laden
    animals_data = load_data('animals_data.json')
    template = load_template('animals_template.html')

    # HTML für alle Tiere generieren
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    # Platzhalter ersetzen
    final_html = template.replace('__REPLACE_ANIMALS_INFO__', output)

    # In animals.html schreiben
    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("HTML-Datei wurde generiert: animals.html")


# Skript ausführen
if __name__ == '__main__':
    main()