import matlist as ml
import cubelist as cb

# OA: (0)Dye, Circuits, Plastic, Hamburger, (4)Filament, 
# Patch, Dumbbells, Charcoal, Feather, (9)Resin, Shard, 
# Tough Stuff, Iron Filament, Polish, (14)Ectoplasm, Pebble, Perfection,
# Poison, Ash, (19)New Tag, Vibrations, Water, Goo, Rubber, (24)Dust, 
# Ice, Crystalline Shard, Strange Capacitor, Glint, (29)Cellulose, 
# Magma Ball, Ghastly Eye, Jotunn Shard

rarity = ""
def check_rarity(arr, p, q): # check rarity and return number
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
        else:
                print("+-------FATAL ERROR HAS OCCURRED-------+")
                raise ValueError("Improper rarity at cube: " + str(arr[p][0])) # Fucked up!!

def return_mps(arr, rarity, legbool): # return mat chance from array input
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

def material_check(cubearr, rarity): # check materials of cubes from array
        output_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for AB in range(len(cubearr)):
                for AE in range(0, 26, 1):
                        output_arr[AE] = return_mps(cubearr, rarity, 0) * cubearr.count(ml.mat_called_name[AE])
                for AF in range(26, 33, 1):
                        output_arr[AF] = return_mps(cubearr, rarity, 1) * cubearr.count(ml.mat_called_name[AF])
        return output_arr # This is the output for the cube itself.

def dissect(s): # dissect a series from input
        output_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for AA in range(len(s)):
                rarity = check_rarity(s, AA, 1) # Tested, this works as intended!
                mps_output = (material_check(s[AA], rarity))
                for AC in range(len(output_arr)):
                        if mps_output[AC] > output_arr[AC]:
                                output_arr[AC] = round(mps_output[AC],4)
        return output_arr

def mats_on_afk(minutes, series, tallym, hsbool): # check mats on afk
        moa_output = dissect(series)
        totalspins = (minutes*6) * (1+tallym)
        if hsbool == True:
                totalspins *= 2
        for AD in range(len(moa_output)):
                moa_output[AD] *= totalspins
                moa_output[AD] = round(moa_output[AD])
        return moa_output

def boxprint(txt): # prints something in a neat box
        print("+----------------+")
        print(txt)
        print("+----------------+")

def beautify_mlist(arr, min, tmod, hsb): # essentially the end print result
        print("+----------------+")
        print("AFK Time: " + str(min) + " minutes...")
        if tmod != 0:
                print("Tally Mods: +" + str(tmod) + " per spin...")
        if hsb == 1:
                print("Halfspinning: Enabled...")
        boxprint("Regular Materials")
        notrolled = []
        for AG in range(26):
                if arr[AG] > 0:
                        print(ml.mat_display_name[AG] + ": " + str(arr[AG]))
                else:
                        notrolled.append(ml.mat_display_name[AG])
        boxprint("Legendary Materials")
        for AH in range(26, 32, 1):
                if arr[AH] > 0:
                        print(ml.mat_display_name[AH] + ": " + str(arr[AH]))
                else:
                        notrolled.append(ml.mat_display_name[AH])
        boxprint("Unrolled Materials")
        print(notrolled)
        print("+----------------+")

def series_check(u): # big series check function (sadly, can't just prepend "cb." to it and return variable. unless im stupid. im probably stupid.)
        if u == 'series_1':
                return cb.series_1
        elif u == 'series_2':
                return cb.series_2
        elif u == 'series_3':
                return cb.series_3
        elif u == 'emote':
                return cb.emote
        elif u == 'ccc2':
                return cb.ccc2
        elif u == 'hazardous':
                return cb.hazardous
        elif u == 'entropy':
                return cb.entropy
        
