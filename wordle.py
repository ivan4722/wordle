import pandas as pd
import matplotlib.pyplot as plt

# Load data
wordle_data = pd.read_csv('wordle.csv', header=None, names=['Word'])

# Function to count letter frequency in all words
def count_letter_frequency_all(words):
    print(len(words))
    frequency_dict = {}
    for word in words:
        for letter in word:
            letter = letter.upper()  # Convert to uppercase for case-insensitivity
            frequency_dict[letter] = frequency_dict.get(letter, 0) + 1
    return frequency_dict

# Count letter frequency in all words
letter_frequency_all = count_letter_frequency_all(wordle_data['Word'])

# Plot the overall letter frequencies
plt.bar(letter_frequency_all.keys(), letter_frequency_all.values())
plt.xlabel('Letter')
plt.ylabel('Frequency')
plt.title('Overall Letter Frequencies in Wordle Words')
plt.show()
