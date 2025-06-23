def find_extra_char(s1, s2):
    for ch in s2:
        if s2.count(ch) != s1.count(ch):
            return ch
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(find_extra_char(s1, s2))
