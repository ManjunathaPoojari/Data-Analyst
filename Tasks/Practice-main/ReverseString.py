s = input()
reversed_string = ""
i = 0
while s[i:]:
    i = i + 1
i = i - 1
while i >= 0:
    reversed_string = reversed_string + s[i]
    i = i - 1
print(reversed_string)
