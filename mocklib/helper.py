from typing import List, Dict, Union
import glob, sys

def check_file_exist(file_path: str):

    file_paths = glob.glob(file_path)

    if len(file_paths) == 0:
        print(file_path + ": no search file path !!!")
        sys.exit()

def set_typing_to_row(
    row_data: Dict[str, str], infoDict: Dict[str, str]
) -> Dict[str, Union[float, str]]:

    for key, value in row_data.items():
        if infoDict[key] == "int":
            if len(value) == 0:
                row_data[key] = 0
            else:
                row_data[key] = int(value)

        elif infoDict[key] == "float":
            if len(value) == 0:
                row_data[key] = 0
            else:
                row_data[key] = float(value)

        elif infoDict[key] == "str":
            if len(value) == 0:
                row_data[key] = ""
            else:
                row_data[key] = value

        elif infoDict[key] == "date":
            if len(value) == 0:
                row_data[key] = ""
            else:
                row_data[key] = value.replace("/", "")

        else:
            print("json invalid value !!!")
            print("{ " + key + " : " + infoDict[key] + " }")
            sys.exit()

    return row_data
