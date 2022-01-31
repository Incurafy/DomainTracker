# stronghold.py

from enum import Enum
import utils

class StrongholdType(Enum):
    KEEP = 0
    TOWER = 1
    TEMPLE = 2
    ESTABLISHMENT = 3
    
    def desc(self):
        match self:
            case StrongholdType.KEEP:
                return "keep"
            case StrongholdType.TOWER:
                return "tower"
            case StrongholdType.TEMPLE:
                return "temple"
            case StrongholdType.ESTABLISHMENT:
                return "establishment"
            case _:
                return "butts"

class StrongholdSize(Enum):
    SIZE_1 = 0
    SIZE_2 = 1
    SIZE_3 = 2
    SIZE_4 = 3
    SIZE_5 = 4
            
    def desc(self):
        match self:
            case StrongholdSize.SIZE_1:
                return "1"
            case StrongholdSize.SIZE_2:
                return "2"
            case StrongholdSize.SIZE_3:
                return "3"
            case StrongholdSize.SIZE_4:
                return "4"
            case StrongholdSize.SIZE_5:
                return "5"
            case _:
                return "kawaiiii"

class Stronghold:    
    def __init__(self, name, type:StrongholdType, size: StrongholdSize):
        self.name = name
        self.type = type
        self.size = size
        self.stronghold_die = utils.calc_die(size)
        self.garrison = []
        self.garrison_size = 0
        self.calc_garrison_size() 
        
    def calc_garrison_size(self):
        match self.type:
            case StrongholdType.KEEP:
                self.garrison_size = (self.size + 1) * 2
            case StrongholdType.TOWER:
                if self.size == StrongholdSize.SIZE_3 or self.size == StrongholdSize.SIZE_4:
                    self.garrison_size = 1
                elif self.size == StrongholdSize.SIZE_5:
                    self.garrison_size = 2
            case StrongholdType.TEMPLE:
                if self.size == StrongholdSize.SIZE_3 or self.size == StrongholdSize.SIZE_4:
                    self.garrison_size = 1
                elif self.size == StrongholdSize.SIZE_5:
                    self.garrison_size = 2
            case StrongholdType.ESTABLISHMENT:
                self.garrison_size = 0
