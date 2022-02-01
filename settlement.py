# settlement.py

from enum import Enum
from unit import Unit
import utils
import ancestry

class SettlementType(Enum):
    VILLAGE = 1
    SMALL_TOWN = 2
    LARGE_TOWN = 3
    SMALL_CITY = 4
    LARGE_CITY = 5
    METROPOLIS = 6
    
    def desc(self):
        match self:
            case SettlementType.VILLAGE:
                return "village"
            case SettlementType.SMALL_TOWN:
                return "small town"
            case SettlementType.LARGE_TOWN:
                return "large town"
            case SettlementType.SMALL_CITY:
                return "small city"
            case SettlementType.LARGE_CITY:
                return "large city"
            case SettlementType.METROPOLIS:
                return "metropolis"
            case _:
                return "your anus"
            
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
                return 1
            case SettlementSize.SMALL_TOWN:
                return 2
            case SettlementSize.LARGE_TOWN:
                return 3
            case SettlementSize.SMALL_CITY:
                return 4
            case SettlementSize.LARGE_CITY:
                return 5
            case SettlementSize.METROPOLIS:
                return 6
            case _:
                return 69
            
class Settlement:
    # resource die
    # number of currently raised units
    # maximum number of units that can be raised
    # garrison status
    # list of garrisoned units
    
    def __init__(self, name, ancestry: ancestry.Ancestry, size: SettlementSize, map_x, map_y):
        self.name = name
        self.ancestry = ancestry
        self.size = size
        self.settlement_die = utils.calc_die(size)
        self.unassigned_units = [] # list of units from this settlement without armies
        self.strongholds = [] # list of strongholds in the settlement
        self.map_x = map_x
        self.map_y = map_y
    
    # Create a unit and add it to the unassigned_units list
    def raise_unit(self, name, experience, equipment, type, size, tier):
        unassigned_unit = Unit(name, self.name)
        unassigned_unit.set_ancestry(self.ancestry)
        unassigned_unit.set_experience(experience)
        unassigned_unit.set_equipment(equipment)
        unassigned_unit.set_type(type)
        unassigned_unit.set_size(size)
        unassigned_unit.set_tier(tier)
        self.unassigned_units.append(unassigned_unit)
    
    # Remove a unit from the unassigned_units list and return it so that it may be assigned to an army or garrison
    def assign_unit(self, index):
        return self.unassigned_units.pop(index)
    
    def desc(self):
        return ("Name: " + self.name + " Ancestry: " + self.ancestry.desc() + " " + str(self.size.desc()) 
                + " Unassigned Units: " + str(len(self.unassigned_units))
                + " Settlement Die: d" + str(self.settlement_die))