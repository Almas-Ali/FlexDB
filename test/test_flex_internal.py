from flexdb import FlexDB

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