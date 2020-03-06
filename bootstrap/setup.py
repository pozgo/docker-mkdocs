from setuptools import setup

setup(
    name='bootstrap',
    version='0.0.1',
    py_modules=['bootstrap'],
    include_package_data=True,
    install_requires=[
        'click', 'termcolor',
    ],
    entry_points='''
        [console_scripts]
        bootstrap=app.cli:cli
    ''',
)
