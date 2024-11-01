def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    # Count every character in lower case
    counted_characters = count_characters(text)
    sorted_list = convert_dict_to_list(counted_characters)
    print(text)
    print(f"{word_count} words were found in the document!")
    print(counted_characters)
    # Sortiert die Liste (mit dictonaries) nach reihenfolge der häufigkeit
    sorted_list.sort(reverse=True, key="count")
    print(sorted_list)


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

def convert_dict_to_list(dict):
    new_list = []
    for char, count in dict.items():
        new_list.append({"char":char,"count":count})
    return new_list

def sort_on(dict):
    return dict["count"]

main()