i = 0
numbers = []

def whileloop(varlimit):
    global i
    while i < varlimit:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

def forloop():
    print("The numbers:")

    for num in numbers:
        print(num)
print("Enter loop limit: ")
varlim = int(input())
whileloop(varlim)
forloop()
