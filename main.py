print("Please answer every question with Yes or No.\n")
contact = input("Have you been in close contact with someone:\n")
if contact.lower() == "yes":
	test = input("Has the person tested positive for WuhanVirus?\n")
	if test.lower() == "yes":
		print("\nCategory: RED \nYou should immediately test yourself for WuhanVirus and stay home meanwhile!")
	elif test.lower() == "no":
		expose = input("He might be exposed?\n")
		if expose.lower() == "yes":
			sym = input("Is he/she experienced symptoms yet?\n")
			if sym.lower() == "yes":
				print("\nCategory: RED \nYou should immediately test yourself for WuhanVirus and stay home meanwhile!")
			elif sym.lower() == "no":
				print("\nCategory: Yellow \nSelf Monitor daily")
			else:
				print("Enter a valid input")
		elif expose.lower() == "no":
			exp = input("Is he exposed to someone else who might have been exposed?\n")
			if exp.lower() == "yes":
				print("\nCategory: Yellow \nSelf Monitor daily")
			elif exp.lower() == "no":
				print("\nCategory: Green \nPractice social distancing.")
			else:
				print("Enter a valid input\n")
elif contact.lower() == "no":
	print("\nCategory: Green \nPractice social distancing.")
else:
	print("Enter a valid input\n")
