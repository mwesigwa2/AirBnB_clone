#!/usr/bin/python3
import json


class FileStorage():
    __objects = {}
    __file_path = "file.json"

    def all(self):
        pass

    def save(self):
        try:
            with open(FileStorage, "w") as f:
                json.dump(FileStorage.__obejcts, f)
        except Exception:
            pass

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except Exception:
            pass

    def new(self, obj):
        name = obj.__class__.__name__
        FileStorage.__objects[name + "." + obj.id] = obj.to_dict()
