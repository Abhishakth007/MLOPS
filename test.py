def adder(*args):
    counter = 0
    for i in args:
        counter +=i

    return counter

if __name__== "__main__":
   result =  adder(2,3,4,6)
   print(result)
