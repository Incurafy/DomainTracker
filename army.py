# army.py

from unit import Unit

class Army:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.units = []
        
    # Add a unit to the army
    def recruit(self, unit: Unit):
        self.units.push(unit)
    
    # Remove a unit from the army
    def dismiss(self, index):
        self.units.pop(index)
        
    # Set the x/y coordinates of the army on the campaign map
    def set_coords(self, x, y):
        self.x = x
        self.y = y
        
    def print(self):
        return (self.units + " " + len(self.units))

    def desc(self):
        return "X: " + self.x + " Y: " + self.y + " " + self.units[0].desc()