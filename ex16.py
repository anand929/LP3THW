from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# target = open(filename,"w")

print("Truncating the file. Goodbye!")
# target.truncate()
#instead of line 12 and 15, line 17 can be used for truncation
open(filename,"w").close()
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target = open(filename,"w")
target.write("{}\n{}\n{}\n".format(line1,line2,line3))

print("And finally, we close it.")
target.close()
