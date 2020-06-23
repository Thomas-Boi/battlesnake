from setuptools import setup

setup(
    name='battlesnake',
    version='0.1',
    author='Thomas-Boi',
    packages=[ 'battlesnake' ],
    include_package_data=True,
    install_requires=["flask", "redis", "waitress"]
)
