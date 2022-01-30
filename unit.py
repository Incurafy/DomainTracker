# unit.py

from enum import Enum

BASE_DEFENCE = 10
BASE_TOUGHNESS = 10
BASE_DAMAGE = 1
BASE_DAMAGE_CAV = 2
BASE_NUM_ATTACKS = 1

class Unit:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
        self.experience = Experience.REGULAR
        self.equipment = Equipment.LIGHT
        self.ancestry = Ancestry.HUMAN
        self.type = UnitType.INFANTRY
        self.size = UnitSize.D6
        self.casualties = self.size.max_casualties()
        self.tier = 1
        self.movement = 1
    
    def desc(self):
        return (self.name + " " + self.origin + " " + self.experience.desc() + " " + self.equipment.desc()
                + " " + self.ancestry.desc() + " " + self.type.desc() + " " + self.size.desc() + " " + str(self.casualties)
                + " " + str(self.tier))
    
    def attack(self):
        return self.type.attack_bonus(self.experience) + self.ancestry.attack_bonus()
    
    def defence(self):
        return BASE_DEFENCE + self.type.defence_bonus(self.experience) + self.ancestry.defence_bonus()
        
    def toughness(self):
        return BASE_TOUGHNESS + self.type.toughness_bonus(self.equipment) + self.ancestry.toughness_bonus()
    
    def morale(self):
        return self.type.morale_bonus(self.experience) + self.ancestry.morale_bonus()
    
    def command(self):
        return self.type.command_bonus(self.experience) + self.ancestry.command_bonus()
    
    def attack_damage(self):
        return BASE_DAMAGE
    
    def power_damage(self):
        if self.type == UnitType.CAVALRY:
            return BASE_DAMAGE_CAV + self.type.damage_bonus(self.equipment)
        else:
            return BASE_DAMAGE + self.type.damage_bonus(self.equipment)
        
    def num_attacks(self):
        return BASE_NUM_ATTACKS + self.type.additional_attacks(self.experience)

    def set_experience(self, experience):
        self.experience = experience
        
    def set_equipment(self, equipment):
        self.equipment = equipment
        
    def set_ancestry(self, ancestry):
        self.ancestry = ancestry
        
    def set_type(self, type):
        self.type = type

    def set_size(self, size):
        self.size = size
        self.casualties = self.size.max_casualties()
        
    def set_casualties(self, amount):
        self.casualties = amount
    
    def set_tier(self, tier):
        self.tier = tier

class Experience(Enum):
    LEVIES = 0
    REGULAR = 1
    VETERAN = 2
    ELITE = 3
    SUPER_ELITE = 4
    
    def desc(self):
        match self:
            case Experience.LEVIES:
                return "levies"
            case Experience.REGULAR:
                return "regular"
            case Experience.VETERAN:
                return "veteran"
            case Experience.ELITE:
                return "elite"
            case Experience.SUPER_ELITE:
                return "super elite"
            case _:
                return "dick"
    
class Equipment(Enum):
    LIGHT = 0
    MEDIUM = 1
    HEAVY = 2
    SUPER_HEAVY = 3
    
    def desc(self):
        match self:
            case Equipment.LIGHT:
                return "light"
            case Equipment.MEDIUM:
                return "medium"
            case Equipment.HEAVY:
                return "heavy"
            case Equipment.SUPER_HEAVY:
                return "super heavy"
            case _:
                return "CULT PLUG"
    
class Ancestry(Enum):
    HUMAN = 0
    DWARF = 1
    
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
            
    def desc(self):
        match self:
            case Ancestry.HUMAN:
                return "human"
            case Ancestry.DWARF:
                return "dwarf"
            case _:
                return "tentacle monster"
    
