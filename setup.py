from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement_lst = []
    try:
        with open('requirements.txt','r') as file:
            # read lines from the file
            lines=file.readlines()
            ## process each line
            for line in lines:
                requirement=line.strip()
                # ignore -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("The requirements.txt file was not found.")
    return requirement_lst


setup(
    name='Network_security_system',
    version='0.0.1',
    author='K Sriganesh',
    author_email="sriganeshkavali@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)