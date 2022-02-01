# main.py

from ancestry import Ancestry
import unit
import army
import domain
import settlement
import jsonpickle
from pathlib import Path

def main():
    domains = []
    
    # Create a domain for the Players
    d_party = domain.Domain("Players", domain.DomainType.adventuring_party(), domain.DomainSize.SIZE_1)
    
    # Create a settlement called Homesville
    s_homesville = settlement.Settlement("Homesville", Ancestry.HUMAN, settlement.SettlementSize.VILLAGE, 0, 0)
    
    # Create a unit and add it to the unassigned_units list within s_homesville
    s_homesville.raise_unit("Homesville Guard", unit.Experience.REGULAR, unit.Equipment.MEDIUM, unit.UnitType.INFANTRY, unit.UnitSize.MEDIUM, 1)
    
    # Remove the unit at index 0 from the unassigned_units list within s_homesville and assign to u_guard
    u_guard = s_homesville.assign_unit(0)
    
    # Create an unassigned army which will have no units in its units list
    a_army = army.Army("Player Army", 0, 0)
    
    # Add the u_guard unit to the army's units list
    a_army.add_unit(u_guard)
    
    # Add the Homesville settlement to the Players domain
    d_party.add_settlement(s_homesville)
    
    # Add the unassigned army to the Players domain
    d_party.add_army(a_army)

    # Add the Player domain to the domains list
    domains.append(d_party)

    # Save the domains list
    file = open("data.json", 'w')
    file.write(jsonpickle.encode(domains))
    file.close()
   
    # Load the domains list
    data = Path("data.json").read_text()
    domains = jsonpickle.decode(data)
    
    filtered = list(filter(lambda d: d.name == "Players", domains))
    
    print("Decoded: " + filtered[0].desc())
    
    filtered[0].name = "New Name"
    
    print("This should have new name: " + filtered[0].desc())
    
    
    file = open("data.json", 'w')
    file.write(jsonpickle.encode(domains))
    file.close()
    
    data = Path("data.json").read_text()
    domains = jsonpickle.decode(data)
    
    print(domains[0].desc())    

print()
main()
print()