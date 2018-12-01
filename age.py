age = int(input())

def occupation (age):
    if age < 7:
        return "You're probably still at kindergarten."
    elif 7 <= age <= 17:
        return "You probably go to school."
    elif 17 < age <= 21:
        return "Prolly you're a student."
    elif age > 22:
        return "You work."

answer = occupation(age)
print(answer)
