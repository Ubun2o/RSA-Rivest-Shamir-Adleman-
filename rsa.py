#!/usr/bin/python

# Import functions 
import os
import sys
import fractions
import time
from random import choice

# Function to decrypt a message
def decrypt():
    done = 'false'
    emessage = []
    dmessage = []
    plaintext = []
    message = []
    another_test = 'false'

	# Loop infinitely until user exits this menu  
    while True:
        os.system('cls')
        print "+--------------------------------------------+"
        print "| Welcome to the RSA Cryptosystem simulator  |"
        print "+--------------------------------------------+"
        print "| Decrypt a message                          |"
        print "|                                            |"
        print "| To go back a menu type 'back' at any time  |"
        print "| and hit the 'enter' key                    |"
        print "+--------------------------------------------+"
        print "\n"

		# Take the first cipherblock of the message to decrypt from the user
        ciphertext = str(raw_input("Please enter the first message block of the message you would like to decrypt: "))
        if ciphertext == 'back':
            main()
			
		# Append the first cipherblock of the message to an array
        ciphertext = int(ciphertext)
        emessage.append(ciphertext)

		# Start loop and keep asking the user if there are more cipherblocks to enter and append to array
        while done != 'true':
            decision = str(raw_input("Would you like to enter another message block? "))
            print "\n"
            if decision == 'y':
                ciphertext = int(raw_input("Please enter another block of the message you would like to decrypt: "))
                emessage.append(ciphertext)
                done = 'false'
            elif decision == 'n':
                done = 'true'

		# If there are no more cipherblocks ask the user to enter the private key values 
        print "Please enter your private key(n, d)"
        n = str(raw_input("Please enter the value for n: "))
        if n == 'back':
            main()

        d = str(raw_input("Please enter the value for d: "))
        if d == 'back':
            main()

		# Convert private key values (n, d) into integers
        n = int(n)
        d = int(d)

		# Display the ciphertext that is going to be be decrypted
        print "\nYour encrypted message block:", " ".join(map(str, emessage))
        print "\nStarting decryption process...\n"
		
		# Start timer to calculate how long the decryption process takes
        start = int(time.time())

		# For each cipherblock use the value of the decryption key to get decrypted values and append to array
        for i in emessage:
            dchar = (i ** d) % n
            dmessage.append(dchar)

		# for each decrypted value find division and modulus and append to array
        for i in dmessage:
            division = i / 26
            plaintext.append(division)
            modulus = i % 26
            plaintext.append(modulus)

		# Get the length of the plaintext message
        plaintext_len = len(plaintext)

		# If the length of the plaintext message is divisible by two
        if plaintext_len % 2 == 0:
			# And if the last element of the array equals zero i.e. it was packed with a zero (A) because the original plaintext message was an odd length
			# Remove value from the array
            if plaintext[(plaintext_len - 1)] == 0:
                plaintext.pop(plaintext_len - 1)

		# For every base26 value calculate the equivalent letter and append to array
        for i in plaintext:
            message.append(chr(i + 65))

		# Display the decrypted message block and the time taken to complete the decryption process
        print "\nYour decrypted message block:", " ".join(map(str, message))
        print "Time taken to complete process:", round(time.time() - start, 3), "seconds" + "\n"

		# If the user does not want to continue go back to the main menu or decrypt another message if they do want to continue
        cont = str(raw_input("\nWould you like to decrypt another message? "))
        if cont == 'y':
            decrypt()
        elif cont == 'n':
            main()

# Function to encrypt a message						
def encrypt():
    caesar = []
    m1 = []
    m2 = []
    test = 'no'

	# Loop infinitely until user exits this menu  
    while True:
        os.system('cls')
        print "+--------------------------------------------+"
        print "| Welcome to the RSA Cryptosystem simulator  |"
        print "+--------------------------------------------+"
        print "| Encrypt a message                          |"
        print "|                                            |"
        print "| To go back a menu type 'back' at any time  |"
        print "| and hit the 'enter' key                    |"
        print "+--------------------------------------------+"
        print "\n"

		# Take plain text message to encrypt from user
        plaintext = str(raw_input("Please enter the message you would like to encrypt: "))
        if plaintext == 'back':
            main()

		# Enter public key values
        print "\nPlease enter your public key(n, e)"
        n = str(raw_input("Please enter the value for n: "))
        if n == 'back':
            main()

        e = str(raw_input("Please enter the value for e: "))
        if e == 'back':
            main()

		# Convert public key values (n, e) into integers
        n = int(n)
        e = int(e)

		# Start timer to calculate how long the encryption process takes 
        print "\nStarting encryption process...\n"
        start = int(time.time())

		# For each character in the plaintext message get the base26 equivalent and append to array
        for char in plaintext:
            newchar = ord(char) - 65
            caesar.append(newchar)

		# If the length of the plaintext message is not divisble by 2 i.e. It is odd
		# Pack a zero (A) to the right in the last block
        if len(plaintext) % 2 != 0:
            caesar.append((ord('A') - 65))
        elif len(plaintext) % 2 == 0:
			pass

		# Do 2-digit block encryption and append to new array
        for x in range(0, len(caesar), 2):
            m1.append((caesar[x] * 26) + caesar[x + 1])

		# Enciper every block using the value of the encryption key
        for i in m1:
            echar = (i ** e) % n
            m2.append(echar)

		# Display the encrypted message and time taken to complete the encryption process
        print "Your encrypted message", " ".join(map(str, m2))
        print "Time taken to complete process:", round(time.time() - start, 3), "seconds" + "\n"

		# If the user does not want to continue go back to the main menu or encrypt another message if they do want to continue
        cont = str(raw_input("\nWould you like to encrypt another message? "))
        if cont == 'y':
            encrypt()
        elif cont == 'n':
            main()
			
