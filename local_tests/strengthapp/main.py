from config import *
import itertools
import pandas as pd

individual_primary_muscles = list(itertools.chain(*[i["primary"] for i in muscles_worked.values()]))
individual_secondary_muscles = list(itertools.chain(*[i["secondary"] for i in muscles_worked.values()]))

individual_muscles = set(individual_primary_muscles + individual_secondary_muscles)

sample_full_body_workout = pd.DataFrame(muscles_worked).T


def sample_exercises(body_focus="full", level='beginner', required_equipment="any", muscle=None):
    if body_focus == "full": 
        muscles_worked = muscle_groupings["upper"] + muscle_groupings["lower"] + muscle_groupings["core"]
    else:
        muscles_worked = list(itertools.chain(*[muscle_groupings[i] for i in body_focus]))
    mask = sample_full_body_workout.primary.apply(lambda x: any(i for i in muscles_worked if i in x)) & sample_full_body_workout.level.apply(lambda x: x == level)
    if required_equipment != 'any':
        mask = mask & sample_full_body_workout['required equipment'].apply(lambda x: any(i for i in required_equipment if x in i))
    if muscle is not None:
        mask = mask & sample_full_body_workout['primary'].apply(lambda x: any(i for i in muscle if i in x))
    return sample_full_body_workout[mask]

test = sample_exercises(body_focus=["upper", "lower"], level = "beginner", required_equipment = ["free weights", "no equipment"], muscle=["front deltoids"])

print(test)