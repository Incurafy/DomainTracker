# utils.py

# Cacuate the size of a die where:
# 1 = d4,  2 = d6,  3 = d8,
# 4 = d10, 5 = d12, 6 = d20
def calc_die(size):
    if size.value == 6:
        return 20
    elif size.value > 0 and size.value < 6:
        return (size.value + 1) * 2
    else:
        return 0