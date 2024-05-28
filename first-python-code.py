"Fizz Buzz challenge"
a = 5
b = 3
for i in range(100):
    if i%a == 0 and i&b == 0:
        print("FizzBuzz")
        continue
    if i%a == 0:
        print("Fizz") 
        continue
    if i%b == 0:
        print("Buzz") 
        continue
    print(i)