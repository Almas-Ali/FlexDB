import json
import pickle
from typing import TextIO, BinaryIO
import os


class FlexDB:
    '''A simple database class'''

    def __init__(self) -> None:
        self.__data = {}

    def set(self, key: any, value: any) -> None:
        '''Set data'''
        self.__data[key] = value

    def get(self, key: any) -> any:
        '''Get data'''
        return self.__data[key]

    def get_all(self) -> dict:
        '''Get all data'''
        return self.__data

    def get_keys(self) -> list:
        '''Get all keys'''
        return self.__data.keys()

    def get_values(self) -> list:
        '''Get all values'''
        return self.__data.values()

    def get_items(self) -> list:
        '''Get all items'''
        return self.__data.items()

    def get_len(self) -> int:
        '''Get length of database'''
        return len(self.__data)

    def get_type(self, key) -> type:
        '''Get data type of a key'''
        return type(self.__data[key])

    def get_size(self, key) -> int:
        '''Get size of a key'''
        return len(self.__data[key])

    def delete(self, key) -> None:
        try:
            del self.__data[key]
            return True
        except KeyError:
            return False

    def delete_all(self) -> None:
        self.__data = {}

    def delete_keys(self, keys: list) -> None:
        for key in keys:
            del self.__data[key]

    def delete_values(self, values: list) -> None:
        for key, value in self.__data.items():
            if value in values:
                del self.__data[key]

    def delete_items(self, items: list) -> None:
        for item in items:
            del self.__data[item[0]]

    def delete_len(self, length: int) -> None:
        for key in list(self.__data.keys())[:length]:
            del self.__data[key]

    def delete_type(self, type) -> None:
        for key in self.__data.keys():
            if type(self.__data[key]) == type:
                del self.__data[key]

    def drop_db(self) -> None:
        self.__data = {}
        if os.path.exists(self.__db_name):
            os.remove(self.__db_name)
            return True
        else:
            return False

    def connect(self, __db_name: str) -> None:
        '''Connect to database'''
        self.__db_name = __db_name

        if os.path.exists(self.__db_name):
            with open(self.__db_name, 'rb') as f:
                self.__data = pickle.load(f)
        else:
            with open(self.__db_name, 'wb') as f:
                pickle.dump(self.__data, f)

    def commit(self) -> None:
        '''Commit changes'''
        if os.path.exists(self.__db_name):
            with open(self.__db_name, 'wb') as f:
                pickle.dump(self.__data, f)

    def close(self) -> None:
        '''Close database'''
        self.__data = {}
        self.__db_name = ''

    def execute(self, command: str) -> None:
        '''Execute commands'''
        command = command.split()

        if command[0] == 'SET':
            self.set(command[1], ' '.join(command[2:]))
            return 'Set'

        elif command[0] == 'GET':
            self.get(command[1])
            return self.get(command[1])

        elif command[0] == 'DELETE':
            self.delete(command[1])
            return 'Deleted'

        else:
            print('Invalid command')
            return False


if __name__ == '__main__':
    # db = FlexDB()
    # db.connect('test.FlexDB')

    # db.set('name', 'almas')
    # db.set('age', 20)
    # db.set('data', [1, 2, 3, 4, 5])
    # db.set('data2', {'name': 'almas', 'age': 20})

    # db.commit()
    # db.close()

    db2 = FlexDB()
    db2.connect('test.FlexDB')

    # with open('test.FlexDB', 'rb') as f:
    #     print(f.readlines())

    # print(db2.get_all())
    # print(db2.get('data'))

    # print(db2.execute('SET name almas    ali  ')) # Data is trimmed not exactly as in the command.
    # db2.set('name', 'almas    ali')
    # print(db2.get_type('data2'))

    # print(db2.get_len())

    # print(db2.get_keys())
    # print(db2.get_values())
    # print(db2.get_items())

    # print(db2.delete('name'))
    
    
    print(db2.drop_db())
    print(db2.get_all())
    # db2.commit()
    db2.close()