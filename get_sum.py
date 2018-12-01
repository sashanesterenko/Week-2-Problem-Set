

def get_sum(num_one, num_two):
    try:
        sum = int(num_one) + int(num_two)
        print(sum)
    except ValueError:
        return print("Type a number, will you?")

get_sum("fsdf", 5)