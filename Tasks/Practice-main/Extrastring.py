def find_extra_char(s1, s2):
    result = 0
    for ch in s1 + s2:
        result ^= ord(ch)
    return chr(result)
