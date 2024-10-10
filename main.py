def main():
    book_path = 'books/frankenstein.txt'
    print(f" --- Begin report of {book_path} --- ")
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_char = char_count(text)
    ordered_char_list = order_char_count(num_char)
    print (f"{num_words} words found in the document.")
    for dict in ordered_char_list:
        print(f"The '{dict['char']}' character was found {dict['num']} times")
    print(' --- End report --- ')
    
    
    
    
def get_book_text(path):    
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    text_lower = text.lower()
    text_lower_unique = set(text_lower)
    char_dict = {char: text_lower.count(char) for char in text_lower_unique if char.isalpha()}
    return char_dict

def sort_on(dict):
    return dict['num']

def order_char_count(dict):
    char_list = [{'char' : key, 'num' : value} for key, value in dict.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()

