from stats import *

def get_book_text(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"

    book_text = get_book_text(path)

    books = sort_dict(count_characters(book_text))

    books.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for book in books:
        if book['char'].isalpha():
            print(f"{book['char']}: {book['num']}")
    print("============= END ===============")
main()