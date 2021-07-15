# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	# lo ="abcdefghijklmnopqrstuvwxyz"
	# en =""

	for k in range((26)):
		trans = ""
		for s in msg:
			if s == " ":
				trans = trans + " "
			elif (s.islower()):
				
				trans += chr((ord(s) + shift - 97)%26+97)
					# n = lo.find(s)
					# n = n + shift
					# if n< 0:
					# 	n = n + len(letters)
					# 	trans = trans + lo[n]
					# elif n>len(letters):
					# 	n = n - len(letters)
					# 	trans = trans - lo[n]
					# else:
					# 	trans = trans + lo[n]
			else:
				
				trans += chr((ord(s) + shift - 65)%26+65)

					# n = letters.find(s)
					# n = n + shift
					# if n< 0:
					# 	n = n + len(letters)
					# 	trans = trans + letters[n]
					# elif n>len(letters):
					# 	n = n - len(letters)
					# 	trans = trans - letters[n]
					# else:
					# 	trans = trans + letters[n] 


	return trans




