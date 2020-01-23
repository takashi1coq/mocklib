import setuptools

with open('README.md', 'r') as f:
    long_discription = f.read()

setuptools.setup(
        name='mocklib',
        version='0.0.1',
        author='takashi1coq',
        author_email='osienai[at]gmail.com',
        long_discription=long_discription,
        long_discription_content_type='text/markdown',
        packages=setuptools.find_packages(),
    )
