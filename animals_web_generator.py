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
animals_info = ""

for animal in animals_data:
    animals_info += '<li class="cards__item">\n'

    if 'name' in animal:
        animals_info += f'  <div class="card__title">{animal["name"]}</div>\n'

    animals_info += '  <div class="card__text">\n'

    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        animals_info += f'    Diet: {animal["characteristics"]["diet"]}<br>\n'

    if 'locations' in animal:
        animals_info += f'    Location: {animal["locations"][0]}<br>\n'

    if 'characteristics' in animal and 'type' in animal['characteristics']:
        animals_info += f'    Type: {animal["characteristics"]["type"]}<br>\n'

    animals_info += '  </div>\n'
    animals_info += '</li>\n\n'

# 3. __REPLACE_ANIMALS_INFO__ durch den erzeugten String ersetzen
final_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_info)

# 4. In animals.html schreiben (mit UTF-8!)
with open('animals.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("HTML-Datei wurde generiert: animals.html")