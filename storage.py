# storage.py

import jsonpickle
from pathlib import Path
from os.path import exists

class Storage:
    def __init__(self, fname):
        self.storage = self.load(fname)
        
    def load(self, fname):
        if exists(fname):
            return jsonpickle.decode(Path(fname).read_text())
        else:
            return []
       
    def store(self, data, fname):
        file = open(fname, 'w')
        file.write(jsonpickle.encode(data))
        file.close()
        
    def find(self, name):
        return list(filter(lambda x: x.name == name, self.storage))

