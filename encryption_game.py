#/ 1. Program imports text file lines. 
#/ 2. Program appends each line to list.
#/ 3. Program selects random line in list.
#/ 4. Program encrypts random line, generates key & coded message.
#/ 5. Key is displayed as ***. Random [x] amount of characters are revealed.
# 6. User guesses characters in key.
# 7. If character in key, updates and return key with guessed characters.
# 8. Continues until user enters correct encryption key. 
# 9. 2 failed characters will reveal 2 characters in the encyption key.
# 10. When user completes the key, their scoreboard will be recorded.

from cryptography.fernet import Fernet
from random import randrange
from encryption_module.random_select import random_list_select
# from encryption_module.encryption_list import encrypt_list
import encryption_module.encryption_list as encryption_list


#   Import message.txt
message_list = []
with open("./message_file.txt", mode="r") as message_file:
    for line in message_file:
        # print(line)
        message_list.append(line)
# print(message_list)
# print(len(message_list))


#   Randomly select message
message = random_list_select(message_list).encode()
#print(f"This is message: {message}")


#   Encryption stage
key = Fernet.generate_key()
base_key =  Fernet(key)
play_keys = encryption_list.encrypt_list(base_key)
#print(f"Hidden and Showing Keys: {play_keys}")


encryption = base_key.encrypt(message)
#print(f"Encrypted Message: {encryption}")
decryption = base_key.decrypt(encryption)
#print(f"Decrypted Message: {decryption}")


#   Set-up showing encryption list (display x amount of hidden characters)
play_keys = encryption_list.show_start(play_keys)
#print(play_keys)


#   initiate game 
control = 0
fail_list = []

print("-- This is Encryption Hand-man! --\n\n")
print("-- You have intercepted an encrypted message --\n")
print(f"[  Encrypted Message: {encryption}  ]\n")
print("-- Guess the characters, Special, Number and Letter, that is in the encryption key --")
print("-- If you guess correct, the character will reveal. --")
print("-- Once you find the encryption key, you can intercept the hiddne message! --\n\n")

while control == 0:
    #print(f"control {control}\n\n")
    encrypt_total = len(play_keys[0])
    encrypt_hit = play_keys[1].count("*")
    encryption_status = f"Progress: {play_keys[1].count("*")}/{len(play_keys[0])}"
    print(f"-- Score: {encryption_status} --")
    print(f"-- This is a record of all the Missed characters --\n")
    print(f"[-- {fail_list} --]\n\n")

    if encrypt_hit == 0:
        control = control + 1
    else:

        #   validate options
        while True:
            try:
                status = int(input("-- Do you want to continue[1], get hints[2], or finish[3]? --\n"))
                break 
            except ValueError:
                print("Please input [1], [2], or [3]")
        # print(status)
        # print(type(status)) 


        #   select loop
        if status == 1:
            # Loop check to validify user input
            chr = input("-- Guess a charcater! *(only one at a time!) --")
            while len(chr) != 1:
                chr = input("-- Said only one character at a time!: --")

            # if input in encryption key, flip to reveal, or store failed input in list
            if chr in play_keys[0]:
                play_keys = encryption_list.show_flip(chr, play_keys)
                #print(play_keys[0])
                print(play_keys[1])
            else:
                fail_list.append(chr)
                print("-- You Missed! --")
                print(f"-- [ {chr} ] is not in the encryption key --")

        elif status == 2:
            print("\n\nI'll give you 3 hints!")
            play_keys = encryption_list.hint_flip(play_keys)
            #print(play_keys[0])
            print(play_keys[1])

        elif status == 3:
            control = 1
        
        print("\n ----------------------------------------------------------------------------------------------\n\n\n")


        # if user 

print("--- Report ---\n")
score = play_keys[1].count("*")
print(f"Score: {play_keys[1].count("*")}/{len(play_keys[0])}\n\n")

if score == 0:
    print("Congradualtions!, You broke the encryption! Lets see the message you decrypted!\n")
    print("--- Message --- \n")
    print(f"[ Decrypted Message: {decryption}  ]\n")
    print("-- Thank you for playing! --\n\n")

else:
    print("You weren't able to break the encryption...")
    print("Oh well, you still have the encrypted message to read...\n")
    print("--- Message --- \n")
    print(f"[ Decrypted Message: {encryption}  ]\n")
    print("-- Thank you for playing! --\n\n")
        

# alpha = "abcde daa"
# alpha_list = list(alpha)
# print(alpha_list)
# print(alpha_list.index("d"))
# for index, value in enumerate(alpha_list):
#     if value == "a":
#         print(index, value)