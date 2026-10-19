import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, 'r', encoding='utf-8') as handler:
        return json.load(handler)


def load_template(file_path):
    """Loads an HTML template file"""
    with open(file_path, 'r', encoding='utf-8') as handler:
        return handler.read()


# 1. Inhalt von animals_template.html lesen
template = load_template('animals_template.html')

# 2. String mit den Tierdaten erzeugen
animals_data = load_data('animals_data.json')
output = ""

for animal in animals_data:
    output += '<li class="cards__item">\n'

    # Name als Titel
    if 'name' in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    # Details in einem <p class="card__text"> mit <strong> Labels
    output += '  <p class="card__text">\n'

    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        output += f'    <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

    if 'locations' in animal:
        output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if 'characteristics' in animal and 'type' in animal['characteristics']:
        output += f'    <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n\n'

# 3. __REPLACE_ANIMALS_INFO__ durch den erzeugten String ersetzen
final_html = template.replace('__REPLACE_ANIMALS_INFO__', output)

# 4. In animals.html schreiben (WICHTIG: encoding='utf-8')
with open('animals.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("HTML-Datei wurde generiert: animals.html")