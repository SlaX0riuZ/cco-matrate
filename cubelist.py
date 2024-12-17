# Array: ['cubename', 'rarity', 'drop%', 'mat1', 'mat2'...]

# Discounting Gold+ since chance is too small to matter.

# Input S1 for testing.

series_1 = [
    ["blue_camo", "c", 11.76, "Plastic", "Painted"],
    ["red_camo", "c", 11.76, "Plastic", "Painted"],
    ["pink_camo", "c", 11.76, "Plastic", "Painted"],
    ["blue_mushroom", "u", 10.29, "Edible", "Organic"],
    ["red_mushroom", "u", 10.29, "Edible"],
    ["yellow_mushroom", "u", 10.29, "Edible", "Organic"],
    ["autumn_leaves", "r", 3.53, "Organic"],
    ["pink_target", "r", 3.53, "Made with Fabric"],
    ["iron", "r", 3.53, "Heavy", "Magnetic", "Hard"],
    ["hologram", "r", 3.53, "Magnetic", "Emits Light", "Light"],
    ["green_grass", "r", 3.53, "Organic", "Dull"],
    ["holey", "e", 2.94, "Edible", "Organic"],
    ["boom", "e", 2.94, "Electronic", "Plastic"],
    ["mosaica", "e", 2.94, "Glass", "Painted"],
    ["invisible", "l", 1.10, "Glass", "Light"],
    ["gold", "l", 1.10, "Shiny", "Heavy", "Hard"],
    ["emerald", "l", 1.10, "Shiny", "Pure"],
    ["copper", "l", 1.10, "Heavy", "Magnetic", "Hard"],
    ["sushi", "rl", 0.44, "Edible", "Fresh"],
    ["chicken", "rl", 0.44, "Organic"],
    ["dice", "rl", 0.44, "Shiny"],
    ["tv", "rl", 0.44, "Electronic", "Magnetic"],
    ["neon", "rl", 0.44, "Emits Light", "Glass", "Light"],
    ["relic", "rl", 0.44, "Magnetic", "Shiny", "Dull"],
    ["crust", "cb", 0.12, "Hot", "Hard"],
    ["aspects", "cb", 0.12, "Heavy", "Cold", "Magnetic"],
    ["kyanite", "cb", 0.12, "Emits Light", "Shiny", "Hard", "Pure"]
]

series_2 = [
    ["red_building", "c", 11.76, "Organic", "Painted", "Light"],
    ["blue_building", "c", 11.76, "Organic", "Painted", "Light"],
    ["green_camo", "c", 11.76, "Plastic", "Painted"],
    ["green_target", "u", 10.29, "Made with Fabric", "Electronic"],
    ["green_mushroom", "u", 10.29, "Edible", "Organic"],
    ["blue_target", "u", 10.29, "Made with Fabric", "Painted"],
    ["burrito", "r", 4.41, "Edible", "Organic"],
    ["yellow_eye", "r", 4.41, "Glass", "Painted"],
    ["red_target", "r", 4.41, "Made with Fabric", "Painted"],
    ["purple_target", "r", 4.41, "Made with Fabric", "Electronic"],
    ["aries", "e", 2.20, "Glass"],
    ["aquarius", "e", 2.20, "Wet"],
    ["red_eye", "e", 2.20, "Glass", "Painted"],
    ["pillar", "e", 2.20, "Stony", "Makes Noise", "Hard"],
    ["red_galaxy", "l", 1.10, "Glass", "Hot", "Pure"],
    ["pink_galaxy", "l", 1.10, "Glass", "Pure"],
    ["purple_galaxy", "l", 1.10, "Glass", "Pure"],
    ["minty", "l", 1.10, "Edible", "Fresh"],
    ["gluttony", "rl", 0.44, "Organic", "Makes Noise", "Haunted"],
    ["blue_nebula", "rl", 0.44, "Glass", "Shiny", "Pure"],
    ["red_nebula", "rl", 0.44, "Glass", "Shiny", "Pure"],
    ["purple_nebula", "rl", 0.44, "Glass", "Shiny", "Pure"],
    ["earth", "rl", 0.44, "Wet", "Magnetic", "Heavy"],
    ["planar_silk", "rl", 0.44, "Made with Fabric"],
    ["plastique", "cb", 0.12, "Plastic", "Electronic", "Light"],
    ["mutes", "cb", 0.12, "Glass", "Electronic", "Hard"],
    ["binary", "cb", 0.12, "Emits Light"]
]

