import re
from collections import Counter
from flask import Flask

app = Flask(__name__)

file_path = "text.txt"

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_word_counts

def validate_word_counts(word_counts, file_path):
    with open(file_path, 'r') as file:
        content = file.read().lower()
        words = re.findall(r'\b\w+\b', content)
        expected_word_counts = Counter(words)
        sorted_expected_word_counts = sorted(expected_word_counts.items(), key=lambda x: x[1], reverse=True)
        return word_counts == sorted_expected_word_counts

@app.route('/count')
def count_route():
    word_counts = count_words(file_path)
    sorted_output = "\n".join([f"{word}: {count}" for word, count in word_counts])
    validation_result = validate_word_counts(word_counts, file_path)
    if validation_result:
        validation_status = "Validation passed!"
    else:
        validation_status = "Validation failed!"
    return f"<pre>{sorted_output}\n{validation_status}</pre>"

if __name__ == "__main__":
    app.run()
