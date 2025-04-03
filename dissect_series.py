import matlist as ml
import cubelist as cb
import math

# OA: (0)Dye, Circuits, Plastic, Hamburger, (4)Filament, 
# Patch, Dumbbells, Charcoal, Feather, (9)Resin, Shard, 
# Tough Stuff, Iron Filament, Polish, (14)Ectoplasm, Pebble, Perfection,
# Poison, Ash, (19)New Tag, Vibrations, Water, Goo, Rubber, (24)Dust, 
# Ice, Crystalline Shard, Strange Capacitor, Glint, (29)Cellulose, 
# Magma Ball, Ghastly Eye, Jotunn Shard

def boxprint(txt): # prints something in a neat box
        print("+----------------+")
        print(txt)
        print("+----------------+")

def check_rarity(arr, p, q): # check rarity and return number SINGLE CUBE ARRAY
        if arr[p][q] == "c": # common rarity
                return 0
        elif arr[p][q] == "u": # uncommon rarity
                return 1
        elif arr[p][q] == "r": # rare rarity
                return 2
        elif arr[p][q] == "e": # epic rarity
                return 3
        elif arr[p][q] == "l": # legendary rarity
                return 4
        elif arr[p][q] == "rl": # relic rarity
                return 5
        elif arr[p][q] == "cb": # cubic rarity
                return 6
        elif arr[p][q] == "sp": # special rarity
                return 10
        else:
                print("+-------FATAL ERROR HAS OCCURRED-------+")
                raise ValueError("Improper rarity at cube: " + str(arr[p][0])) # Fucked up!!

def return_mps(arr, rarity, legbool): # return mat chance from array input, SINGLE CUBE ARRAY
        if legbool == False: # Return regular materials (ie Plastics)
                if rarity == 0 or rarity == 10:
                        return(arr[2]/100) * 0.26 # Mats per Spin (common and special have exact same...)
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
                        return 0 # failsafe; special also doesnt give leg

def material_check(seriesarr, rarity): # check materials of cubes from array
        output_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for AB in range(len(seriesarr)):
                for AE in range(0, 26, 1):
                        output_arr[AE] = return_mps(seriesarr, rarity, 0) * seriesarr.count(ml.mat_called_name[AE])
                for AF in range(26, 33, 1):
                        output_arr[AF] = return_mps(seriesarr, rarity, 1) * seriesarr.count(ml.mat_called_name[AF])
        return output_arr # This is the output for the cube itself.

def error_input_check(cubearr, p):
        if cubearr[p] not in ml.mat_called_name:
                        if cubearr[p] != '':
                                print("+-------FATAL ERROR HAS OCCURRED-------+")
                                raise MemoryError("Improper material displayname at cube name: " + str(cubearr[0]))
                        
def dissect(s): # dissect a series from input
        output_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for AA in range(len(s)):
                for AJ in range(3, 12, 1):
                        try:
                                error_input_check(s[AA], AJ) # Checking if slax inputted thing wrongly >:(
                        except IndexError:
                                break # get outta the loop...
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

def beautify_mlist(arr, min, tmod, hsb): # essentially the end print result
        chance_tcheck = 1
        print("+----------------+")
        print("AFK Time: " + str(min) + " minutes...")
        if tmod != 0:
                print("Tally Mods: +" + str(tmod) + " per spin...")
                chance_tcheck = 1 + tmod
        tspins = (min*6)*(chance_tcheck)
        if hsb == 1:
                print("Halfspinning: Enabled...")
                tspins = tspins * 2
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
        boxprint("Special Chances")
        e_ch = 1-((0.99999)**tspins)
        u_ch = 1-((0.9999988345)**tspins)
        ds_ch = 1-((0.99956)**tspins)
        print("Exotic %: " + str(round(e_ch*100,3)) + "%")
        print("Unreal %: " + str(round(u_ch*100,3)) + "%")
        print("Divine/Slated %: " + str(round(ds_ch*100,3)) + "%")
        print("+----------------+")
        
def series_check(u): # big series check function (sadly, can't just prepend "cb." to it and return variable. unless im stupid. im probably stupid.)
        if u == '1':
                return cb.series_1
        elif u == '2':
                return cb.series_2
        elif u == '3':
                return cb.series_3
        elif u == '4':
                return cb.series_4
        elif u == '5':
                return cb.series_5
        if u == '6':
                return cb.series_6
        elif u == '7':
                return cb.series_7
        elif u == '8':
                return cb.series_8
        elif u == '9':
                return cb.series_9
        elif u == '10':
                return cb.series_10
        elif u == '11':
                return cb.series_11
        elif u == 'misfit':
                return cb.misfit
        elif u == 'cool':
                return cb.cool
        elif u == 'emote':
                return cb.emote
        elif u == 'ccc2':
                return cb.ccc2
        elif u == 'character':
                return cb.character
        elif u == 'super':
                return cb.super_series
        elif u == 'duper':
                return cb.duper_series
        elif u == 'haz':
                return cb.hazardous
        elif u == 'mundane':
                return cb.mundane
        elif u == 'trash':
                return cb.trash
        elif u == 'collectors':
                return cb.collectors
        elif u == 'ccc3':
                return cb.ccc3
        elif u == 'entropy':
                return cb.entropy
        elif u == 'nolife':
                return cb.nolife

def check_mat_position(m):
        for Z in range(len(ml.mat_display_name)):
                if m == ml.mat_display_name[Z]:
                        return Z

def material_optimize(m):
        mpos = check_mat_position(m)
        enarr = []
        output_arr = []
        for N in range(len(ml.series_list)):
                try:
                        used_s = series_check(ml.series_list[N]) # get the series into temp variable
                except:
                        break # get outta there
                enarr.append([ml.series_list[N], dissect(used_s)[mpos]]) # ex. ["1", 0.0378]

        while len(enarr) > 0:
                lm = enarr[0] # assume largest is first pos
                for S in range(len(enarr)):
                        if enarr[S][1] > lm[1]:
                                lm = enarr[S] # find largest number, essentially
                output_arr.append(lm)
                enarr.remove(lm)
        boxprint("Rankings: ")
        for P in range(len(output_arr)):
                print("Rank #" + str(P) + ": " + output_arr[P][0] + " (" + str(output_arr[P][1]) + ")")

def rank_successor(spincount):
        spincount = math.ceil(spincount/6)
        tempseriespush = []
        f = open('ranksuccessorpush.txt', 'a')
        for seriesname in ml.series_list:
                try:
                        tempseriespush = mats_on_afk(spincount, series_check(seriesname), 0, 0)
                except: print("not right code :(")