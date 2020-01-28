MODULES_INIT_HEADER = '''
EQUAL_KEY = ['']

'''
MODULES_INIT_IMPORT = '''
from .{upperName}.{upperName} import *
'''

MODULES_MAIN = '''
import mocklib
import modules

{upperName}_DICT = mocklib.create_dict_from_svfile(
            configPath='modules/{upperName}/{upperName}.json',
            dataPath='modules/{upperName}/{upperName}.tsv',
        )
{upperName}_KEYS = [
            '',
        ]

def {upperName}_ADD_ROW(row):
    for key in {upperName}_KEYS:
        row[key] = mocklib.get_dict_in_list_value(
                    targetDictList={upperName}_DICT,
                    rowDict=row,
                    key=key,
                    equalKey=modules.EQUAL_KEY,
                    errorDisp=True,
                )
    return row
'''
RUN_PY_INITIAL_MAIN = '''
import mocklib
import modules

def _addRow(row):
    return row

output = [_addRow(row) for row in modules.{upperName}_DICT]

mocklib.output_json_from_dict(
            outPath='OUTPUT.json',
            outDict=dict(output=output)
        )
'''
RETURN_ROW = '''    return row'''
REPLACE_FUNCTION = '''    row = modules.{upperName}_ADD_ROW(row)
'''
