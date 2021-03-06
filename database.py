import json
from tinydb import TinyDB, Query

db = TinyDB('database.json')

cz_table = db.table('chinese_zodiac')
wz_table = db.table('western_zodiac')

def insert_animal(name, characteristics, position):
    animal = {
        "animal": name,
        "characteristics": characteristics,
        "position": position
    }
    cz_table.insert(animal)
    return animal

def find_animal(name):
    animal_query = Query()
    result = cz_table.search(animal_query.animal.matches(name))
    if (len(result) > 0):
        return result[0]
    return None

def update_animal(name, **kwargs):
    animal_query = Query()
    result = cz_table.search(animal_query.animal.matches(name))

    # update the first entry
    if len(result) > 0:
        target = result[0]
        target_id = target.doc_id
        animal = kwargs.get("animal", target["animal"])
        characteristics = kwargs.get("characteristics", target["characteristics"])
        position = kwargs.get("position", target["position"])
        updated_record = {
            "animal": animal,
            "characteristics": characteristics,
            "position": position
        }
        cz_table.update(updated_record, doc_ids=[target_id])
        return updated_record
    return None

def delete_animal(name):
    animal_query = Query()
    result = cz_table.search(animal_query.animal.matches(name))

    # delete the first entry
    if len(result) > 0:
        target = result[0]
        target_id = target.doc_id
        cz_table.remove(doc_ids=[target_id])
        return True
    return False

def get_animals():
    return cz_table.all()