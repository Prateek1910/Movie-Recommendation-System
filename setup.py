from setuptools import setup

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()
    

AUTHOR_NAME ='PRATEEK PAREEK'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit'] # streamlit is helpful to use html code without writing html codes 

setup(
    name= SRC_REPO,
    version='0.0.1',
    author= AUTHOR_NAME,
    author_email='prateekpareek19@gmail.com',
    description='A small example package for movies recommendation',
    long_description= long_description,
    long_description_content_type='text/markdown',
    #url= 'http:// github link of mine
    package=[SRC_REPO],
    python_requires = '>=3.7',
    install_requires= LIST_OF_REQUIREMENTS,
)
