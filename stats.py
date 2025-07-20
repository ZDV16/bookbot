def get_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def get_char(file_contents):
    character = {}
    chars = file_contents.lower()
    for char in chars:
        if char in character:
            character[char] = character[char] + 1
        else:
            character[char] = 1
    return character

def char_sorter(character):
    char_list = []
    for key in character:
        d = {"char": key, "num": character[key]}
        char_list.append(d)
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list
