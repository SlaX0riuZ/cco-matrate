# Array: ['cubename', 'rarity', 'drop%', 'mat1', 'mat2'...]

# Discounting Gold+ since chance is too small to matter.

# TO-DO LIST
'''
Series 3 - 11
Misfit Series
Cool Cube Series
Super Cube Series + Duper Cube Series
Mundane Series
Trash Series
Nightmarish
Collector's Collection
CCC3
'''

series_1 = [
    ["blue_camo", "c", 11.76, "plastic", "painted"],
    ["red_camo", "c", 11.76, "plastic", "painted"],
    ["pink_camo", "c", 11.76, "plastic", "painted"],
    ["blue_mushroom", "u", 10.29, "edible", "organic"],
    ["red_mushroom", "u", 10.29, "edible"],
    ["yellow_mushroom", "u", 10.29, "edible", "organic"],
    ["autumn_leaves", "r", 3.53, "organic"],
    ["pink_target", "r", 3.53, "madewithfabric"],
    ["iron", "r", 3.53, "heavy", "magnetic", "hard"],
    ["hologram", "r", 3.53, "magnetic", "emitslight", "light"],
    ["green_grass", "r", 3.53, "organic", "dull"],
    ["holey", "e", 2.94, "edible", "organic"],
    ["boom", "e", 2.94, "electronic", "plastic"],
    ["mosaica", "e", 2.94, "glass", "painted"],
    ["invisible", "l", 1.10, "glass", "light"],
    ["gold", "l", 1.10, "shiny", "heavy", "hard"],
    ["emerald", "l", 1.10, "shiny", "pure"],
    ["copper", "l", 1.10, "heavy", "magnetic", "hard"],
    ["sushi", "rl", 0.44, "edible", "fresh"],
    ["chicken", "rl", 0.44, "organic"],
    ["dice", "rl", 0.44, "shiny"],
    ["tv", "rl", 0.44, "electronic", "magnetic"],
    ["neon", "rl", 0.44, "emitslight", "glass", "light"],
    ["relic", "rl", 0.44, "magnetic", "shiny", "dull"],
    ["crust", "cb", 0.12, "hot", "hard"],
    ["aspects", "cb", 0.12, "heavy", "cold", "magnetic"],
    ["kyanite", "cb", 0.12, "emitslight", "shiny", "hard", "pure"]
]

series_2 = [
    ["red_building", "c", 11.76, "organic", "painted", "light"],
    ["blue_building", "c", 11.76, "organic", "painted", "light"],
    ["green_camo", "c", 11.76, "plastic", "painted"],
    ["green_target", "u", 10.29, "madewithfabric", "electronic"],
    ["green_mushroom", "u", 10.29, "edible", "organic"],
    ["blue_target", "u", 10.29, "madewithfabric", "painted"],
    ["burrito", "r", 4.41, "edible", "organic"],
    ["yellow_eye", "r", 4.41, "glass", "painted"],
    ["red_target", "r", 4.41, "madewithfabric", "painted"],
    ["purple_target", "r", 4.41, "madewithfabric", "electronic"],
    ["aries", "e", 2.20, "glass"],
    ["aquarius", "e", 2.20, "wet"],
    ["red_eye", "e", 2.20, "glass", "painted"],
    ["pillar", "e", 2.20, "stony", "makesnoise", "hard"],
    ["red_galaxy", "l", 1.10, "glass", "hot", "pure"],
    ["pink_galaxy", "l", 1.10, "glass", "pure"],
    ["purple_galaxy", "l", 1.10, "glass", "pure"],
    ["minty", "l", 1.10, "edible", "fresh"],
    ["gluttony", "rl", 0.44, "organic", "makesnoise", "haunted"],
    ["blue_nebula", "rl", 0.44, "glass", "shiny", "pure"],
    ["red_nebula", "rl", 0.44, "glass", "shiny", "pure"],
    ["purple_nebula", "rl", 0.44, "glass", "shiny", "pure"],
    ["earth", "rl", 0.44, "wet", "magnetic", "heavy"],
    ["planar_silk", "rl", 0.44, "madewithfabric"],
    ["plastique", "cb", 0.12, "plastic", "electronic", "light"],
    ["mutes", "cb", 0.12, "glass", "electronic", "hard"],
    ["binary", "cb", 0.12, "emitslight"]
]

series_3 = [
    ["yellow", "c", 11.76, "plastic", "shiny", "light"],
    ["pink_building", "c", 11.76, "organic", "painted", "light"],
    ["green_building", "c", 11.76, "organic", "painted", "light"],
    ["bean", "u", 10.29, "organic", "edible", "light"],
    ["red_grass", "u", 10.29, "organic", "stony", "painted"],
    ["pink_checkered", "u", 10.29, "glass", "painted"],
    ["maze", "r", 4.41, "cold", "dull", "pure"],
    ["barrel", "r", 4.41, "organic"],
    ["pancake", "r", 4.41, "edible", "light"],
    ["steel", "r", 4.41, "magnetic", "heavy"],
    ["gemini", "e", 2.20, "glass"],
    ["capricorn", "e", 2.20, "glass"],
    ["cancer", "e", 2.20, "glass"],
    ["aries", "e", 2.20, "glass"],
    ["blue_galaxy", "l", 1.10, "glass", "cold", "pure"],
    ["flamesteel", "l", 1.10, "hot", "magnetic"],
    ["yellow_galaxy", "l", 1.10, "glass", "pure"],
    ["baked_potato", "l", 1.10, "organic", "edible"]
    ["red_button", "rl", 0.44, "hot", "magnetic", "electronic", "plastic"],
    ["blue_button", "rl", 0.44, "makesnoise", "magnetic", "electronic", "plastic"],
    ["configurum", "rl", 0.44, "heavy", "cold"],
    ["blooming", "rl", 0.44, "organic", "poisonous"],
    ["cat", "rl", 0.44, "organic", "makesnoise"],
    ["orichalcum", "rl", 0.44, "shiny", "wet"],
    ["cake", "cb", 0.12, "haunted", "edible"],
    ["cubeonastick", "cb", 0.12, "edible", "plastic", "fresh"],
    ["buddy", "cb", 0.12, "haunted", "madewithfabric"]
]

