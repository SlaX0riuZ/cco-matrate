import cubelist as cb

# OA: (1)Dye, Circuits, Plastic, Hamburger, (5)Filament, 
# Patch, Dumbbells, Charcoal, Feather, (10)Resin, Shard, 
# Tough Stuff, Iron Filament, Polish, (15)Ectoplasm, Pebble, Perfection,
# Poison, Ash, (20)New Tag, Vibrations, Water, Goo, Rubber, (25)Dust, 
# Ice, Crystalline Shard, Strange Capacitor, Glint, (30)Cellulose, 
# Magma Ball, Ghastly Eye, Jotunn Shard

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

def return_reg_mps(arr, pos): # Returns regular mats/spin (Non-Legendary Mats)
        if rarity == 0:
                return[(arr[2]/100) * 0.26, pos] # Mats per Spin | Output Array Push
        elif rarity == 1:
                return[(arr[2]/100) * 0.613, pos]
        elif rarity == 2:
                return[(arr[2]/100) * 1.1964, pos]
        elif rarity == 3:
                return[(arr[2]/100) * 2.0678, pos]
        elif rarity == 4:
                return[(arr[2]/100) * 3.04, pos]
        elif rarity == 5:
                return[(arr[2]/100) * 3.5392, pos]
        elif rarity == 6:
                return[(arr[2]/100) * 6, pos]

def material_check(cubearr, rarity):
        output_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for AB in range(len(cubearr)):
                output_arr[0] = cubearr.count("Painted")
        return output_arr

def dissect(s):
        output_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for AA in range(len(s)):
                rarity = check_rarity(s, AA, 1) # Tested, this works as intended!
                print(rarity)
                print(material_check(s[AA], rarity))



