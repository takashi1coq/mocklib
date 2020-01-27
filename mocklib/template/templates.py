tmp_import_mocklib = '''
import mocklib

EQUAL_KEY = ['']
'''
tmp_create_dict = '''
{upperName} = mocklib.create_dict_from_svfile(
            configPath='dicts/{upperName}/{upperName}.json',
            dataPath='dicts/{upperName}/{upperName}.tsv',
        )
{upperName}_KEYS = [
            '',
        ]
'''
tmp_addrow_header = '''
import mocklib
import dicts

def addRow(row):
'''
tmp_get_value = '''
    for key in dicts.{upperName}_KEYS:
        # {upperName}
        row[key] = mocklib.get_dict_in_list_value(
                    targetDictList=dicts.{upperName},
                    rowDict=row,
                    key=key,
                    equalKey=dicts.EQUAL_KEY,
                    errorDisp=True,
                )
'''
tmp_return_row = '''    return row'''

tmp_run_py = '''
import mocklib
import dicts
import addrow

ShopData = [addrow.addRow(row) for row in dicts.{upperName}]

mocklib.output_json_from_dict(
            outPath='OUTPUT.json',
            outDict=dict(test=ShopData)
        )
'''

