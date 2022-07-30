import random
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
     "Happiness-Range": (10-15),
     {"Shape": "Circle",
      "Softness": "Soft",
      "Happiness-Range": (5, 10)},

    # Square-based Toys

    # Rectangle-based Toys
    
]

def generateChunk(arg):
    """ Given a tuple for the max records to generate, and max range for upper integer, will generate fixture information
    (present in toInsert), and in the end convert to a Pandas DataFrame and return to generateRecords for combination
    with other work done. """
    maxRecords, maxInt = arg
    toInsert = {
        "KEY": [],
        "Shape": [],
        "": []
    }

    for x in range(maxRecords):
        md = uuid.uuid4().hex
        intValue = random.randint(0, maxInt)
        if intValue in insertedValues:
           continue
        insertedValues[intValue] = None
        randString = gen.gen_sentence()

        toInsert["intColumn"].append(intValue)
        toInsert["md5"].append(md)
        toInsert["string"].append(randString)

    pdToInsert = pd.DataFrame.from_dict(toInsert, orient='columns')
    return pdToInsert


def generateRecords(maxRecords: int):
    """ Will create a pool of 8, and will call generateChunk parallel.  Returns a Pandas dataframe of concatenated
    results. """
    numProcesses = 8
    maxInt = maxRecords * 200

    rangeMap = list(itertools.repeat((int(maxRecords / numProcesses), maxInt), numProcesses))
    with Pool(processes=numProcesses) as pool:
        # process_pool = Pool(processes=numProcesses)
        dfs = pool.map(generateChunk, rangeMap)
    pdToInsert = pd.concat(dfs, ignore_index=True, axis=0)

    return pdToInsert