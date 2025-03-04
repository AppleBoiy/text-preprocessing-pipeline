import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def save_processed_data(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)

def plot_word_frequency(tokens, top_n=20):
    word_counts = Counter(tokens)
    common_words = word_counts.most_common(top_n)
    words, counts = zip(*common_words)

    plt.bar(words, counts)
    plt.title("Top Words by Frequency")
    plt.xticks(rotation=45)
    plt.show()

