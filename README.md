# FlexDB

A simple, fast, and lightweight database for storing and retrieving data.

Created by [**@Almas-Ali**](https://github.com/Almas-Ali)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [License](#license)

## Features

- Simple and easy to use
- Fast and lightweight
- Stores any data type
- Stores data in a encrypted binary file

## Installation

```bash
pip install flexdb
```

## Usage

```python
from flexdb import FlexDB # Import the database

db = FlexDB() # Create a database instance
db.connect('flex.db') # Connect to the database

db.set('name', 'Almas') # Set a key and value pair any data type can be used

db.get('name') # Get the value of a key
db.get_all() # Get all the key and value pairs

db.delete('name') # Delete a key and value pair

db.commit() # Commit the changes to the database

db.close() # Close the database
```

## Documentation

- [Website](https://almas-ali.github.io/FlexDB/)
- [GitHub](https://github.com/Almas-Ali/FlexDB)
- [PyPI](https://pypi.org/project/flexdb/)


## License

Free to use and modify under the [**MIT License**](https://github.com/Almas-Ali/FlexDB/blob/master/LICENSE)