# just makes a 1 to 1 map with letters chosen at random
import random

message = input("type your message here:\t")

alphabet = "qwertyuiopasdfghjklzxcvbnm"
alphabet2 = [i for i in alphabet]
random.shuffle(alphabet2)
letmap = {}
for i in range(len(alphabet)):
    letmap[alphabet[i]]=alphabet2[i]

scrambled_message = ""
for i in message:
    if i in alphabet:
        scrambled_message = scrambled_message + letmap[i]
    else:
        scrambled_message = scrambled_message + i

print("your scrambled message is",scrambled_message)
with open("simple_random_map.txt","w") as f:
    f.write(scrambled_message)
    f.close()



