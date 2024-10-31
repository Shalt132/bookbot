def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    # Count every character in lower case
    counted_characters = count_characters(text)
    print(text)
    print(f"{word_count} words were found in the document!")
    print(counted_characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_case_book = text.lower()
    characters = {}
    for c in (lower_case_book):
        if c.isalpha():
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1
    return characters

main()