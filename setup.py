# Python applications generally have a requirements.txt file and a setup.py file.

# requirements.txt is a plain text file that lists down the python package requirements.

# setup.py is a python script that uses setuptools to define a package. setup.py also contains the list of dependencies to be installed along with all the other metadata about the package.

# If you define your dependencies in both places this is a redundancy. -e . is the way you can overcome this problem. You can just define your dependencies in setup.py alone and create requirements.txt file with just -e . in it.

# You can now use pip install -r requirements.txt without defining all the dependencies again in the requirements file. All the packages in setup.py are automatically installed, setup.py becomes your single source of truth for what dependencies are to be installed.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# requirements.txt—This file is used by pip to install all of the dependencies for your application. In this case, it contains only -e . This tells pip to install the requirements specified in setup.py. It also tells pip to run

# So it tells pip to install the requirements specified in setup.py.

from setuptools import setup,find_packages
from typing import List


EDITABLE = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''Returns a list of requirements to be supplied to setup'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() #https://www.tutorialspoint.com/python/file_readlines.htm
        requirements = [req.replace("\n","") for req in requirements]

        if EDITABLE in requirements:
            requirements.remove(EDITABLE)
    return requirements



setup(
    name= 'recommend recipes',
    version='0.0.1',
    author='Kamalashree',
    author_email='Kamalashree.sudhakar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)