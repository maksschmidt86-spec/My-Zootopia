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

    # Details in einem <div class="card__text"> mit innerer <ul>
    output += '  <div class="card__text">\n'
    output += '    <ul class="animal-details">\n'

    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += f'      <li><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n'

    if 'locations' in animal_obj:
        output += f'      <li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'

    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f'      <li><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n'

    # Bonus-Felder (optional)
    if 'characteristics' in animal_obj and 'lifespan' in animal_obj['characteristics']:
        output += f'      <li><strong>Lifespan:</strong> {animal_obj["characteristics"]["lifespan"]}</li>\n'

    if 'characteristics' in animal_obj and 'top_speed' in animal_obj['characteristics']:
        output += f'      <li><strong>Top Speed:</strong> {animal_obj["characteristics"]["top_speed"]}</li>\n'

    if 'characteristics' in animal_obj and 'habitat' in animal_obj['characteristics']:
        output += f'      <li><strong>Habitat:</strong> {animal_obj["characteristics"]["habitat"]}</li>\n'

    output += '    </ul>\n'
    output += '  </div>\n'
    output += '</li>\n\n'

    return output


def main():
    """Hauptfunktion: Lädt Daten und Template, generiert HTML"""
    animals_data = load_data('animals_data.json')
    template = load_template('animals_template.html')

    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    final_html = template.replace('__REPLACE_ANIMALS_INFO__', output)

    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("HTML-Datei wurde generiert: animals.html")


if __name__ == '__main__':
    main()