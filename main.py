import cubelist as cb
import dissect_series as ds

tmod = ""
hsbool = ""

print("+----------------+")
print("Available Series: 'series_1', 'series_2'")
print("+----------------+")

minutes = int(input("Planned AFK time (minutes): "))
tminp = input("Rolling with Tally Mods? (y/n): ")
if tminp == "y" or tminp == "Y":
    tmod = int(input("How many mods? Input the number. (+x --> x): "))
elif tminp == "n" or tminp == "N":
    tmod = 0

hsinp = input("Halfspinning? (y/n): ")
if hsinp == "y" or hsinp == "Y":
    hsbool = 1
elif hsinp == "n" or hsinp == "N":
    hsbool = 0

ds.beautify_mlist(ds.mats_on_afk(minutes, cb.series_1, tmod, hsbool), minutes, tmod, hsbool) # Literally everything.