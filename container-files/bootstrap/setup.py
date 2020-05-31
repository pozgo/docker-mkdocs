from setuptools import setup

setup(
    name='bootstrap',
    version='1.0.0',
    py_modules=['bootstrap'],
    include_package_data=True,
    install_requires=[
        'click', 'termcolor', 'GitPython', 'python-crontab'
    ],
    entry_points='''
        [console_scripts]
        bootstrap=app.cli:cli
    ''',
)
