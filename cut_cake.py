def cut_cake(parts):
    try:
        return 1 / int(parts)
    except (ZeroDivisionError, TypeError, ValueError):
        return "You mad?"

parts = "4, 5"
if __name__ == "__main__":
    result = cut_cake(parts) 
    print(result)