#  File: Cipher.py

#  Description:

#  Student Name: Nicholas Webb

#  Student UT EID: nw6887

#  Partner Name: EJ Porras

#  Partner UT EID: ejp2488

#  Course Name: CS 313E

#  Unique Number: 51135

#  Date Created: 2/8/2022

#  Date Last Modified: 2/8/2022

import math

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt(strng):

	string_to_encyrpt = strng
	size = math.sqrt(len(string_to_encyrpt))

	# changes the length of string until it can fit into square matrix
	while size ** 2 != len(string_to_encyrpt):
		string_to_encyrpt += "*"

	# inserts characters in the string to be encrypted into the square matrix
	p1 = []
	for i in range(size):
		p2 = []
		for j in range(size):
			p2.append(string_to_encyrpt[0])
			string_to_encyrpt = string_to_encyrpt[1:]
		p1.append(p2)

	# rotates square matrix clockwise by 90 degrees
	for i in range(size // 2):
		for j in range(i, size - i - 1):
			temp = p1[i][j]
			p1[i][j] = p1[size - j - 1][i]
			p1[size - j - 1][i] = p1[size - i - 1][size - j - 1]
			p1[size - i - 1][size - j - 1] = p1[j][size - i - 1]
			p1[j][size - i - 1] = temp

	encrypted_string = ""

	# traverses through matrix to record the encrypted string
	for i in range(size):
		for j in range(size):
			if p1[i][j] == "*":
				continue
			else:
				encrypted_string += p1[i][j]

	return encrypted_string

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
	pass

def main():

	# read the strings P and Q from standard input
	p_str = input()
	q_str = input()

	try:
		while True:

			# encrypt the string P
			printed_encryption = encrypt(p_str)

			# decrypt the string Q
			printed_decryption = decrypt(q_str)

			# print the encrypted string of P
			print(printed_encryption)

			# and the decrypted string of Q
			print(printed_decryption)

	except EOFError:
		pass

if __name__ == "__main__":
  main()


