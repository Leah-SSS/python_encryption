from cryptography.fernet import Fernet
from random import randrange

def encrypt_list(key):
    #   stringifies key (from fernet data type)
    str_key = str(key)

    #   list-ifies string key, removing [byte] + [""] elements
    hidden_list = list(str(key))
    del hidden_list[0]
    del hidden_list[0]
    del hidden_list[-1]

    # generates a hidden [*] list of equal length to hidden_list
    show_list = []
    for chr in hidden_list:
        show_list.append("*")
   
    return [hidden_list, show_list]


def show_start(list):
    # defines how much chr will show (loop duration)
    list_limit = len(list[0])
    taken_num = []
    for n in range(randrange(15, 21)):
        # chose random number in length list
        hit_chr = randrange(list_limit)
        while hit_chr in taken_num:
            hit_chr = randrange(list_limit)
        list[1][hit_chr] = list[0][hit_chr]

        # register number as taken so no duplicate
        taken_num.append(hit_chr)
    #print(f"Showing Index: {taken_num}")
    return list


def show_flip(input, list):
    hit = []

    # loops to catch all instances of input in list[0]
    for index, value in enumerate(list[0]):
        if value == input:
            print(f"Nice!, You got these hits in the encryption: \n -- {index, value} --")
            hit.append(index)

    # if hits exits, then start flipping(OUT!)
    if len(hit) > 0:
        # Use entries in hit as index reference to show display list[0]
        for n in hit:
            list[1][n] = list[0][n]
    return list


def hint_flip(list):
    # [*] count how much, if > 3 set hint limit
    counter = 0
    for index, value in enumerate(list[1]):
        if value == "*":
            counter = counter+1

    # collect [*] hidden key characters
    hidden_indeces = []
    for index, value in enumerate(list[1]):
        if value == "*":
            hidden_indeces.append(index)
    
    if counter > 3:
        # choose 3 hidden key characters
        hidden_choice = [0]
        while len(hidden_choice) < 4:
            # chose the random flipping index
            random_choice = randrange(0, len(hidden_choice))
            # get the value from hidden_indeces index(random choice)
            chosen_one = hidden_indeces[random_choice]
            hidden_choice.append(chosen_one)

            # remove the index from list so no duplicates
            del hidden_indeces[random_choice]

        del hidden_choice[0]

        for n in hidden_choice:
            list[1][n] = list[0][n]
        return list
    
    else: 
        list[1] = list[0]
        return list


        


    