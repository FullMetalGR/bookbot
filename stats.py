def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    characters_count = {}
    for character in text:
        if character in characters_count:
            characters_count[character] += 1
        else:
            characters_count[character] = 1
    return characters_count

def sort_counted_characters(characters_count):
    sorted_characters = []
    for character, count in characters_count.items():
        sorted_characters.append({"char": character, "num": count})
    sorted_characters = sorted(sorted_characters, key=lambda x: x["num"], reverse=True)
    return sorted_characters