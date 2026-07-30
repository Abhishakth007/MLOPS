import math
def adder(*args):

    counter = 0
    for i in args:
        counter +=i

    return counter


def prime_checker(n):
   is_prime = False
   if n <0:
        is_prime = False
   elif n==1:
        is_prime = False

   else:
        for i in range(2,math.ceil(math.sqrt(n))):
            if n%i ==0:
                is_prime = False
                break
            else:
                is_prime = True

   return is_prime
    


if __name__ == "__main__":
    adder_result = adder(2,3,4,5)
    prime_checker_result = prime_checker(22)
    print(f"Adder Result : {adder_result}")
    print(f"Prime Checker : {prime_checker_result}")


