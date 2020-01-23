from . import helper
import os, json, csv, pathlib

def create_dict_from_svfile(*, configPath, dataPath):
    '''
    configPath: json file
        {
            "ID": "str"
            "VAL": "int"
        }
        *values : ['str','int','float']
    dataPath: tsv file
        ID	VAL
        A220	3050
    '''
    helper.check_file_exist(configPath)
    helper.check_file_exist(dataPath)

    with open(configPath) as f:
        configDict = json.load(f)
    with open(dataPath) as f:
        reader = csv.DictReader(f, delimiter="\t")
        svDict = [helper.set_typing_to_row(row, configDict) for row in reader]

    return svDict

def output_json_from_dict(*, outPath, outDict):

    parentDir = pathlib.Path(outPath).parent
    if not (os.path.exists(parentDir)):
        os.makedirs(parentDir, exist_ok=True)

    with open(outPath, "w") as f:
        json.dump(
            outDict,
            f,
            ensure_ascii=False,
            indent=2,
        )
