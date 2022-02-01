# main.py

from ancestry import Ancestry
from domain import *
from settlement import *
from unit import *
from army import *
from domainhandler import DomainHandler

def main():
    d_handler = DomainHandler()
    
    # Create a domain for the Players
    d_party = Domain("Players", DomainType.adventuring_party(), DomainSize.SIZE_1)
    
    # Create a settlement called Homesville
    s_homesville = Settlement("Homesville", Ancestry.HUMAN, SettlementSize.VILLAGE, 0, 0)
    
    # Create a unit and add it to the unassigned_units list within s_homesville
    s_homesville.raise_unit("Homesville Guard", Experience.REGULAR, Equipment.MEDIUM, UnitType.INFANTRY, UnitSize.MEDIUM, 1)
    
    # Remove the unit at index 0 from the unassigned_units list within s_homesville and assign to u_guard
    u_guard = s_homesville.assign_unit(0)
    
    # Create an unassigned army which will have no units in its units list
    a_army = Army("Player Army", 0, 0)
    
    # Add the u_guard unit to the army's units list
    a_army.add_unit(u_guard)
    
    # Add the Homesville settlement to the Players domain
    d_party.add_settlement(s_homesville)
    
    # Add the unassigned army to the Players domain
    d_party.add_army(a_army)

    # Add the Players domain to the domains list inside d_handler
    d_handler.add(d_party)
       
    # Save domain data
    d_handler.save()

print()
main()
print()