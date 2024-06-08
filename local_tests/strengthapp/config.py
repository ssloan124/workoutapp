at_home_friendly = ["no equipment", "free weights"]
muscle_groupings = {
    "upper": ['forearm flexors', 'lats', 'chest', 'trapezius', 'rear deltoids', 'biceps', 'front deltoids', 'rotator cuff', 'middle deltoids', 'triceps'],
    "lower": ['calves', 'glutes', 'quads', 'hamstrings'],
    "core": ['hip flexor', "abs", "obliques", "lower back", 'adductors', 'abductors']
}
muscles_worked = {
    "ball slams": {
        "primary": ["abs", "lats", "obliques"], 
        "secondary": ["front deltoids", "glutes"],
        "level": "beginner",
        "required equipment": "medicine ball"
    },
    "high to low wood chop": {
        "primary": ["obliques"],
        "secondary": ["abs"],
        "level": "beginner",
        "required equipment": "free weights or machine"
    },
    "crunch": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "dead bug": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "dragon flag": {
        "primary": ["abs"],
        "secondary": ["obliques", "lats"],
        "level": "advanced",
        "required equipment": "no equipment"
    },
    "farmer's walk": {
        "primary": ["forearm flexors", "obliques", "glutes", "trapezius"],
        "secondary": ["quads", "abs", "lower back", "calves", "middle deltoids"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "get-ups": {
        "primary": ["abs", "front deltoids", "middle deltoids", "rotator cuff", "rear deltoids", "glutes"],
        "secondary": ["quads"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "hanging knee raise": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "beginner",
        "required equipment": "pullup bar"
    },
    "hanging knee to elbows": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "intermediate",
        "required equipment": "pullup bar"
    },
    "hanging l-sit": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "intermediate",
        "required equipment": "pullup bar"
    },
    "hanging l-sit with tucked knees": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "beginner",
        "required equipment": "pullup bar"
    },
    "hanging leg raise": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "advanced",
        "required equipment": "pullup bar"
    },
    "hanging sit-up": {
        "primary": ["abs", "hip flexor"],
        "secondary": ["obliques"],
        "level": "advanced",
        "required equipment": "pullup bar"
    },
    "horizontal wood chop": {
        "primary": ["obliques"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "machine"
    },
    "jackknife sit-up": {
        "primary": ["abs"],
        "secondary": [],
        "level": "intermediate",
        "required equipment": "no equipment"
    },
    "kneeling ab wheel": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "beginner",
        "required equipment": "wheel"
    },
    "kneeling plank": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "kneeling side plank": {
        "primary": ["obliques"],
        "secondary": ["abs"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "lying leg raise": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "intermediate",
        "required equipment": "no equipment"
    },
    "lying windshield wiper": {
        "primary": ["obliques"],
        "secondary": ["abs"],
        "level": "intermediate",
        "required equipment": "no equipment"
    },
    "lying windshield wiper with bent knees": {
        "primary": ["obliques"],
        "secondary": ["abs"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "mountain climbers": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "intermediate",
        "required equipment": "no equipment"
    },
    "oblique crunch": {
        "primary": ["obliques"],
        "secondary": ["abs"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "oblique sit-up": {
        "primary": ["obliques"],
        "secondary": ["abs"],
        "level": "intermediate",
        "required equipment": "no equipment"
    },
    "forearm plank": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "forearm plank with leg raises": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "intermediate",
        "required equipment": "no equipment"
    },
    "russian twist": {
        "primary": ["abs", "obliques"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "side plank": {
        "primary": ["obliques"],
        "secondary": ["abs"],
        "level": "intermediate",
        "required equipment": "no equipment"
    },
    "sit-up": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "intermediate",
        "required equipment": "no equipment"
    },
    "standing ab wheel": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "intermediate",
        "required equipment": "wheel"
    },
    "suitcase carry": {
        "primary": ["forearm flexors", "obliques", "trapezius", "glutes", "abductors"],
        "secondary": ["calves", "middle deltoids", "abs", "lower back", "quads"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "toes to bar": {
        "primary": ["abs"],
        "secondary": ["obliques"],
        "level": "advanced",
        "required equipment": "pullup bar"
    },
    "turkish get-up": {
        "primary": ["front deltoids", "rear deltoids", "middle deltoids", "abs", "obliques", "glutes"],
        "secondary": ["lats", "trapezius", "hamstrings", "quads"],
        "level": "advanced",
        "required equipment": "free weights"
    },
    "assisted chin-up": {
        "primary": ["lats"],
        "secondary": ["rear deltoids", "biceps", "forearm flexors"],
        "level": "beginner",
        "required equipment": "pullup bar"
    },
    "assisted pull-up": {
        "primary": ["lats"],
        "secondary": ["biceps", "rear deltoids", "forearm flexors"],
        "level": "beginner",
        "required equipment": "pullup bar"
    },
    "back extension": {
        "primary": ["glutes", "lower back"],
        "secondary": ["hamstrings"],
        "level": "intermediate",
        "required equipment": "no equipment"
    },
    "wide grip row": {
        "primary": ["rear deltoids", "trapezius"],
        "secondary": ["forearm flexors", "biceps", "rotator cuff", "lats", "lower back"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "neutral grip row": {
        "primary": ["lats", "trapezius", "rear deltoids"],
        "secondary": ["biceps", "lower back", "forearm flexors", "rotator cuff"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "shrug": {
        "primary": ["trapezius"],
        "secondary": ["forearm flexors"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "cable close grip seated row": {
        "primary": ["lats", "rear deltoids", "trapezius"],
        "secondary": ["biceps", "forearm flexors", "rotator cuff"],
        "level": "beginner",
        "required equipment": "machine"
    },
    "cable wide grip seated row": {
        "primary": ["lats", "rear deltoids", "trapezius"],
        "secondary": ["biceps", "forearm flexors", "rotator cuff"],
        "level": "beginner",
        "required equipment": "machine"
    },
    "chest to bar": {
        "primary": ["lats"],
        "secondary": ["rear deltoids", "biceps", "forearm flexors", "rotator cuff"],
        "level": "advanced",
        "required equipment": "pullup bar"
    },
    "chin-up": {
        "primary": ["lats"],
        "secondary": ["rear deltoids", "biceps", "forearm flexors", "rotator cuff"],
        "level": "advanced",
        "required equipment": "pullup bar"
    },
    "close-grip pulldown": {
        "primary": ["lats"],
        "secondary": ["rear deltoids", "biceps", "forearm flexors", "rotator cuff"],
        "level": "beginner",
        "required equipment": "machine"
    },
    "deadlift": {
        "primary": ["glutes", "lower back"],
        "secondary": ["adductors", "quads", "forearm flexors", "trapezius", "hamstrings"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "dumbbell squat": {
        "primary": ["quads", "glutes", "adductors", "lower back"],
        "secondary": ["calves", "forearm flexors"],
        "level": "beginner",
        "required equipment": "free weights"       
    },
    "good morning": {
        "primary": ["glutes", "lower back", "hamstrings"],
        "secondary": ["adductors"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "jefferson curl": {
        "primary": ["lower back"],
        "secondary": ["trapezius", "adductors", "hamstrings", "glutes"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "lat pulldown": {
        "primary": ["lats"],
        "secondary": ["rear deltoids", "biceps", "forearm flexors", "rotator cuff"],
        "level": "beginner",
        "required equipment": "machine"
    },
    "lat pulldown with supinated grip": {
        "primary": ["lats"],
        "secondary": ["rear deltoids", "biceps", "forearm flexors", "rotator cuff"],
        "level": "beginner",
        "required equipment": "machine"
    },
    "pull-up": {
        "primary": ["lats"],
        "secondary": ["rear deltoids", "biceps", "forearm flexors", "rotator cuff"],
        "level": "beginner",
        "required equipment": "pullup bar"
    },
    "reverse hyperextension": {
        "primary": ["glutes", "hamstrings", "lower back"],
        "secondary": [],
        "level": "intermediate",
        "required equipment": "machine"
    },
    "single leg deadlift": {
        "primary": ["glutes", "hamstrings", "lower back"],
        "secondary": ["adductors", "trapezius", "abductors", "forearm flexors"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "straight arm lat pulldown": {
        "primary": ["lats"],
        "secondary": ["rotator cuff", "rear deltoids"],
        "level": "beginner",
        "required equipment": "machine"
    },
    "sumo deadlift": {
        "primary": ["glutes", "lower back"],
        "secondary": ["quads", "hamstrings", "adductors", "trapezius", "forearm flexors"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "bicep curl": {
        "primary": ["biceps"],
        "secondary": ["forearm flexors"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "hammer curl": {
        "primary": ["biceps"],
        "secondary": ["forearm flexors"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "incline bicep curl": {
        "primary": ["biceps"],
        "secondary": ["forearm flexors"],
        "level": "intermediate",
        "required equipment": "free weights"
    },
    "reverse curl": {
        "primary": ["biceps"],
        "secondary": ["forearm flexors"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "ring or dip bar support hold": {
        "primary": ["triceps", "biceps", "front deltoids", "rear deltoids", "middle deltoids"],
        "secondary": ["lats", "trapezius", "rotator cuff", "chest"],
        "level": "intermediate",
        "required equipment": "dip bar"
    },
    "assisted dip": {
        "primary": ["chest", "front deltoids"],
        "secondary": ["triceps"],
        "level": "beginner",
        "required equipment": "dip bar"
    },
    "bench press": {
        "primary": ["chest", "front deltoids"],
        "secondary": ["triceps"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "burpee": {
        "primary": ["chest", "quads", "front deltoids", "glutes", "adductors"],
        "secondary": ["triceps", "abs", "calves"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "close-grip pushup": {
        "primary": ["triceps", "chest"],
        "secondary": ["front deltoids", "abs"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "cobra pushup": {
        "primary": ["triceps", "chest"],
        "secondary": ["front deltoids", "abs"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "chest fly": {
        "primary": ["chest"],
        "secondary": ["front deltoids"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "pullover": {
        "primary": ["chest"],
        "secondary": ["lats"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "pushup": {
        "primary": ["chest", "front deltoids"],
        "secondary": ["triceps", "abs"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "bar hang": {
        "primary": ["forearm flexors"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "pullup bar"
    },
    "wrist curl": {
        "primary": ["forearm flexors"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "wrist curl behind the back": {
        "primary": ["forearm flexors"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "wrist extension": {
        "primary": ["forearm flexors"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "plate pinch": {
        "primary": ["forearm flexors"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "scap pullups": {
        "primary": ["rotator cuff", "forearm flexors"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "pullup bar"
    },
    "banded side kick": {
        "primary": ["abductors"],
        "secondary": ["glutes"],
        "level": "beginner",
        "required equipment": "machine or band"
    },
    "lunge": {
        "primary": ["glutes", "quads", "adductors"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "walking lunges": {
        "primary": ["glutes", "quads", "adductors"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "box jump": {
        "primary": ["quads", "glutes", "adductors"],
        "secondary": ["calves"],
        "level": "beginner",
        "required equipment": "box"
    },
    "box step-up": {
        "primary": ["quads", "glutes", "adductors"],
        "secondary": ["calves"],
        "level": "beginner",
        "required equipment": "box"      
    },
    "bulgarian split squat": {
        "primary": ["quads", "glutes", "adductors"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "glute kickback": {
        "primary": ["glutes"],
        "secondary": ["adductors", "hamstrings"],
        "level": "beginner",
        "required equipment": "machine"
    },
    "clamshell": {
        "primary": ["abductors"],
        "secondary": ["glutes"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "donkey kick": {
        "primary": ["glutes"],
        "secondary": ["hamstrings", "adductors"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "frog pump": {
        "primary": ["glutes"],
        "secondary": ["adductors", "hamstrings"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "fire hydrants": {
        "primary": ["glutes"],
        "secondary": ["hamstrings", "adductors"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "side squat": {
        "primary": ["glutes", "quads"],
        "secondary": ["adductors"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "glute bridge": {
        "primary": ["glutes"],
        "secondary": ["quads"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "hip abduction": {
        "primary": ["abductors"],
        "secondary": ["glutes"],
        "level": "beginner",
        "required equipment": "machine"
    },
    "hip thrust": {
        "primary": ["glutes"],
        "secondary": ["adductors", "quads"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "jump lunge": {
        "primary": ["glutes", "quads", "adductors"],
        "secondary": [],
        "level": "intermediate",
        "required equipment": "no equipment"
    },
    "jump squat": {
        "primary": ["glutes", "quads", "adductors"],
        "secondary": ["calves"],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "one-legged glute bridge": {
        "primary": ["glutes"],
        "secondary": ["quads"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "one-legged hip thrust": {
        "primary": ["glutes"],
        "secondary": ["adductors", "quads"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "reverse lunge": {
        "primary": ["glutes", "quads", "adductors"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "thruster": {
        "primary": ["quads", "glutes", "front deltoids", "adductors"],
        "secondary": ["hamstrings", "calves", "middle deltoids", "triceps", "lower back"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "wall sit": {
        "primary": ["adductors", "glutes", "quads"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "no equipment"
    },
    "standing calf raise": {
        "primary": ["calves"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "leg curl": {
        "primary": ["hamstrings"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "machine"
    },
    "leg extension": {
        "primary": ["quads"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "machine"
    },
    "arnold press": {
        "primary": ["front deltoids"],
        "secondary": ["triceps", "middle deltoids"],
        "level": "beginner",
        "required equipment": "free weights"
    },
    "external shoulder rotation": {
        "primary": ["rotator cuff"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "machine or free weights"     
    },
    "internal shoulder rotation": {
        "primary": ["rotator cuff"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "machine or free weights"   
    },
    "front raise": {
        "primary": ["front deltoids"],
        "secondary": ["middle deltoids"],
        "level": "beginner",
        "required equipment": "free weights"    
    },
    "lateral raise": {
        "primary": ["middle deltoids"],
        "secondary": ["front deltoids"],
        "level": "beginner",
        "required equipment": "free weights"   
    },
    "shoulder press": {
        "primary": ["front deltoids"],
        "secondary": ["triceps", "middle deltoids"],
        "level": "beginner",
        "required equipment": "free weights"   
    },
    "front hold": {
        "primary": ["front deltoids"],
        "secondary": ["middle deltoids"],
        "level": "beginner",
        "required equipment": "free weights"    
    },
    "dolphin": {
        "primary": ["front deltoids"],
        "secondary": ["abs", "middle deltoids", "chest", "triceps"],
        "level": "beginner",
        "required equipment": "no equipment"   
    },
    "pike pushup": {
        "primary": ["front deltoids"],
        "secondary": ["abs", "middle deltoids", "chest", "triceps"],
        "level": "beginner",
        "required equipment": "no equipment"      
    },
    "reverse fly": {
        "primary": ["rear deltoids", "rotator cuff"],
        "secondary": ["trapezius"],
        "level": "beginner",
        "required equipment": "free weights"    
    },
    "lying triceps extension": {
        "primary": ["triceps"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"   
    },
    "standing triceps extension": {
        "primary": ["triceps"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"         
    },
    "tricep kickback": {
        "primary": ["triceps"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "free weights"   
    },
    "tricep pushdown": {
        "primary": ["triceps"],
        "secondary": [],
        "level": "beginner",
        "required equipment": "machine"   
    }
}