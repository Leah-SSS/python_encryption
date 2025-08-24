from random import randrange

def random_list_select (list):
    count = len(list)
    choice = randrange(count)
    return list[choice]
    