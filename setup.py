from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this functon will return the list of requirements
    :param file_path: shld be a string type
    :return: a list
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name="mlproject_01",
    version="0.0.1",
    author='sibibalan',
    author_email='sibibalan94@gmail.com',
    packages=find_packages(),
    install_requries=get_requirements('requirements.txt')
    )