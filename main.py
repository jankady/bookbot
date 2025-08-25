def get_book_text(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)


main()