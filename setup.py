from setuptools import setup, find_packages

setup(
    name = 'Flask-Edits',
    version = '0.8',
    packages = find_packages(),
    install_requires = ['Flask>=0.7',],
    license = 'BSD',
    url = 'http://github.com/nathancahill/flask-edits',
    author = 'Nathan Cahill',
    author_email = 'nathan@nathancahill.com',
    description = 'Editable Content in Flask',
    long_description = open('README').read(),
    include_package_data=True,
)
