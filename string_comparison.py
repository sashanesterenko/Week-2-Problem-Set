first_str = input()
second_str = input()

def comparison(first_str, second_str):
    if isinstance(first_str, str) == True and isinstance(second_str, str) == True:
        if first_str==second_str:
            return 1
        elif first_str != second_str and second_str == 'learn':
            return 3
        elif len(first_str) > len(second_str):
            return 2
        else:
            return 4
    else: 
        return 0

result = comparison(first_str, second_str)
print(result)