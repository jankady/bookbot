from stats import count_words

def get_book_text(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")



main()