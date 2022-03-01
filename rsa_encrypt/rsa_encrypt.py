import numpy as np
import random
import re

charToNum={
'a':'00001',
'b':'00010',
'c':'00011',
'd':'00100',
'e':'00101',
'f':'00110',
'g':'00111',
'h':'01000',
'i':'01001',
'j':'01010',
'k':'01011',
'l':'01100',
'm':'01101',
'n':'01110',
'o':'01111',
'p':'10000',
'q':'10001',
'r':'10010',
's':'10011',
't':'10100',
'u':'10101',
'v':'10110',
'w':'10111',
'x':'11000',
'y':'11001',
'z':'11010'
}

numToChar = {v: k for k,v in charToNum.items()} # reverses the dictionary

def gete(lambdaN): # assumes e=3 for simplicity
	if (lambdaN+1) % 5 == 0:
		return int((lambdaN+1)/5)
	elif (2*lambdaN+1)%5 == 0:
		return int((2*lambdaN+1)/5)
	elif (3*lambdaN+1)%5 == 0:
		return int((3*lambdaN+1)/5)
	elif (4*lambdaN+1)%5 == 0:
		return int((4*lambdaN+1)/5)
	elif (5*lambdaN+1)%5 == 0:
		print("I don't think this should happend"*3)
		return int((5*lambdaN+1)/5)
	raise Exception('Something went terribly wrong in your brain my dear steve.')

def charBinaryToDecimal(stringRep):
	listRep = [int(i) for i in stringRep]
	listRep.reverse()
	#print(listRep)#trace
	decimal = sum([(2**i)*j for i,j in enumerate(listRep)])
	return decimal


def decrypt(scrambledMessage,d,n): # rem d=3 and n=p*q
	# the scrambledMessage is just m^e
	# here we use a baby rsa protocol where you unscrable each letter (length five binary diget) as a different message
	unscrambled = [charBinaryToDecimal(i)**d%n for i in scrambledMessage]
	unscrambled = ["{0:b}".format(i) for i in unscrambled] # put back into binary format
	return unscrambled
	
def encrypt(binaryMessage,e,n):
	scrambled = [charBinaryToDecimal(i)**e%n for i in binaryMessage]
	scrambled = ["{0:b}".format(i) for i in scrambled]
	return scrambled

def addRandomTwoDigits(binMessage):
	newMessage = [i for i in binMessage]
	for j,binChar in enumerate(binMessage):
		# assumes that they are of length 5, simply adds two random 0/1 chars
		a,b=random.choice(['0','1']),random.choice(['0','1'])
		newMessage[j] = a+b+binChar
	return newMessage

def encryptMessage():
	message = input("your secret message:\n")
	message = message.replace(" ", "")
	binaryMessage = [charToNum[char] for char in message]
	print('your message in binary looks like \n{}'.format(binaryMessage))
	binaryMessage = addRandomTwoDigits(binaryMessage)
	print('your message in binary with two random digets appended looks like \n{}'.format(binaryMessage))
	p,q = 17,7
	n = p*q
	lambdaN = np.lcm(p-1,q-1)
	d = 5
	e = gete(lambdaN) # assumes d=5 for simplicity
	scrambled = encrypt(binaryMessage,e,n)
	print("Here is your scrambled message in binary form\n\n{}\n\n".format(scrambled))
	print("writing to scrambled_message.txt")
	with open('scrambled_message.txt','w') as f:
		#for char in scrambled:
		f.writelines([i+'\n' for i in scrambled])
	return scrambled

def decryptMessage(scrambled,d,n):
	unscrambled = decrypt(scrambled,d,n)
	# take off the random 1/0 padding
	unscrambled = [str(i) for i in unscrambled]
	print("unscrabled binary \n\n{}\n\n".format(unscrambled))
	for j,i in enumerate(unscrambled):
		if len(i)>7:
			raise Exception("len should be smaller than or equal to 7")
		elif len(i)>5:
			unscrambled[j] = unscrambled[j][len(i)-5:]	
		elif len(i)<5:
			unscrambled[j] = '0'*(5-len(i))+unscrambled[j]
	unscrambledString = [numToChar[i] for i in unscrambled]
	print("unscrambled String:")
	print(unscrambledString)
	return unscrambledString

def decryptFromTxt(fname):
	with open(fname,"r") as f:
		rawMessage = f.readlines()
	message = []
	for i in rawMessage:
		out = re.search("(0|1){1,7}",i)
		if out: message.append(out[0])
	return decryptMessage(message,5,7*17)

if __name__=="__main__":
    scrambled = encryptMessage()
    print("scrmbled message: {}".format(scrambled))
    unscrabled = decryptMessage(scrambled,5,7*17)
    
# # to unscramble a message uncomment following block and comment out previous, 
# # then enter your message in list of strings format as indicated
# if __name__=="__main__":
#     scrambled = ["0111111","0101010","1100101","0101111","1100111","1010111","0110101",
#             "0101110","1011110","1101011"]
#     unscrambled = decryptMessage(scrambled,5,7*17)
#     print("unscrambled: {}".format(unscrambled))
	
"""

if __name__=="__main__":
	# get the message:
	message = input("your secret message:\n")
	### preprocessing - turn it into strings of ones
	message = message.replace(" ","")	# take out all spaces
	binaryMessage = [charToNum[char] for char in message]	# assume all chars in our dic
	print('your message in binary looks like \n{}'.format(binaryMessage))
	p,q = 17,7
	n = p*q
	lambdaN = np.lcm(p-1,q-1) 	# compute charmichael's totient function
	print("lambdaN, and %5= {} , {}".format(lambdaN,lambdaN%5)) #trace
	d = 5 # we chose dee to be equal to 5 for simplicity 
	e = gete(lambdaN) # assumes d=5 for simplicity
	
	scrambled = encrypt(binaryMessage,e,n)
	print("Here is your scrabled message in binary form\n\n{}\n\n".format(scrambled))

	# now we unscrable it to see if decryption works :)
	unscrabled = decrypt(scrambled,d,n)
	print("here is you unscrabled message in binary form\n\n{}\n\n".format(unscrabled))

	print("cya!")	

"""


