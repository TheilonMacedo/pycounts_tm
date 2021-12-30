"""A package to count the number of words in a text.

Author: Theilon Macedo
Date: 30-12-2021

"""


from collections import Counter
from string import punctuation


def load_text(filepath):
    """Loads text from a file and returns it as a string.

    Args:
        filepath (str): The path to the file to be loaded.

    Returns:
        text (str): The text loaded from the file.
    """
    with open(filepath) as file:
        text = file.read()
    return text


def clean_text(text):
    """Format letters to lowercase and removes punctuation from a string.

    Args:
        text (str): The string to be cleaned.

    Returns:
        text (str): The cleaned string.
    """
    text = text.lower()
    for signal in punctuation:
        text = text.replace(signal, '')
    return text


def count_words(input_file):
    """Counts the number of words in a string.

    Args:
        input_file (str): The string to be counted.

    Returns:
        Word count (dict): A dictionary of words and their counts.
    """
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
