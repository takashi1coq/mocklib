import sys, os
from . import template

def _create_dicts(modules):
    for moduleTitle in modules:
        dictsDir = 'dicts'
        moduleDir = '/'.join([dictsDir, moduleTitle.upper()])
        initFile = '/'.join([dictsDir, '__init__.py'])
        jsonFile = '/'.join([moduleDir, moduleTitle.upper() + '.json'])
        tsvFile = '/'.join([moduleDir, moduleTitle.upper() + '.tsv'])

        if not os.path.exists(dictsDir):
            os.makedirs(dictsDir, exist_ok=True)
            with open(initFile, mode='w') as f:
                f.write(template.tmp_import_mocklib + template.tmp_create_dict.format(upperName=moduleTitle.upper()))
        elif not os.path.exists(moduleDir):
            with open(initFile, mode='a') as f:
                f.write(template.tmp_create_dict.format(upperName=moduleTitle.upper()))

        os.makedirs(moduleDir, exist_ok=True)
        with open(jsonFile, mode='w') as f:
            f.write('')
        with open(tsvFile, mode='w') as f:
            f.write('')

def main(as_module=False):
    print('create module')
    modules = input().split()
    _create_dicts(modules)
    runFile = 'run.py'
    addrowFile = 'addrow.py'
    if not os.path.exists(runFile):
        with open(runFile, mode='w') as f:
            f.write(template.tmp_run_py.format(upperName=modules[0].upper()))
        with open(addrowFile, mode='w') as f:
            f.write(template.tmp_addrow_header)
            for module in modules[1:]:
                f.write(template.tmp_get_value.format(upperName=module.upper()))

            f.write(template.tmp_return_row)
    else:
        for module in modules:
            with open(addrowFile) as f:
                addrowFileLine = f.read()
            replaceLine = addrowFileLine.replace(template.tmp_return_row, template.tmp_get_value.format(upperName=module.upper()))
            with open(addrowFile, mode='w') as f:
                f.write(replaceLine)
                f.write(template.tmp_return_row)

if __name__ == '__main__':
    main(as_module=True)
