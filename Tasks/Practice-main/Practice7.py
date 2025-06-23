def has_duplicate_letters(sentence):
    for word in sentence.split():
        seen = set()
        for char in word:
            if char in seen:
                return True
            seen.add(char)
    return False
