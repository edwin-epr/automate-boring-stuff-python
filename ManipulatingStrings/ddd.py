from typing import List, Tuple

INPUT_PROMPT: str = 'Enter the English message to translate into Pig Latin: '
VOWELS: Tuple[str, ...] = ('a', 'e', 'i', 'o', 'u', 'y')
CONSONANT_SUFFIX: str = 'ay'
VOWEL_SUFFIX: str = 'yay'


def extract_non_letters(word: str, start: bool) -> Tuple[str, str]:
    """Extrae caracteres no alfabéticos del inicio o final de una palabra."""
    non_letters = ''
    while word and not word[0 if start else -1].isalpha():
        non_letters += word[0 if start else -1]
        word = word[1:] if start else word[:-1]
    return non_letters, word


def translate_to_pig_latin(word: str) -> str:
    """Traduce una palabra a Pig Latin."""
    prefix_consonants = ''
    while word and word[0] not in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    if prefix_consonants:
        return word + prefix_consonants + CONSONANT_SUFFIX
    else:
        return word + VOWEL_SUFFIX


def process_word(word: str) -> str:
    """Procesa una palabra para convertirla a Pig Latin."""
    prefix_non_letters, word = extract_non_letters(word, True)
    suffix_non_letters, word = extract_non_letters(word, False)

    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()
    word = translate_to_pig_latin(word)

    if was_upper:
        word = word.upper()
    elif was_title:
        word = word.title()

    return prefix_non_letters + word + suffix_non_letters


def main():
    """Función principal para la traducción a Pig Latin."""
    message = input(INPUT_PROMPT)
    pig_latin_words: List[str] = [process_word(word) for word in message.split()]
    print(' '.join(pig_latin_words))


if __name__ == "__main__":
    main()
