import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    return round(sum([i['score']*i['weight'] for i in data]), 3)

print(task())
