# main.py

import unit
#import army
import domain
import settlement
import jsonpickle
from pathlib import Path

def main():
    dom = domain.Domain("Test Domain", domain.DomainType(1, 1, 1, 1, 10, 10, 10))
    dom.conquer_settlement(settlement.Settlement("Testville", unit.Ancestry.HUMAN, settlement.SettlementSize.VILLAGE))
    dom.raise_army(dom.raise_unit("Testville", "The Testy Terrors", unit.Experience.VETERAN, unit.Equipment.HEAVY, unit.Type.INFANTRY, unit.Size.D6, 1))
    print(dom.desc())
    
    file = open("data.json", 'w')
    file.write(jsonpickle.encode(dom))
    file.close()
    
    data = Path("data.json").read_text()
    newdom = jsonpickle.decode(data)
    print(newdom.desc())
    
    for i in range(len(newdom.settlements)):
        print(newdom.settlements[i].desc())

print()
main()
print()