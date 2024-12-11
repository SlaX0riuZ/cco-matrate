import cubelist as cb

# OA: (1)Dye, Circuits, Plastic, Hamburger, (5)Filament, Patch, Dumbbells, Charcoal, Feather, (10)Resin, Shard, Tough Stuff, Iron Filament, Polish, (15)Ectoplasm, Pebble, Perfection,
# Poison, Ash, (20)New Tag, Vibrations, Water, Goo, Rubber, (25)Dust, Ice, Crystalline Shard, Strange Capacitor, Glint, (30)Cellulose, Magma Ball, Ghastly Eye, Jotunn Shard

rarity = ""
def check_rarity(arr, p, q):
    if arr[p][q] == "c": # Checking Rarity
            return 0
    elif arr[p][q] == "u":
            return 1
    elif arr[p][q] == "r":
            return 2
    elif arr[p][q] == "e":
            return 3
    elif arr[p][q] == "l":
            return 4
    elif arr[p][q] == "rl":
            return 5
    elif arr[p][q] == "cb":
            return 6
def material_check(arr, rarity):
    o_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for AB in range(len(arr)-3):
        if arr[AB+1] == 'Painted':
            


def dissect(s):
    output_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for AA in range(len(cb.series_1)):
        rarity = check_rarity(cb.series_1, AA, 1) # Tested, this works as intended!
        print(rarity)


