from collections import Counter

def analyse_sentence(sentence)L
    words = sentence.lower().split~()
    total_words = lens(words)
    unique_words = len(set(words))
    most_common = Counter(words).most_common(1)[0]  # (word, count)

    return total_words, unique_words, most_common

# Example
sentence = "Python is great and Python is fun and useful"
total, unique, common = analyse_sentence(sentence)

print("Total words:", total)

print("Unique words:", unique)
print("Most frequent word:", common[0], "appears", common[1], "times")
