# ancestry.py

from enum import Enum

class Ancestry(Enum):
    HUMAN = 1
    DWARF = 2
    
    def desc(self):
        match self:
            case Ancestry.HUMAN:
                return "human"
            case Ancestry.DWARF:
                return "dwarf"
            case _:
                return "catgirls"

    def attack_bonus(self):
        match self:
            case Ancestry.HUMAN:
                return 1
            case Ancestry.DWARF:
                return 1
            case _:
                return 0
            
    def defence_bonus(self):
        match self:
            case Ancestry.HUMAN:
                return 2
            case Ancestry.DWARF:
                return 2
            case _:
                return 0
    
    def power_bonus(self):
        match self:
            case _:
                return 0
            
    def toughness_bonus(self):
        match self:
            case Ancestry.HUMAN:
                return 0
            case Ancestry.DWARF:
                return 2
            case _:
                return 0
            
    def morale_bonus(self):
        match self:
            case Ancestry.HUMAN:
                return 1
            case Ancestry.DWARF:
                return 0
            case _:
                return 0
    
    def command_bonus(self):
        match self:
            case Ancestry.HUMAN:
                return 1
            case Ancestry.DWARF:
                return 0
            case _:
                return 0
