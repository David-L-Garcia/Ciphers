import cipher

print ("///////////////////////////////")
print ("/Welcome to the Caeser Cipher!/")
print ("///////////////////////////////\n\n")
choice = str(raw_input("Do you want to encrypt or decrypt?"))
if (choice.lower() ==  "encrypt"):
	cipher.crypt()
elif (choice.lower() ==  "decrypt"):
	cipher.decrypt()
else:
	print "invalid input"
