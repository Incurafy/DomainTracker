# army.py

from unit import Unit

class Army:
    def __init__(self, name, map_x, map_y):
        self.name = name
        self.map_x = map_x
        self.map_y = map_y
        self.units = []
        
    # Add a unit to the army
    def add_unit(self, unit: Unit):
        self.units.append(unit)
    
    # Remove a unit from the army
    def remove_unit(self, index):
        self.units.pop(index)
        
    # Set the x/y coordinates of the army on the campaign map
    def set_coords(self, x, y):
        self.x = x
        self.y = y
        
    def print(self):
        return (self.units + " " + len(self.units))

    def desc(self):
        return "Army - X: " + str(self.map_x) + " Y: " + str(self.map_y) + " " + self.units[0].desc()