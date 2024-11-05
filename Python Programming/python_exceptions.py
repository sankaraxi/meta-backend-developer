def divide(a,b):
    return a/b

try:
    print(divide(1,0))
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(e, "Something went wrong!")