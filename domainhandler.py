# domainhandler.py

import jsonpickle
from pathlib import Path
from os.path import exists

FILE_NAME = "domains.json"

class DomainHandler:
    def __init__(self):
        self.domains = []
        self.load()
        
    def load(self):
        if exists(FILE_NAME):
            self.domains = jsonpickle.decode(Path(FILE_NAME).read_text())

    def save(self):
        file = open(FILE_NAME, 'w')
        file.write(jsonpickle.encode(self.domains))
        file.close()
    
    # Use 'if index is not None:' as error handling
    def find_index_by_name(self, name):
        index = -1
        for d in self.domains:
            index += 1
            if d.name == name:
                return index
    
    def add(self, domain):
        self.domains.append(domain)
    
    def remove(self, domain):
        self.domains.remove(domain)
