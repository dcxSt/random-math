# a python script that makes your words hard to read

message = input("type your message here:\t")

message = message.split(" ")

new_message = ""

for word in message:
    word_cp = word[:]
    while word_cp:
        if len(word_cp) >= 2:
            new_message = new_message + word_cp[1] + word_cp[0]
            word_cp = word_cp[2:]
        else:
            new_message = new_message + word_cp
            word_cp = None
    new_message = new_message + " "

with open("scrambled_message.txt","w") as f:
    f.write(new_message)
print(new_message)
        


