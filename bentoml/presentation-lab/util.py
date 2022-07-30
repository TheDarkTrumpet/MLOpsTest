import random as rnd
import uuid
import pandas as pd
import itertools
from multiprocessing import Pool

available_shapes_happiness = [
    # Circle-based Toys
    {"Shape": "Circle",
     "Softness": "Hard",
     "Happiness-Range": (5, 10)},
    {"Shape": "Circle",
     "Softness": "Medium",
     "Happiness-Range": (10, 15),
     {"Shape": "Circle",
      "Softness": "Soft",
      "Happiness-Range": (5, 10)},

    # Square-based Toys
    {"Shape": "Square",
     "Softness": "Hard",
     "Happiness-Range": (3, 5)},
    {"Shape": "Square",
     "Softness": "Medium",
     "Happiness-Range": (3, 5)},
    {"Shape": "Square",
     "Softness": "Soft",
     "Happiness-Range": (3, 5)},

    # Rectangle-based Toys
    {"Shape": "Rectangle",
     "Softness": "Hard",
     "Happiness-Range": (10, 15)},
    {"Shape": "Rectangle",
     "Softness": "Medium",
     "Happiness-Range": (30, 40)},
    {"Shape": "Rectangle",
     "Softness": "Soft",
     "Happiness-Range": (15, 25)},
]

def generateChunk(arg):
    """ Given a tuple for the max records to generate, and max range for upper integer, will generate fixture information
    (present in toInsert), and in the end convert to a Pandas DataFrame and return to generateRecords for combination
    with other work done. """
    maxRecords, maxInt = arg
    toInsert = {
        "KEY": [],
        "Shape": [],
        "Softness": [],
        "Happiness": []
    }

    for x in range(maxRecords):
        md = uuid.uuid4().hex

        toy_to_add = available_shapes_happiness[rnd.randint(0, len(available_shapes_happiness) - 1)]
        toy_rand_range = toy_to_add["Happiness-Range"]

        toInsert["KEY"].append(md)
        toInsert["Shape"].append(toy_to_add["Shape"])
        toInsert["Softness"].append(toy_to_add["Softness"])
        toInsert["Happiness"].append(rnd.randint(toy_rand_range[0], toy_rand_range[1]))

    pdToInsert = pd.DataFrame.from_dict(toInsert, orient='columns')
    return pdToInsert


def generateRecords(maxRecords: int):
    """ Will create a pool of 8, and will call generateChunk parallel.  Returns a Pandas dataframe of concatenated
    results. """
    num_processes = 8
    range_map = list(itertools.repeat((int(maxRecords / numProcesses), maxInt), numProcesses))

    with Pool(processes=num_processes) as pool:
        # process_pool = Pool(processes=numProcesses)
        dfs = pool.map(generateChunk, range_map)
    pdToInsert = pd.concat(dfs, ignore_index=True, axis=0)

    return pdToInsert