from functions import Calculator

def sum(*args):
    val = 0
    for i in args:
        val = val + int(i)
    print(val)

sum(44,22,55,22)
        