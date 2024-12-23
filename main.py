import dissect_series as ds
import matlist as ml

tmod = ""
hsbool = ""
spin_series = ""
minutes = ""
tminp = ""

def afk_materials():
    ds.boxprint("Available Series: ")
    spin_series = ds.series_check(input("Input the series you are spinning: "))
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
    ds.beautify_mlist(ds.mats_on_afk(minutes, spin_series, tmod, hsbool), minutes, tmod, hsbool)

def optimize_materials():
    ds.boxprint("Available Materials: ")
    print(ml.mat_display_name)
    print("+----------------+")
    mchoice = ""
    while mchoice not in ml.mat_display_name:
        mchoice = input("Material to Optimize: ")
    ds.material_optimize(mchoice)
    ds.boxprint("Rankings: ")


# The actual code that runs.
uimp = int(input("1 (afk functionality) or 2 (material optimization): "))
if uimp == 1:
    afk_materials()
elif uimp == 2:
    optimize_materials()

