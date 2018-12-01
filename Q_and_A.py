q_and_a = {"How are you?": "Good", 
		"What are you doing?": "I am programming", 
		"How's weather?": "Snowy"}

#def ask_user(q_and_a):
	#try:
		#while True:
			#question = input("Ask a question: ")
			#if question in q_and_a:
				#print(q_and_a[question])
			#elif question == "Bye":
				#break
			#else: 
				#print("Let's try again.")
	#except KeyboardInterrupt:
		#print("Sorry to see you go!")


def get_answer(question, q_and_a):
	return q_and_a.get(question)

def ask_user(answers):
    try:
        while True:
            user_question = input("Ask a question: ")
            answer = get_answer(user_question, q_and_a)
            print(answer)

            if user_question == "Bye":
                print("Sorry to see you go!")
                break
    except KeyboardInterrupt:
        print("Sorry to see you go!")

if __name__ == "__main__":
    ask_user(q_and_a)