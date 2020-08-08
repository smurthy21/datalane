from setuptools import setup, find_packages

name = 'datalane'
setup(
    author = 'Sri Murthy',
    author_email = 'srimurthy21@gmail.com',
    name = name,
    package_data = {name: ['_/*/*']},
    packages = find_packages(),
    version =  1.0,
    zip_safe = True,
    entry_points = {
        'console_scripts': [
            'datalane = datalane.run:chug',
        ]
    }
)