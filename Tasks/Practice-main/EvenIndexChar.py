#"""Please write a program which accepts a string from console and print the characters that have even indexes.
#Example: If the following string is given as input to the program:
s = ""
c = ''
print("Enter a string (end with !):")
while True:
    c = input()
    if c == "!":
        break
    s = s + c
count = 0
for ch in s:
    count = count + 1
i = 0
while i < count:
    print(s[i], end="")
    i = i + 2
