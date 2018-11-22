#Caesar Cipher
def loOver(x):
	new = x - 122
	new += 96
	return chr(new)
	
def upOver(x):	
	new = x - 90
	new += 64
	return chr(new)
	
def loUnder(x):
	new = 97 - x
	new = 123 - new 
	return chr(new)
	
def upUnder(x):
	new = 65 - x
	new = 91 - new 
	return chr(new)
	
def upCryp(x, key):
	z = ''
	cry = x + key
	if (cry > 90):
		z = upOver(cry)
	else:
		z = chr(cry)
	return z
	
def loCryp(x, key):
	z = ''
	cry = x + key
	if (cry > 122):
		z = loOver(cry)
	else:
		z = chr(cry)
	return z
	
def upDe(x, key):
	z = ''
	cry = x - key
	if (cry < 65):
		z = upUnder(cry)
	else:
		z = chr(cry)
	return z
	
def loDe(x, key):
	z = ''
	cry = x - key
	if (cry < 97):
		z = loUnder(cry)
	else:
		z = chr(cry)
	return z
		
def crypt():
	orig = raw_input("What message do you want to encrypt?")
	key = int(raw_input("What is the key?"))
	z = ''
	for letters in range(len(orig)):
		x = ord(orig[letters])
		if(x >= 65 and x <= 90):
			z += upCryp(x, key)
		elif(x >= 97 and x <= 122):
			z += loCryp(x, key)
		else:
			z += orig[letters]
	print z
	
def decrypt():
	orig = raw_input("What message do you want to decrypt?")
	key = int(raw_input("What is the key?"))
	z = ''
	for letters in range(len(orig)):
		x = ord(orig[letters])
		if(x >= 65 and x <= 90):
			z += upDe(x, key)
		elif(x >= 97 and x <= 122):
			z += loDe(x, key)
		else:
			z += orig[letters]
	print z