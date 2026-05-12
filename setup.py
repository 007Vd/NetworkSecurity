from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    #list of req.
    req_lst=[]
    try:
        with open("requirements.txt",'r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    req_lst.append(requirement)


    except FileNotFoundError:
        print("requirement.txt not found")
    return req_lst

setup(
   name="NetworkSecurity",
   version="0.0.1",
   author="007Vd",
   author_email="vdeogade007@gmail.com",
   packages=find_packages(),
   install_requires=get_requirements()
)
