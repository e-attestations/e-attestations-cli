from setuptools import setup

setup(
    name='address',
    version='1.0',
    py_module=['address'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        address=address:search
    '''
)