class UnitType(Enum):
    INFANTRY = 0
    ARTILLERY = 1
    CAVALRY = 2
    AERIAL = 3
    
    def additional_attacks(self, experience: Experience):        
        match (self, experience):
            case (_, Experience.ELITE | Experience.SUPER_ELITE):
                return 1
            case (UnitType.ARTILLERY, Experience.VETERAN):
                return 1
            case _:
                return 0
            
    def attack_bonus(self, experience: Experience):
        match (self, experience):
            case (UnitType.INFANTRY, Experience.LEVIES):
                return -1
            case (_, Experience.REGULAR):
                return 0
            case (UnitType.INFANTRY | UnitType.CAVALRY | UnitType.AERIAL, Experience.VETERAN):
                return 1
            case (UnitType.INFANTRY | UnitType.CAVALRY | UnitType.AERIAL, Experience.ELITE):
                return 2
            case (UnitType.INFANTRY | UnitType.CAVALRY | UnitType.AERIAL, Experience.SUPER_ELITE):
                return 3
            case (UnitType.ARTILLERY, Experience.VETERAN):
                return 2
            case (UnitType.ARTILLERY, Experience.ELITE):
                return 4
            case (UnitType.ARTILLERY, Experience.SUPER_ELITE):
                return 6
            case _:
                return 0
        
    def defence_bonus(self, experience: Experience):
        match (self, experience):
            case (UnitType.INFANTRY, Experience.LEVIES):
                return -2
            case (_, Experience.REGULAR):
                return 0
            case (UnitType.INFANTRY, Experience.VETERAN):
                return 2
            case (UnitType.INFANTRY, Experience.ELITE):
                return 4
            case (UnitType.INFANTRY, Experience.SUPER_ELITE):
                return 6
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Experience.VETERAN):
                return 1
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Experience.ELITE):
                return 2
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Experience.SUPER_ELITE):
                return 3
            case _:
                return 0
            
    def morale_bonus(self, experience: Experience):
        match (self, experience):
            case (UnitType.INFANTRY, Experience.LEVIES):
                return -2
            case (_, Experience.REGULAR):
                return 0
            case (UnitType.INFANTRY, Experience.VETERAN):
                return 2
            case (UnitType.INFANTRY, Experience.ELITE):
                return 4
            case (UnitType.INFANTRY, Experience.SUPER_ELITE):
                return 6
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Experience.VETERAN):
                return 1
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Experience.ELITE):
                return 2
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Experience.SUPER_ELITE):
                return 3
            case _:
                return 0
        
    def command_bonus(self, experience: Experience):
        match (self, experience):
            case (UnitType.INFANTRY, Experience.LEVIES):
                return -1
            case (_, Experience.REGULAR):
                return 0
            case (UnitType.INFANTRY, Experience.VETERAN):
                return 0
            case (UnitType.INFANTRY, Experience.ELITE | Experience.SUPER_ELITE):
                return 1
            case (UnitType.CAVALRY | UnitType.AERIAL, Experience.VETERAN):
                return 2
            case (UnitType.CAVALRY | UnitType.AERIAL, Experience.ELITE):
                return 4
            case (UnitType.CAVALRY | UnitType.AERIAL, Experience.SUPER_ELITE):
                return 6
            case (UnitType.ARTILLERY, Experience.VETERAN):
                return 1
            case (UnitType.ARTILLERY, Experience.ELITE):
                return 2
            case (UnitType.ARTILLERY, Experience.SUPER_ELITE):
                return 3
            case _:
                return 0
            
    def power_bonus(self, equipment: Equipment):
        match (self, equipment):
            case (_, Equipment.LIGHT):
                return 0
            case (UnitType.INFANTRY, Equipment.MEDIUM):
                return 2
            case (UnitType.INFANTRY, Equipment.HEAVY):
                return 4
            case (UnitType.INFANTRY, Equipment.SUPER_HEAVY):
                return 6
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Equipment.LIGHT):
                return 0
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Equipment.MEDIUM):
                return 1
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Equipment.HEAVY):
                return 2
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Equipment.SUPER_HEAVY):
                return 3
            case _:
                return 0
    
    def toughness_bonus(self, equipment: Equipment):
        match (self, equipment):
            case (_, Equipment.LIGHT):
                return 0
            case (UnitType.INFANTRY, Equipment.MEDIUM):
                return 2
            case (UnitType.INFANTRY, Equipment.HEAVY):
                return 4
            case (UnitType.INFANTRY, Equipment.SUPER_HEAVY):
                return 6
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Equipment.LIGHT):
                return 0
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Equipment.MEDIUM):
                return 1
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Equipment.HEAVY):
                return 2
            case (UnitType.CAVALRY | UnitType.AERIAL | UnitType.ARTILLERY, Equipment.SUPER_HEAVY):
                return 3
            case _:
                return 0
    
    def damage_bonus(self, equipment: Equipment):
        match (self, equipment):
            case (UnitType.INFANTRY | UnitType.CAVALRY | UnitType.AERIAL, Equipment.SUPER_HEAVY):
                return 1
            case _:
                return 0

    def desc(self):
        match self:
            case UnitType.INFANTRY:
                return "infantry"
            case UnitType.CAVALRY:
                return "cavalry"
            case UnitType.AERIAL:
                return "aerial"
            case UnitType.ARTILLERY:
                return "artillery"
            case _:
                return "egirl"
            
class UnitSize(Enum):
    D4 = 0
    D6 = 1
    D8 = 2
    D10 = 3
    D12 = 4
    
    def max_casualties(self):
        match self:
            case UnitSize.D4:
                return 4
            case UnitSize.D6:
                return 6
            case UnitSize.D8:
                return 8
            case UnitSize.D10:
                return 10
            case UnitSize.D12:
                return 12
            
    def desc(self):
        match self:
            case UnitSize.D4:
                return "4"
            case UnitSize.D6:
                return "6"
            case UnitSize.D8:
                return "8"
            case UnitSize.D10:
                return "10"
            case UnitSize.D12:
                return "12"
            case _:
                return "20"