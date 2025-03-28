import json
import os

DB_FILE = "data/recognized_objects.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def save_recognized_object(obj_name):
    db = load_db()
    if obj_name not in db:
        db[obj_name] = {"count": 1}
    else:
        db[obj_name]["count"] += 1
    save_db(db)

def get_recognized_objects():
    return load_db()
