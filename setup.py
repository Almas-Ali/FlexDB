import setuptools

with open("README.md", "r") as README:
    long_description = README.read()

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development :: Libraries :: Python Modules"
    "Topic :: Database",
    "Natural Language :: English",
    "Environment :: Console",
    "Environment :: Web Environment",
]

setuptools.setup(
    name="FlexDB",
    version="0.0.1",
    description="FlexDB - A simple, fast, and lightweight database for storing and retrieving data.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/Almas-Ali/FlexDB",
    author="Md. Almas Ali",
    author_email="almaspr3@gmail.com",
    keyword="Database, Database Management System, DBMS, Database Library, Python Database, FlexDB, FlexDB Library, FlexDB Database, FlexDB Database Management System, FlexDB DBMS, FlexDB Database Library, FlexDB Python Database",
    license="GNU General Public License v3 (GPLv3)",
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    install_requires=[],
)
