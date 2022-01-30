# domain.py

class DomainType:
    def __init__(self, diplomacy, espionage, lore, operations, communications, resolve, resources):
        self.diplomacy = diplomacy
        self.espionage = espionage
        self.lore = lore
        self.operations = operations
        self.communications = communications
        self.resolve = resolve
        self.resources = resources

class Domain:
    def __init__(self, name, type: DomainType):
        self.name = name
        self.type = type
        self.settlements = []
        self.armies = []
    
    # Add a settlement to the domain
    def conquer_settlement(self, settlement):
        self.settlements.append(settlement)
        
    # Remove a settlement from the domain
    def lose_settlement(self, index):
        self.settlements.pop(index)
    
    # Add an army to the domain
    def raise_army(self, army):
        self.armies.append(army)
        
    # Remove an army from the domain
    def disband_army(self, index):
        self.armies.pop(index)
    
    # Create a new unit without an army
    def raise_unit(self, settlement, name, experience, equipment, type, size, tier):
        new_unit = None
        for s in self.settlements:
            if s.name == settlement:
                s.raise_unit(name, experience, equipment, type, size, tier)
                new_unit = s.assign_unit(0)
                break
        return new_unit
    
    def print(self):
        return (self.name + ": " + self.type + " " + self.diplomacy + " "
                + self.espionage + " " + self.lore + " " + self.operations
                + " " + self.communications + " " + self.resolve + " " + self.resources
                + " " + self.settlements + " " + self.armies)
    
    def desc(self):
        return self.name + " " + self.settlements[0].desc() + " " + self.armies[0].desc()