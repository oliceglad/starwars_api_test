
import requests
import json
from typing import List

def add_pilot(data, key: str) -> List:
    pilots = []
    for i_pilot in data[key]:
        request_pilot = requests.get(i_pilot)
        pilot = json.loads(request_pilot.text)
        new_pilot = {}
        for key in pilot.keys():
            if key in ('name', 'height', 'mass', 'homeworld'):
                new_pilot[key] = pilot[key]
        pilots.append(new_pilot)
    return pilots


new_data = {}
try:
    result = requests.get('https://swapi.dev/api/starships/10')
    if result.status_code == 200:
        data = json.loads(result.text)

        for key in data.keys():
            if key in ('name', 'max_atmosphering_speed', 'starship_class'):
                new_data[key] = data[key]
            elif key == 'pilots':
                new_data[key] = add_pilot(data, key)

        with open('starship_info.json', 'w') as file:
            json.dump(new_data, file, indent=4)
            print(json.dumps(new_data, indent=4))
    else:
        raise ValueError('Ошибка')
except ValueError as exc:
    print(exc)
