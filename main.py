from stats import (
     booktext,
     num_words,
     characters,
     sorting1,
)
import sys
def main():
    if len(sys.argv) == 1:
       print('Usage: python3 main.py <path_to_book>')
       sys.exit(1)
    book_path = sys.argv[1]
    text = booktext(book_path)
    get_num = num_words(text)
    text3 = characters(text)
    text4 = sorting1(text3)
    print_report(book_path, get_num, text4)

def print_report(book_path, get_num, text4):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num} total words")
    print("--------- Character Count -------")
    for i in text4:
        op = i["char"]
        if op.isalpha():
           print(f"{op}: {i['num']}")
    print("============= END ===============")

main()
