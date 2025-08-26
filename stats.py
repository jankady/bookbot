
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

def sort_on(dictionary: dict):
    return dictionary["num"]

def sort_dict(dictionary: dict):
    result = []

    for value in dictionary:
        new_dict = {
            "char": value,
            "num": dictionary[value]
        }
        result.append(new_dict)

    return result