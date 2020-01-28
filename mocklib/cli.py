import sys, os
from . import template

def _create_modules(modules):
    for moduleTitle in modules:
        dictsDir = 'modules'
        moduleDir = '/'.join([dictsDir, moduleTitle.upper()])
        initFile = '/'.join([dictsDir, '__init__.py'])
        jsonFile = '/'.join([moduleDir, moduleTitle.upper() + '.json'])
        tsvFile = '/'.join([moduleDir, moduleTitle.upper() + '.tsv'])
        pyFile = '/'.join([moduleDir, moduleTitle.upper() + '.py'])

        if not os.path.exists(dictsDir):
            os.makedirs(dictsDir, exist_ok=True)
            with open(initFile, mode='w') as f:
                f.write(template.MODULES_INIT_HEADER)
                f.write(template.MODULES_INIT_IMPORT.format(upperName=moduleTitle.upper()))
        elif not os.path.exists(moduleDir):
            with open(initFile, mode='a') as f:
                f.write(template.MODULES_INIT_IMPORT.format(upperName=moduleTitle.upper()))

        os.makedirs(moduleDir, exist_ok=True)
        with open(jsonFile, mode='w') as f:
            f.write('')
        with open(tsvFile, mode='w') as f:
            f.write('')
        with open(pyFile, mode='w') as f:
            f.write(template.MODULES_MAIN.format(upperName=moduleTitle.upper()))

    print('1. modified EQUAL_KEY : modules/__init__.py')
    print('2. modified MODULE_KEYS : module/ .py file')
    print('3. add data : module/ .tsv & .json file')

def main(as_module=False):
    print('create module')
    modules = input().split()
    _create_modules(modules)
    runFile = 'run.py'
    if not os.path.exists(runFile):
        with open(runFile, mode='w') as f:
            f.write(template.RUN_PY_INITIAL_MAIN.format(upperName=modules[0].upper()))
        modules = modules[1:]
    for module in modules:
        with open(runFile) as f:
            fileLine = f.read()
        replaceLine = fileLine.replace(template.RETURN_ROW, template.REPLACE_FUNCTION.format(upperName=module.upper()) + template.RETURN_ROW)
        with open(runFile, mode='w') as f:
            f.write(replaceLine)

if __name__ == '__main__':
    main(as_module=True)
