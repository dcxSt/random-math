import numpy as np

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

def encryptMessageSimple():
	return

if __name__=="__main__":
	# get the message:
	message = input("your secret message:\n")
	### preprocessing - turn it into strings of ones
	message = message.replace(" ","")	# take out all spaces
	binaryMessage = [charToNum[char] for char in message]	# assume all chars in our dic
	print('your message in binary looks like \n{}'.format(binaryMessage))
	#p = int(input('enter prime p: '))
	#q = int(input('enter prime q: '))
	p,q = 17,7
	n = p*q
	lambdaN = np.lcm(p-1,q-1) 	# compute charmichael's totient function
	print("lambdaN, and %5= {} , {}".format(lambdaN,lambdaN%5)) #trace
	d = 5 # we chose dee to be equal to for simplicity 
	e = gete(lambdaN) # assumes d=5 for simplicity
	
	scrambled = encrypt(binaryMessage,e,n)
	print("Here is your scrabled message in binary form\n\n{}\n\n".format(scrambled))

	# now we unscrable it to see if decryption works :)
	unscrabled = decrypt(scrambled,d,n)
	print("here is you unscrabled message in binary form\n\n{}\n\n".format(unscrabled))

	print("cya!")	