emote = [
    ["ayaya", "c", 17.64, "shiny", "plastic"],
    ["kekw", "c", 17.64, "dull", "painted"],
    ["pog", "u", 15.43, "makesnoise", "wet"],
    ["5head", "u", 15.43, "painted", "dull"],
    ["yep", "r", 8.82, "electronic", "haunted"],
    ["monkaw", "r", 8.82, "electronic", "haunted"],
    ["pepel", "e", 4.41, "organic", "electronic"],
    ["pepehmm", "e", 4.41, "organic", "electronic"],
    ["wicked", "l", 2.20, "organic", "fresh"],
    ["popcat", "l", 2.20, "organic", "makesnoise", "fresh"],
    ["sadge", "rl", 1.32, "fresh", "haunted"],
    ["pepega", "rl", 1.32, "dull", "haunted"],
    ["ez", "cb", 0.18, "organic", "madewithfabric"],
    ["pepelaugh", "cb", 0.18, "organic", "dull"]
]

ccc2 = [
    ["abstract_1", "c", 11.76, "plastic", "dull"],
    ["abstract_2", "c", 11.76, "plastic", "dull"],
    ["abstract_3", "c", 11.76, "plastic", "dull"],
    ["xiii_remix", "u", 30.86, "plastic", "haunted"],
    ["peeka", "r", 8.82, "plastic", "painted"],
    ["twirling", "r", 8.82, "plastic", "electronic"],
    ["celebratory", "e", 4.41, "hot", "painted"],
    ["mouth", "e", 4.41, "organic", "slimy"],
    ["lunar_flare", "l", 2.20, "emitslight", "magnetic"],
    ["weird_box", "l", 2.20, "heavy", "haunted", "organic"],
    ["pulsar_cube", "rl", 1.32, "emitslight", "heavy"],
    ["laser_tag", "rl", 1.32, "emitslight", "electronic", "magnetic"],
    ["rotting_log", "cb", 0.12, "organic", "wet"],
    ["racc_2", "cb", 0.12, "organic", "wet"],
    ["cotw", "cb", 0.12, "haunted", "hard"]
]
hazardous = [
    ["yellow_haz", "c", 11.76, "plastic", "glass"],
    ["red_haz", "c", 11.76, "plastic", "glass"],
    ["green_haz", "c", 11.76, "plastic", "glass"],
    ["uranium_core", "u", 15.43, "poisonous", "electronic", "heavy"],
    ["thorium_core", "u", 15.43, "poisonous", "electronic", "stony"],
    ["irradiated", "r", 8.82, "heavy", "hot"],
    ["ionizing_rad", "r", 8.82, "heavy", "hot"],
    ["radon_ore", "e", 2.94, "stony", "heavy"],
    ["iridium_ore", "e", 2.94, "stony", "heavy"],
    ["kunzite_ore", "e", 2.94, "stony", "heavy"],
    ["quantum", "l", 2.20, "plastic", "poisonous", "light"],
    ["dark_matter", "l", 2.20, "heavy", "glass"],
    ["unstable_neutron", "rl", 1.32, "hot", "hard"],
    ["pulsing_alien", "rl", 1.32, "organic", "haunted"],
    ["hazardous_barrel", "cb", 0.18, "heavy", "poisonous", "poisonous"],
    ["radium", "cb", 0.18, "heavy", "heavy", "poisonous"]
]

entropy = [
    ["barcode", "c", 17.64, "painted", "light"],
    ["jailed", "c", 17.64, "madewithfabric"],
    ["splatter_2", "u", 15.43, "painted", "heavy"],
    ["houndstooth", "u", 15.43, "painted"],
    ["topographical", "r", 8.82, "haunted", "glass", "organic"],
    ["infested", "r", 8.82, "haunted", "glass", "organic"],
    ["vascular", "e", 4.41, "electronic", "emitslight", "makesnoise"],
    ["polka_dotted", "e", 4.41, "plastic", "magnetic", "heavy"],
    ["chalkboard", "l", 2.20, "makesnoise", "heavy", "painted"],
    ["elixir", "l", 2.20, "glass", "poisonous", "wet"],
    ["percieving", "rl", 1.32, "haunted", "organic", "slimy"],
    ["confetti", "rl", 1.32, "light", "plastic", "ancient"],
    ["racing", "cb", 0.12, "painted", "glass", "plastic", "hard"],
    ["eclipse", "cb", 0.12, "emitslight", "heavy", "hot"],
    ["general", "cb", 0.12, "organic", "madewithfabric", "makesnoise"]
]