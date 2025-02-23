from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function reads the requirements file and returns a list of requirements.
    :param file_path: The file path to the requirements file.
    :return: requirements list of string values
    '''

    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='D:\Machine-Learning',
    version='0.0.1',
    packages=find_packages(),
    author='4HS33N',
    install_requires=get_requirements('requirements.txt'),
)