def is_shadow_sentence(s1, s2):
    words1 = s1.split()
    words2 = s2.split()

    if len(words1) != len(words2):
        return False

    for w1, w2 in zip(words1, words2):
        if len(w1) != len(w2):
            return False
        for ch in w1:
            if ch in w2:
                return False

    return True

s1 = input()
s2 = input()
print(is_shadow_sentence(s1, s2))
