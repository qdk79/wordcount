import re
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()  # Read the file content and convert to lowercase
        words = re.findall(r'\b\w+\b', text)  # Tokenize words using regex
        word_counts = Counter(words)  # Count the occurrences of each word

    # Sort words by occurrences in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts

def validate_word_counts(word_counts, file_path):
    with open(file_path, 'r') as file:
        content = file.read().lower()
        words = re.findall(r'\b\w+\b', content)
        expected_word_counts = Counter(words)
        sorted_expected_word_counts = sorted(expected_word_counts.items(), key=lambda x: x[1], reverse=True)
        assert word_counts == sorted_expected_word_counts, "Validation failed!"
    print("Validation passed!")

    # main
if __name__ == "__main__":
    file_path = "text.txt"
    word_counts = count_words(file_path)
    for word, count in word_counts:
        print(f"{word}: {count}")
    validate_word_counts(word_counts, file_path)
