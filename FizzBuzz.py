for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    elif (fizzbuzz % fizzbuzz) == 0 or (fizzbuzz % 1) == 0:
        print("prime")
        continue
    print(fizzbuzz)