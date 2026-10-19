import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, 'r', encoding='utf-8') as handler:
        return json.load(handler)


def load_template(file_path):
    """Loads an HTML template file"""
    with open(file_path, 'r', encoding='utf-8') as handler:
        return handler.read()


def get_available_skin_types(animals_data):
    """Sammelt alle verfügbaren skin_type-Werte aus den Daten"""
    skin_types = set()
    for animal in animals_data:
        if 'characteristics' in animal and 'skin_type' in animal['characteristics']:
            skin_types.add(animal['characteristics']['skin_type'])
    return sorted(skin_types)


def filter_animals_by_skin_type(animals_data, skin_type):
    """Filtert Tiere nach skin_type"""
    filtered = []
    for animal in animals_data:
        if 'characteristics' in animal and 'skin_type' in animal['characteristics']:
            if animal['characteristics']['skin_type'].lower() == skin_type.lower():
                filtered.append(animal)
    return filtered


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

    if 'characteristics' in animal_obj and 'skin_type' in animal_obj['characteristics']:
        output += f'      <li><strong>Skin Type:</strong> {animal_obj["characteristics"]["skin_type"]}</li>\n'

    if 'characteristics' in animal_obj and 'lifespan' in animal_obj['characteristics']:
        output += f'      <li><strong>Lifespan:</strong> {animal_obj["characteristics"]["lifespan"]}</li>\n'

    output += '    </ul>\n'
    output += '  </div>\n'
    output += '</li>\n\n'

    return output


def main():
    """Hauptfunktion: Lädt Daten, filtert nach skin_type und generiert HTML"""
    # Daten und Template laden
    animals_data = load_data('animals_data.json')
    template = load_template('animals_template.html')

    # Verfügbare skin_types anzeigen
    available_skin_types = get_available_skin_types(animals_data)
    print("Verfügbare Hauttypen:")
    for i, skin_type in enumerate(available_skin_types, 1):
        print(f"  {i}. {skin_type}")

    # Benutzer nach skin_type fragen
    selected_skin_type = input("\nBitte wähle einen Hauttyp (Name eingeben): ").strip()

    # Tiere filtern
    filtered_animals = filter_animals_by_skin_type(animals_data, selected_skin_type)

    if not filtered_animals:
        print(f"Keine Tiere mit dem Hauttyp '{selected_skin_type}' gefunden.")
        return

    print(f"\n{len(filtered_animals)} Tier(e) mit dem Hauttyp '{selected_skin_type}' gefunden.")

    # HTML für gefilterte Tiere generieren
    output = ''
    for animal_obj in filtered_animals:
        output += serialize_animal(animal_obj)

    # Platzhalter ersetzen
    final_html = template.replace('__REPLACE_ANIMALS_INFO__', output)

    # In animals.html schreiben
    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"HTML-Datei wurde generiert: animals.html (nur Tiere mit skin_type: {selected_skin_type})")


if __name__ == '__main__':
    main()