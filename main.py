def count_characters(text):
    characters_dict = {}

    for char in text:
        key = char.lower()
        if key not in characters_dict.keys():
            characters_dict[key] = 0
        characters_dict[key] += 1
    return characters_dict


def count_words(text):
    return len(text.split())


def print_report_header(book_file):
    return f'--- Begin report of {f.name} ---'


if __name__ == '__main__':
    with open('./books/frankenstein.txt') as f:
        print(print_report_header(f))
        file_contents = f.read()
        print(f'{count_words(file_contents)} words found in the document \n')
        char_count = count_characters(file_contents)
        for item in char_count.items():
            print(f"The '{item[0]}' character was found {item[1]} times")
    print('--- End report ---')
