import sys

from collections import Counter

def find_duplicates(strings):
    """
    Identifies which strings are duplicaties by using the counter function
    from the collections module. And then iterates through a loop to determine which words have
    more than one count and adds them to a duplicates list.

    Args:
        strings (str): A string representing the text given in as a terminal argument

    Raises:
        ValueError: If the money string is in an incorrect format.
    """
    if not strings:
        print("ERROR: You must provide at least one string")
        return

    # Concatenate all strings into one and split them into words
    words = ' '.join(strings).split()

    # Convert all words to lowercase for case-insensitive comparison
    words_lower = [word.lower() for word in words]

    # Count the occurrences of each word
    word_counts = Counter(words_lower)

    # keeps track of words that have been printed
    wordssaid = []

    # keeps track of duplicates
    numduplicates = 0
    prints = 0

    # Output words with duplicates, maintaining the case of the first occurrence
    duplicates = set()
    for word, count in word_counts.items():
        if count > 1:
            numduplicates += 1
            duplicates.add(word)

    for word in words:
        if word.lower() in duplicates:
            # ensures that a word hasn't been printed already by making a list of words that have been 
            if not word in wordssaid:
                wordssaid.append(word)
                print(word)
                prints += 1
        # ensures the number of prints dont exceed the number of duplicates to avoid duplicate prints
        if prints == numduplicates :
            break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: You must provide at least one string")
    else:
        find_duplicates(sys.argv[1:])
