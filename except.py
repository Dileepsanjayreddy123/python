a=10
b=10
try:
    print(a/b)
    raise Exception(a/b)
    print("ok")
except Exception as e:
    print("you can't divide by zero",e)
finally:
    print("bye")
