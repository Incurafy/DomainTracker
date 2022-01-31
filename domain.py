# domain.py

import utils
from enum import Enum

class DomainType:
    def __init__(self, diplomacy, espionage, lore, operations, communications, resolve, resources):
        self.diplomacy = diplomacy
        self.espionage = espionage
        self.lore = lore
        self.operations = operations
        self.communications = communications
        self.resolve = resolve
        self.resources = resources
        
    # do this for each of the domain types
    def adventuring_party():
        return DomainType(-1, 0, 1, 2, 11, 12, 10)
    
class DomainSize(Enum):
    SIZE_1 = 1
    SIZE_2 = 2
    SIZE_3 = 3
    SIZE_4 = 4
    SIZE_5 = 5
    
    def desc(self):
        match self:
            case DomainSize.SIZE_1:
                return "1"
            case DomainSize.SIZE_2:
                return "2"
            case DomainSize.SIZE_3:
                return "3"
            case DomainSize.SIZE_4:
                return "4"
            case DomainSize.SIZE_5:
                return "5"
            case _:
                return "80085"
    
class Domain:
    def __init__(self, name, type: DomainType, size: DomainSize):
        self.name = name
        self.type = type
        self.settlements = []
        self.armies = []
        self.size = size
        self.power_die = utils.calc_die(self.size)
    
    # Add a settlement to the domain
    def add_settlement(self, settlement):
        self.settlements.append(settlement)
        
    # Remove a settlement from the domain
    def remove_settlement(self, index):
        self.settlements.pop(index)
    
    # Add an army to the domain
    def add_army(self, army):
        self.armies.append(army)
        
    # Remove an army from the domain
    def remove_army(self, index):
        self.armies.pop(index)
    
    # Create a new unit without an army
    def create_unit(self, settlement, name, experience, equipment, type, size, tier):
        new_unit = None
        for s in self.settlements:
            if s.name == settlement:
                s.raise_unit(name, experience, equipment, type, size, tier)
                new_unit = s.assign_unit(0)
                break
        return new_unit
        
    def desc(self):
        return self.name + " " + self.settlements[0].desc() + " " + self.armies[0].desc()
