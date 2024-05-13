import string
PATH_TO_BOOKS = "books/"

def count_words_from_content(content: str) -> int:
    """Counts the words in given content
    """
    word_count = len(content.split())
    return word_count

def count_characters_from_content(content: str) -> dict:
    """Counts the different characters seen in the content,
    returns a dict with each character as a key
    """
    content = content.lower()
    character_dict = {}
    for character in content:
        # Do not count non-ascii characters, like punctuation
        if not character.isalpha():
            continue
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict

def sort_on(dict):
    return dict["count"]

def sort_character_dict(character_count: dict) -> list:
    character_list = []
    for character, count in character_count.items():
        character_list.append({"character": character, "count": count})
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def print_content_composition_report(word_count: int, character_list: list):
    print(f"--- Begin report of {PATH_TO_BOOKS}frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    # Loop through all the characters seen in the content
    for character in character_list:
        print(f"The '{character["character"]}' character was found {character["count"]} times")
    print(f"--- End report ---")

if __name__ == "__main__":
    with open(PATH_TO_BOOKS + "frankenstein.txt") as f:
        book_content = f.read()
        word_count = count_words_from_content(book_content)
        character_count = count_characters_from_content(book_content)
        character_list = sort_character_dict(character_count)
        print_content_composition_report(word_count, character_list)
