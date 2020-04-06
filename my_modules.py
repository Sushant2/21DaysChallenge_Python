print('Imported my_modules...')
test = 'Test String'

def find_index(top_search, target):
    '''find the index of a value in a sequence'''
    for i, values in enumerate(top_search):
        if values == target:
            return i
    return -1

