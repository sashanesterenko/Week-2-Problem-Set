names = ['Basil', 'Mary', 'Peter', 'Valery', 'Sasha', "Donna"]

def find_person():
    while names:
        name = names.pop()
        if name == 'Valery':
            print('Here he is!')
find_person()