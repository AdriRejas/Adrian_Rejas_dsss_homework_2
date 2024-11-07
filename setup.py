from setuptools import setup, find_packages

setup(
    name="math_quiz_project",                 
    version="0.1",
    packages=find_packages(),
    install_requires=[],                       
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz",  
        ]
    },
    author="Adrian Rejas Llamera",
    author_email="rejasllamera@gmail.com",
    description="A simple math quiz game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AdriRejas/Adrian_Rejas_dsss_homework_2.git",  
    license="Apache License 2.0",
)