emote = [
    ["ayaya", "c", 17.64, "Shiny", "Plastic"],
    ["kekw", "c", 17.64, "Dull", "Painted"],
    ["pog", "u", 15.43, "Makes Noise", "Wet"],
    ["5head", "u", 15.43, "Painted", "Dull"],
    ["yep", "r", 8.82, "Electronic", "Haunted"],
    ["monkaw", "r", 8.82, "Electronic", "Haunted"],
    ["pepel", "e", 4.41, "Organic", "Electronic"],
    ["pepehmm", "e", 4.41, "Organic", "Electronic"],
    ["wicked", "l", 2.20, "Organic", "Fresh"],
    ["popcat", "l", 2.20, "Organic", "Makes Noise", "Fresh"],
    ["sadge", "rl", 1.32, "Fresh", "Haunted"],
    ["pepega", "rl", 1.32, "Dull", "Haunted"],
    ["ez", "cb", 0.18, "Organic", "Made with Fabric"],
    ["pepelaugh", "cb", 0.18, "Organic", "Dull"]
]

ccc2 = [
    ["abstract_1", "c", 11.76, "Plastic", "Dull"],
    ["abstract_2", "c", 11.76, "Plastic", "Dull"],
    ["abstract_3", "c", 11.76, "Plastic", "Dull"],
    ["xiii_remix", "u", 30.86, "Plastic", "Haunted"],
    ["peeka", "r", 8.82, "Plastic", "Painted"],
    ["twirling", "r", 8.82, "Plastic", "Electronic"],
    ["celebratory", "e", 4.41, "Hot", "Painted"],
    ["mouth", "e", 4.41, "Organic", "Slimy"],
    ["lunar_flare", "l", 2.20, "Emits Light", "Magnetic"],
    ["weird_box", "l", 2.20, "Heavy", "Haunted", "Organic"],
    ["pulsar_cube", "rl", 1.32, "Emits Light", "Heavy"],
    ["laser_tag", "rl", 1.32, "Emits Light", "Electronic", "Magnetic"],
    ["rotting_log", "cb", 0.12, "Organic", "Wet"],
    ["racc_2", "cb", 0.12, "Organic", "Wet"],
    ["cotw", "cb", 0.12, "Haunted", "Hard"]
]
hazardous = [
    ["yellow_haz", "c", 11.76, "Plastic", "Glass"],
    ["red_haz", "c", 11.76, "Plastic", "Glass"],
    ["green_haz", "c", 11.76, "Plastic", "Glass"],
    ["uranium_core", "u", 15.43, "Poisonous", "Electronic", "Heavy"],
    ["thorium_core", "u", 15.43, "Poisonous", "Electronic", "Stony"],
    ["irradiated", "r", 8.82, "Heavy", "Hot"],
    ["ionizing_rad", "r", 8.82, "Heavy", "Hot"],
    ["radon_ore", "e", 2.94, "Stony", "Heavy"],
    ["iridium_ore", "e", 2.94, "Stony", "Heavy"],
    ["kunzite_ore", "e", 2.94, "Stony", "Heavy"],
    ["quantum", "l", 2.20, "Plastic", "Poisonous", "Light"],
    ["dark_matter", "l", 2.20, "Heavy", "Glass"],
    ["unstable_neutron", "rl", 1.32, "Hot", "Hard"],
    ["pulsing_alien", "rl", 1.32, "Organic", "Haunted"],
    ["hazardous_barrel", "cb", 0.18, "Heavy", "Poisonous", "Poisonous"],
    ["radium", "cb", 0.18, "Heavy", "Heavy", "Poisonous"]
]

entropy = [
    ["barcode", "c", 17.64, "Painted", "Light"],
    ["jailed", "c", 17.64, "Made With Fabric"],
    ["splatter_2", "u", 15.43, "Painted", "Heavy"],
    ["houndstooth", "u", 15.43, "Painted"],
    ["topographical", "r", 8.82, "Haunted", "Glass", "Organic"],
    ["infested", "r", 8.82, "Haunted", "Glass", "Organic"],
    ["vascular", "e", 4.41, "Electronic", "Emits Light", "Makes Noise"],
    ["polka_dotted", "e", 4.41, "Plastic", "Magnetic", "Heavy"],
    ["chalkboard", "l", 2.20, "Makes Noise", "Heavy", "Painted"],
    ["elixir", "l", 2.20, "Glass", "Poisonous", "Wet"],
    ["percieving", "rl", 1.32, "Haunted", "Organic", "Slimy"],
    ["confetti", "rl", 1.32, "Light", "Plastic", "Ancient"],
    ["racing", "cb", 0.12, "Painted", "Glass", "Plastic", "Hard"],
    ["eclipse", "cb", 0.12, "Makes Light", "Heavy", "Hot"],
    ["general", "cb", 0.12, "Organic", "Made With Fabric", "Makes Noise"]
]