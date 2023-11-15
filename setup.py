
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas", "matplotlib","numpy"]

setup(
    name="anamofo",
    version="1.0.1",
    author="yuanttx",
    author_email="yuanttx@gmail.com",
    description="A project for processing bioinformation analysis",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/YUANTTX/anamofo/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
