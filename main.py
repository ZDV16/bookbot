import sys
from stats import get_words, get_char, char_sorter

def get_book_text(dir):
    with open(dir) as f:
        file_contents = f.read()
        return file_contents

def main():
    # Check if we have the correct number of command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Use the second argument as the book path
    book_path = sys.argv[1]
    
    contents = get_book_text(book_path)
    num_words = get_words(contents)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    char_count = get_char(contents)
    sorted_chars = char_sorter(char_count)
    print("--------- Character Count -------")
    for c in sorted_chars:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['num']}")
    print("============= END ===============")

main()
