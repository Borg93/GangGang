DATADIR = "TRAINING/"
MODELDIR = "MODELS/"


def _load_and_process_gh_json(filename, index):
    import json
    import os

    filebase = os.path.splitext(os.path.basename(filename))[0]

    with open(filename) as fp:
        data = json.load(fp)

        for d in data:
            d.update({'geometry':filebase})
    
        return data

