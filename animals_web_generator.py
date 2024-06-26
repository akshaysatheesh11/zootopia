import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    if 'Name' in animal:
        print(f"Name: {animal['Name']}")
    if 'Diet' in animal:
        print(f"Diet: {animal['Diet']}")
    if 'locations' in animal and animal['locations']:
        print(f"Location: {animal['locations'][0]}")
    if 'Type' in animal:
        print(f"Type: {animal['Type']}")
    print() 

