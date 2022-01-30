# settlement.py

from enum import Enum
from unit import Unit

class Settlement:
    # name
    # ancestry
    # type
    # owner
    # size
    # resource die
    # number of currently raised units
    # maximum number of units that can be raised
    # strongholds (none or Type[Level])
    # list of raised units
    # garrison status
    # list of garrisoned units
    
    def __init__(self, name, ancestry, size):
        self.name = name
        self.ancestry = ancestry
        self.size = size
        self.free_units = [] # list of units from this settlement without armies
        self.strongholds = [] # list of strongholds in the settlement
    
    # Create a unit and add it to the free_units list
    def raise_unit(self, name, experience, equipment, type, size, tier):
        free_unit = Unit(name, self.name)
        free_unit.set_ancestry(self.ancestry)
        free_unit.set_experience(experience)
        free_unit.set_equipment(equipment)
        free_unit.set_type(type)
        free_unit.set_size(size)
        free_unit.set_tier(tier)
        self.free_units.append(free_unit)
    
    # Remove a unit from the free_units list and return it so that it may be assigned to an army or garrison
    def assign_unit(self, index):
        return self.free_units.pop(index)
    
    def desc(self):
        return self.name + " " + self.ancestry.desc() + " " + self.size.desc() + " num free units: " + str(len(self.free_units))
        
class SettlementSize(Enum):
    VILLAGE = 1
    SMALL_TOWN = 2
    LARGE_TOWN = 3
    SMALL_CITY = 4
    LARGE_CITY = 5
    METROPOLIS = 6
    
    def desc(self):
        match self:
            case SettlementSize.VILLAGE:
                return "village"
            case SettlementSize.SMALL_TOWN:
                return "small town"
            case SettlementSize.LARGE_TOWN:
                return "large town"
            case SettlementSize.SMALL_CITY:
                return "small city"
            case SettlementSize.LARGE_CITY:
                return "large city"
            case SettlementSize.METROPOLIS:
                return "metropolis"
            case _:
                return "your anus"