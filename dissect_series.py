import cubelist as cb

# OA: (0)Dye, Circuits, Plastic, Hamburger, (4)Filament, 
# Patch, Dumbbells, Charcoal, Feather, (9)Resin, Shard, 
# Tough Stuff, Iron Filament, Polish, (14)Ectoplasm, Pebble, Perfection,
# Poison, Ash, (19)New Tag, Vibrations, Water, Goo, Rubber, (24)Dust, 
# Ice, Crystalline Shard, Strange Capacitor, Glint, (29)Cellulose, 
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

def return_mps(arr, rarity, legbool):
        if legbool == False: # Return regular materials (ie Plastics)
                if rarity == 0:
                        return(arr[2]/100) * 0.26 # Mats per Spin
                elif rarity == 1:
                        return (arr[2]/100) * 0.613
                elif rarity == 2:
                        return (arr[2]/100) * 1.1964
                elif rarity == 3:
                        return (arr[2]/100) * 2.0678
                elif rarity == 4:
                        return (arr[2]/100) * 3.04
                elif rarity == 5:
                        return (arr[2]/100) * 3.5392
                elif rarity == 6:
                        return (arr[2]/100) * 6
                else:
                        return 0 # failsafe
        elif legbool == True: # Return legendary materials (ie Strange Capacitors)
                if rarity == 4:
                        return (arr[2]/100) * 2.4312
                elif rarity == 5:
                        return (arr[2]/100) * 2.8312
                elif rarity == 6:
                        return (arr[2]/100) * 6
                else:
                        return 0 # failsafe

def material_check(cubearr, rarity):
        output_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for AB in range(len(cubearr)):
                reg_mps = return_mps(cubearr, rarity, 0)
                leg_mps = return_mps(cubearr, rarity, 1)
                output_arr[0] = reg_mps * cubearr.count("Painted") # How many times this shows up
                output_arr[1] = reg_mps * cubearr.count("Electronic")
                output_arr[2] = reg_mps * cubearr.count("Plastic")
                output_arr[3] = reg_mps * cubearr.count("Edible")
                output_arr[4] = reg_mps * cubearr.count("Emits Light")
                output_arr[5] = reg_mps * cubearr.count("Made With Fabric")
                output_arr[6] = reg_mps * cubearr.count("Heavy")
                output_arr[7] = reg_mps * cubearr.count("Dull")
                output_arr[8] = reg_mps * cubearr.count("Light")
                output_arr[9] = reg_mps * cubearr.count("Organic")
                output_arr[10] = reg_mps * cubearr.count("Glass")
                output_arr[11] = reg_mps * cubearr.count("Hard")
                output_arr[12] = reg_mps * cubearr.count("Magnetic")
                output_arr[13] = reg_mps * cubearr.count("Shiny")
                output_arr[14] = reg_mps * cubearr.count("Haunted")
                output_arr[15] = reg_mps * cubearr.count("Stony")
                output_arr[16] = reg_mps * cubearr.count("Pure")
                output_arr[17] = reg_mps * cubearr.count("Poisonous")
                output_arr[18] = reg_mps * cubearr.count("Hot")
                output_arr[19] = reg_mps * cubearr.count("Fresh")
                output_arr[20] = reg_mps * cubearr.count("Makes Noise")
                output_arr[21] = reg_mps * cubearr.count("Wet")
                output_arr[22] = reg_mps * cubearr.count("Slimy")
                output_arr[23] = reg_mps * cubearr.count("Bouncy")
                output_arr[24] = reg_mps * cubearr.count("Ancient")
                output_arr[25] = reg_mps * cubearr.count("Cold")
                # ---------------------------------------------------
                output_arr[26] = leg_mps * cubearr.count("Glass")
                output_arr[27] = leg_mps * cubearr.count("Electronic")
                output_arr[28] = leg_mps * cubearr.count("Shiny")
                output_arr[29] = leg_mps * cubearr.count("Plastic")
                output_arr[30] = leg_mps * cubearr.count("Hot")
                output_arr[31] = leg_mps * cubearr.count("Haunted")
                output_arr[32] = leg_mps * cubearr.count("Cold")
        return output_arr # This is the output for the cube itself.

def dissect(s):
        output_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for AA in range(len(s)):
                rarity = check_rarity(s, AA, 1) # Tested, this works as intended!
                mps_output = (material_check(s[AA], rarity))
                for AC in range(len(output_arr)):
                        if mps_output[AC] > output_arr[AC]:
                                output_arr[AC] = round(mps_output[AC],4)

        print(output_arr)