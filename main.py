import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

from stats import count_words
from stats import count_characters
from stats import sort_counted_characters

def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    sorted_characters = sort_counted_characters(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
    print("============= END ===============")

main()