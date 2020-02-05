from . import helper
import os, json, csv, pathlib, sys

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

def _condition_equal(target, row, equalKey):
    for key in equalKey:
        if len([check for check in target if key in target]) == 0:
            print('target key does not exist : ' + key)
            print(target)
            return False
        if len([check for check in row if key in target]) == 0:
            print('row key does not exist : ' + key)
            print(row)
            return False
        if target[key] != row[key]:
            return False
    return True

def get_dict_in_list_value(*, targetDictList, rowDict, key, equalKey, errorDisp):
    checked_value = [target[key] for target in targetDictList if key in target]
    if len(checked_value) == 0:
        print('key does not exist !!!!')
        print(key)
        sys.exit()
    hit_items = [target[key] for target in targetDictList if _condition_equal(target, rowDict, equalKey)]
    if len(hit_items) == 0:
        if (errorDisp):
            print('value does not exist : ' + rowDict[equalKey[0]])
        return ''
    return hit_items[0]
