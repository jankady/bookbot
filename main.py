from stats import *
import sys

def get_book_text(filename):
    try:
        with open(filename) as f:
            return f.read()
    except:
        print("Could not open book text file")
        sys.exit(1)



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

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