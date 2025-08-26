import collections


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    result = {}
    for word in text:

        char = word.lower()

        if char in result:
            result[char] = result[char] + 1
        else:
            result[char] = 1
    return result

