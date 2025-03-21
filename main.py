#! /usr/bin/env python3
import sys
from stats import get_word_count, get_char_count, gen_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents
 

def main(*args):
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with status code 1
    else:
        filepath = sys.argv[1]  
        try:
            book_txt = get_book_text(filepath)
            char_dict = get_char_count(book_txt)
            report = gen_report(char_dict)
            print("============ BOOKBOT ============")
            print(f"Analyzing book found {filepath}...")
            print("----------- Word Count ----------")
            print(f"Found {get_word_count(book_txt)} total words")
            print("--------- Character Count -------")
            
            for char_dict in report:
                char = char_dict["char"]
                count = char_dict["count"]
                if char.isalpha():
                    print(f"{char}: {count}")
            
            print("============= END ===============")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
