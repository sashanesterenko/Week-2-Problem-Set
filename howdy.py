def ask_user():
	while True:
		answer = input("How are you? ")
		if answer == "Good":
			print("Great!")
			break
ask_user()