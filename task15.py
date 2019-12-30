# Write the code, which will print numbers from 0 till your age. And if your age
# is odd, will be printed all odd numbers till your age, if even all even numbers.

age = int(input("Your age?: " ))
for x in range(1, age+1):
        if age % 2 == 0:
            if x % 2 == 0:
                print(x, end=' ')
        else:
            if x % 2 == 1:
                print(x, end=" ")
