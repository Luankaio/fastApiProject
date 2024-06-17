import json
from models.curriculum import Curriculum

class JsonDB():
    def __init__(self, path:str):
       self.path = path

    def read(self):
        with open(self.path, 'r') as f:
            data = json.load(f)
        return data
    
    def insert(self, curriculum:Curriculum):
        data = self.read()
        data['curriculum'].append(curriculum.to_dict())
        f = open(self.path, 'w')
        f.write(json.dumps(data))
        f.close