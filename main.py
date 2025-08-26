from stats import count_words, count_characters

def get_book_text(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    char_num = count_characters(book_text)
    print(char_num)


main()