# Function to generate public/private key pairs
def generate_keys():
    key_gen = 'no'
	
	# Loop infinitely until user exits this menu  
    while key_gen != 'yes':
        os.system('cls')
        print "+--------------------------------------------+"
        print "| Welcome to the RSA Cryptosystem simulator  |"
        print "+--------------------------------------------+"
        print "| Generate Public/Private key pairs          |"
        print "|                                            |"
        print "| To go back a menu type 'back' at any time  |"
        print "| and hit the 'enter' key                    |"
        print "+--------------------------------------------+"
        print "\n"
		
		# Take prime numbers from user input
        p = str(raw_input("Enter first prime number (p): "))
        if p == 'back':
            main()

        q = str(raw_input("Enter second prime number (q): "))
        if q == 'back':
            main()

        print "\nCalculation:\n"
		
		# Convert prime numbers p and q into integers 
        p = int(p)
        q = int(q)

		# Calculate the product (n) of the two prime numbers and display the calculation and result
        n = p * q

        print "n = p * q"
        print "%s = %s * %s" % (n, p, q)
		
		# Find the totient of the product of the prime numbers (all the positive values up to the integer (n) that a relatively prime to (n)) 
        z = (p - 1) * (q - 1)

		# Display the calculation used to find the totient and the result
        print "\nz = (p - 1) * (q - 1)"
        print "%s = (%s - 1) * (%s - 1)" % (z, p, q)

        i = 2
        e = []
        d = int()
        counter = 1
        solution = int()

        print "\nGenerating a public/private key pair...\n"
		
		# Start timer to calculate how long the public/private keygen process takes 
        start = int(time.time())
	
		# Find all the integers (e) such that e and z have no common divisors 
        while i != z:
            if fractions.gcd(i, z) == 1:
                e.append(i)
                i += 1
            else:
                i += 1
				
		# Pick a random choice for e
        e = choice(e)

		# Do while the solution (d) has not been found (if the result of the calculation is 1 then solution (d) becomes the value of counter)
        while solution != 1:
            solution = (counter * e) % z
            if solution == 1:
                d = counter
            else:
                counter += 1

		# Display the public/private key pair values 
        print "+-----------------------------------------------------+"
        print "          public key(n, e): (" + str(n) + ", " + str(e) + ")"
        print "          private key(n, d): (" + str(n) + ", " + str(d) + ")"
        print "+-----------------------------------------------------+"

		# Display the time it has taken to complete the process
        print "\nTime taken to complete process:", round(time.time() - start, 3), "seconds"
        cont = str(raw_input("\nWould you like to generate another public/private key pair? "))

		# If the user does not want to continue go back to the main menu or generate another key pair if they do want to continue
        if cont == 'y':
            generate_keys()
        elif cont == 'n':
            main()

# Function for main menu
def main():
    os.system('cls')
    while True:

        print "+--------------------------------------------+"
        print "| Welcome to the RSA Cryptosystem simulator  |"
        print "+--------------------------------------------+"
        print "| Please select from the following options:  |"
        print "|                                            |"
        print "|   1) Generate Public/Private key pairs     |"
        print "|   2) Encrypt a message                     |"
        print "|   3) Decrypt a message                     |"
        print "|                                            |"
        print "| To quit the program type 'exit'            |"
        print "+--------------------------------------------+"
        print "\n"
        user_option = str(raw_input("Select your option and hit the 'enter' key: "))

		# User options: [1] Generate Public/Private key pairs, [2] Encrypt a message, [3] Decrypt a message
        if user_option == '1':
            print generate_keys()
        elif user_option == '2':
            print encrypt()
        elif user_option == '3':
            print decrypt()
        elif user_option == 'exit':
            os.system('cls')
            sys.exit()

main()
