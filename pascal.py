#!/home/steve/anaconda3/bin/python3

def next_row(row):
    new_row=[1]
    for i in range(len(row)-1):
        new_row.append(row[i]+row[i+1])
    new_row.append(1)
    return new_row

def mod_row(row,mod=2):
    new_row=[]
    for i in range(len(row)):
        new_row.append(row[i]%mod)
    return new_row


# main
usr_in = input("how many rows? just press enter for default of 15: ")
mod = None
try: n = int(usr_in)
except: 
    if 'mod' in usr_in:
        try:
            n = int(usr_in[:usr_in.index('mod')])
            mod = int(usr_in[usr_in.index('mod')+3:])
            print("trace")# trace
        except: n=15
    else: n = 15

row = [1]
for i in range(n):
    for i in row:
        print(i,end="  ")
    print()
    row = next_row(row)
    if mod: row = mod_row(row,mod=mod)
    

