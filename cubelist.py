# Array: ['cubename', 'rarity', 'drop%', 'mat1', 'mat2'...]

# Discounting Gold+ since chance is too small to matter.

# TO-DO LIST
'''
Series 6 - 11
Misfit Series
Cool Cube Series
Super Cube Series + Duper Cube Series
Mundane Series
Trash Series
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
    ["baked_potato", "l", 1.10, "organic", "edible"],
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

series_4 = [
    ["checkered", "c", 8.82, "glass", "painted"],
    ["red", "c", 8.82, "plastic", "bouncy", "light"],
    ["black", "c", 8.82, "shiny", "light", "pure"],
    ["white", "c", 8.82, "shiny", "light", "pure"],
    ["pink_goo", "u", 10.29, "slimy", "magnetic"],
    ["blue_goo", "u", 10.29, "slimy", "poisonous"],
    ["green_goo", "u", 10.29, "slimy", "poisonous"],
    ["pink_crystal", "r", 4.41, "stony", "hard"],
    ["blue_crystal", "r", 4.41, "stony", "magnetic", "hard"],
    ["green_crystal", "r", 4.41, "stony", "shiny", "hard"],
    ["glasscube", "r", 4.41, "glass", "pure"],
    ["scorpio", "e", 2.94, "glass"],
    ["sagittarius", "e", 2.94, "glass"],
    ["pisces", "e", 2.94, "glass"],
    ["obsidian", "l", 1.10, "hot", "glass", "hard", "pure"],
    ["sapphire", "l", 1.10, "shiny"],
    ["rusted", "l", 1.10, "wet", "magnetic", "dull"],
    ["mossy_metal", "l", 1.10, "organic", "magnetic", "dull"],
    ["distorted", "rl", 0.44, "plastic", "heavy"],
    ["gilded", "rl", 0.44, "stony", "shiny"],
    ["hay", "rl", 0.44, "organic", "light"],
    ["ultra_hd", "rl", 0.44, "plastic", "shiny"],
    ["meaty", "rl", 0.44, "organic", "edible", "fresh"],
    ["green_button", "rl", 0.44, "makesnoise", "magnetic", "electronic", "plastic"],
    ["durasteel", "cb", 0.12, "magnetic", "shiny", "dull"],
    ["delusional", "cb", 0.12, "haunted", "organic", "madewithfabric"],
    ["adamantium", "cb", 0.12, "shiny", "magnetic"]
]

series_5 = [
    ["purple", "c", 11.76, "plastic", "light"],
    ["green", "c", 11.76, "plastic", "shiny", "light", "pure"],
    ["blue", "c", 11.76, "plastic", "light"],
    ["pink_mushroom", "u", 10.29, "poisonous", "organic"],
    ["pink_eye", "u", 10.29, "glass", "painted"],
    ["red_goo", "u", 10.29, "slimy", "hot"],
    ["aquarium", "r", 4.41, "wet", "organic", "glass"],
    ["ghostly", "r", 4.41, "haunted", "plastic"],
    ["rocky", "r", 4.41, "stony", "hard"],
    ["red_crystal", "r", 4.41, "stony", "hot", "hard"],
    ["virgo", "e", 4.41, "pure"],
    ["taurus", "e", 4.41, "pure"],
    ["valentines", "l", 1.10, "haunted", "makesnoise"],
    ["olive", "l", 1.10, "slimy", "edible"],
    ["corny", "l", 1.10, "organic", "haunted"],
    ["arcade", "l", 1.10, "electronic", "magnetic"],
    ["overpriced", "rl", 0.44, "madewithfabric", "shiny"],
    ["melting", "rl", 0.44, "haunted", "organic", "makesnoise"],
    ["tabby", "rl", 0.44, "organic", "makesnoise"],
    ["upsidedown", "rl", 0.44, "plastic", "shiny"],
    ["edgeless", "rl", 0.44, "plastic", "shiny"],
    ["foursided", "rl", 0.44, "plastic", "shiny"],
    ["cowardly", "cb", 0.07, "haunted", "ancient", "stony"],
    ["terrarium", "cb", 0.07, "glass", "wet", "organic"],
    ["deathly", "cb", 0.07, "haunted", "pure"],
    ["color_wheel", "cb", 0.07, "emitslight", "painted"],
    ["neonoir", "cb", 0.07, "magnetic", "emitslight", "heavy"]
]

series_6 = [
    ["green_striped", "c", 11.76, "plastic", "painted"],
    ["blue_striped", "c", 11.76, "plastic", "painted"],
    ["saltine", "c", 11.76, "edible", "dull"],
    ["red_wireframe", "u", 10.29, "plastic", "hot"],
    ["green_wireframe", "u", 10.29, "plastic", "shiny"],
    ["purple_mushroom", "u", 10.29, "organic", "edible"],
    ["really_big", "r", 4.41, "heavy", "dull"],
    ["red_block", "r", 4.41, "plastic", "heavy"],
    ["blue_block", "r", 4.41, "plastic", "heavy"],
    ["pink_block", "r", 4.41, "plastic", "heavy"],
    ["brick", "e", 2.94, "stony", "dull"],
    ["alien_grass", "e", 2.94, "organic", "painted"],
    ["demonsteel", "e", 2.94, "heavy", "hard"],
    ["watching", "l", 1.10, "glass", "emitslight"],
    ["forwardfacing", "l", 1.10, "plastic", "shiny"],
    ["battery", "l", 1.10, "magnetic", "electronic"],
    ["dragonglass", "l", 1.10, "shiny", "hot"],
    ["chromatic_2", "rl", 0.44, "shiny", "stony"],
    ["chromatic_1", "rl", 0.44, "shiny", "stony"],
    ["staring", "rl", 0.44, "haunted", "heavy"],
    ["popcorn", "rl", 0.44, "edible", "fresh"],
    ["ls_cube", "rl", 0.44, "haunted", "makesnoise"],
    ["missing", "rl", 0.44, "heavy", "hard"],
    ["synthesizing", "cb", 0.12, "makesnoise", "heavy", "magnetic"],
    ["anodized", "cb", 0.12, "magnetic", "shiny"],
    ["cardboard_box", "cb", 0.12, "glass", "shiny", "heavy"]
]

series_7 = [
    ["purple_striped", "c", 11.76, "plastic", "painted"],
    ["pink_striped", "c", 11.76, "plastic", "painted"],
    ["orange_wireframe", "u", 10.29, "plastic", "shiny", "light"],
    ["purple_wireframe", "u", 10.29, "plastic", "light"],
    ["pink_wireframe", "u", 10.29, "plastic", "madewithfabric", "light"],
    ["green_fabric", "r", 4.41, "madewithfabric", "dull"],
    ["blue_fabric", "r", 4.41, "madewithfabric", "dull"],
    ["mountainous", "r", 4.41, "glass", "painted"],
    ["sunny", "r", 4.41, "glass", "painted"],
    ["pink_ice", "e", 2.94, "cold", "edible", "fresh"],
    ["ice", "e", 2.94, "cold", "edible", "pure", "fresh"],
    ["heywatson_cinderblock", "e", 2.94, "stony", "dull"],
    ["makeyourself_magnetic", "l", 1.10, "organic", "magnetic", "dull"],
    ["goopy_exploits", "l", 1.10, "organic", "slimy", "dull"],
    ["lead_paint", "l", 1.10, "poisonous", "heavy", "painted"],
    ["refracting", "l", 1.10, "emitslight", "magnetic"],
    ["pink_shoji", "rl", 0.44, "organic", "painted", "light"],
    ["red_shoji", "rl", 0.44, "organic", "painted", "light"],
    ["blue_shoji", "rl", 0.44, "organic", "painted", "light"],
    ["ocean_opal", "rl", 0.44, "shiny", "hard"],
    ["cerulean_opal", "rl", 0.44, "shiny", "hard"],
    ["polyphemus", "cb", 0.12, "wet", "ancient", "organic", "makesnoise"],
    ["working", "cb", 0.12, "organic", "wet", "dull"],
    ["shimmering", "cb", 0.12, "shiny", "bright"]
]

series_8 = [
    ["yellow_striped", "c", 11.76, "plastic", "painted"],
    ["white_goo", "c", 11.76, "slimy"],
    ["red_striped", "c", 11.76, "plastic", "painted"],
    ["blue_jumble", "u", 10.29, "plastic", "light"],
    ["child_safe", "u", 10.29, "bouncy", "plastic", "light"],
    ["blue_wireframe", "u", 10.29, "plastic", "cold", "light"],
    ["petrified_wood_1", "r", 4.41, "organic", "ancient", "dull"],
    ["petrified_wood_2", "r", 4.41, "organic", "ancient", "dull"],
    ["red_fabric", "r", 4.41, "madewithfabric", "dull"],
    ["pink_fabric", "r", 4.41, "madewithfabric", "dull"],
    ["ducky", "e", 2.94, "wet", "bouncy"],
    ["green_ice", "e", 2.94, "cold", "organic"],
    ["red_ice", "e", 2.94, "cold", "organic", "fresh"],
    ["pandoras", "l", 1.10, "heavy", "shiny", "painted"],
    ["crimson", "l", 1.10, "heavy", "painted"],
    ["velvet", "l", 1.10, "shiny", "plastic"],
    ["cubeshining", "l", 1.10, "organic", "shiny"],
    ["dog", "rl", 0.44, "organic", "makesnoise"],
    ["oldfashionedtv", "rl", 0.44, "electronic", "glass"],
    ["autumn", "rl", 0.44, "organic", "dull"],
    ["clover", "rl", 0.44, "organic", "wet", "fresh"],
    ["terminal", "rl", 0.44, "electronic", "heavy"],
    ["purple_shoji", "rl", 0.44, "organic", "light"],
    ["teensy", "cb", 0.12, "plastic", "shiny", "light"],
    ["threecubes", "cb", 0.12, "haunted", "plastic"],
    ["cautionary", "cb", 0.12, "plastic", "shiny"]
]

series_9 = [
    ["blue_pill", "c", 11.76, "plastic", "light"],
    ["red_pill", "c", 11.76, "hot", "light"],
    ["cyanide_real", "c", 11.76, "poisonous", "light"],
    ["pink_jumble", "u", 10.29, "plastic", "light"],
    ["green_jumble", "u", 10.29, "plastic", "light"],
    ["red_jumble", "u", 10.29, "plastic", "light"],
    ["green_tiles", "r", 4.41, "shiny", "glass"],
    ["blue_tiles", "r", 4.41, "shiny", "glass"],
    ["petrified_wood_3", "r", 4.41, "organic", "ancient", "dull"],
    ["petrified_wood_4", "r", 4.41, "organic", "ancient", "dull"],
    ["blue_marble", "e", 2.20, "stony", "wet", "hard"],
    ["is_this_also_cyanide", "e", 2.20, "stony", "poisonous", "hard"],
    ["red_marble", "e", 2.20, "stony", "hot", "hard"],
    ["petroleum", "e", 2.20, "plastic", "poisonous", "dull"],
    ["splatter", "l", 1.10, "wet", "painted"],
    ["horus_right", "l", 1.10, "shiny", "stony"],
    ["horus_left", "l", 1.10, "shiny", "stony"],
    ["meteorite", "l", 1.10, "stony", "magnetic", "pure"],
    ["pond", "rl", 0.44, "organic", "wet"],
    ["ballin", "rl", 0.44, "shiny", "heavy"],
    ["bear", "rl", 0.44, "organic", "makesnoise"],
    ["apple", "rl", 0.44, "organic", "edible", "fresh"],
    ["tp", "rl", 0.44, "haunted", "fresh"],
    ["dog_again", "rl", 0.44, "organic", "makesnoise"],
    ["core", "cb", 0.12, "magnetic", "electronic", "heavy"],
    ["older", "cb", 0.12, "ancient", "shiny"],
    ["banded", "cb", 0.12, "glass", "shiny"]
]

series_10 = [

]

series_11 = [

]

misfit = [

]

cool = [

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

super_series = [

]

duper_series = [

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

mundane = [
    
]

trash = [

]

nightmarish = [
    ["demon", "c", 14.28, "hot", "organic"],
    ["red_serp", "c", 14.28, "wet", "organic"],
    ["green_serp", "c", 14.28, "wet", "organic"],
    ["blue_serp", "c", 14.28, "wet", "organic"],
    ["helm_fiction", "c", 14.28, "ancient", "shiny"],
    ["helm_myth", "c", 14.28, "ancient", "shiny"],
    ["helm_legend", "c", 14.28, "ancient", "shiny"]
]

collectors = [
    ["blue_tc", "c", 4.41, "heavy", "stony"],
    ["purple_tc", "c", 4.41, "heavy", "stony"],
    ["red_tc", "c", 4.41, "heavy", "stony"],
    ["orange_tc", "c", 4.41, "heavy", "stony"],
    ["green_uhd_target", "c", 4.41, "madewithfabric", "dull"],
    ["red_uhd_target", "c", 4.41, "madewithfabric", "dull"],
    ["blue_uhd_target", "c", 4.41, "madewithfabric", "dull"],
    ["purple_uhd_target", "c", 4.41, "madewithfabric", "dull"],
    ["sed", "u", 15.43, "glass", "pure"],
    ["baked_2", "u", 15.43, "organic", "dull"],
    ["moony", "r", 8.82, "glass", "painted"],
    ["real_bee", "r", 8.82, "organic", "makesnoise"],
    ["margarine", "e", 4.41, "plastic", "pure"],
    ["melting_2", "e", 4.41, "wet", "slimy"],
    ["structurally_unsound_brick", "l", 2.20, "heavy", "hard"],
    ["amongus", "l", 2.20, "bouncy", "glass"],
    ["piano", "rl", 0.38, "heavy", "makesnoise"],
    ["rooster", "rl", 0.38, "organic", "makesnoise"],
    ["hen", "rl", 0.38, "organic", "makesnoise"],
    ["ham", "rl", 0.38, "edible", "organic"],
    ["amber", "rl", 0.38, "ancient", "shiny"],
    ["safe_red_button", "rl", 0.38, "electronic", "magnetic", "glass"],
    ["safe_green_button", "rl", 0.38, "electronic", "magnetic", "glass"],
    ["pickle_jar", "cb", 0.09, "heavy", "edible", "wet"],
    ["receipt", "cb", 0.09, "madewithfabric", "heavy"],
    ["monkey_maybe", "cb", 0.09, "organic", "wet"],
    ["rusted_adamantite", "cb", 0.09, "heavy", "wet"]
]

ccc3 = [
    ["nagiri", "c", 14.27, "edible", "wet"],
    ["traffic_cone_1", "c", 14.27, "plastic", "bouncy", "shiny"],
    ["traffic_cone_2", "c", 14.27, "plastic", "bouncy", "shiny"],
    ["bored_guy", "u", 18.73, "dull", "organic"],
    ["ballot", "u", 18.73, "heavy", "dull"],
    ["neapolitan", "e", 3.57, "edible", "cold", "ancient"],
    ["honeycomb", "e", 3.57, "edible", "shiny", "wet"],
    ["revolutionary", "e", 3.57, "haunted", "hard"],
    ["garnet", "l", 2.68, "hard", "shiny", "stony"],
    ["freon", "l", 2.68, "cold", "cold", "wet"],
    ["vine", "rl", 1.07, "wet", "organic", "painted"],
    ["industrial", "rl", 1.07, "dull", "heavy", "electronic"],
    ["draft", "rl", 1.07, "edible", "glass", "wet", "cold"],
    ["polluted", "cb", 0.14, "wet", "poisonous", "slimy"],
    ["radish", "cb", 0.14, "edible", "organic", "fresh"],
    ["ninja", "cb", 0.14, "haunted", "madewithfabric", "organic"]

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