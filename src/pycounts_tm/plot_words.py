"""
Function to create a bar plot of the number of most commons words in
a text.

"""
import matplotlib.pyplot as plt


def plot_word_counts(word_counts, num_words=10):
    """Creates a barplot of the word counts.

    Args:
        word_counts (dict): A dictionary of words and their counts.
        top_words (int): The number of most commo words to be plotted.
    """
    top_n_words = word_counts.most_common(num_words)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(num_words), count)
    plt.xticks(range(num_words), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    plt.show()
    return fig
