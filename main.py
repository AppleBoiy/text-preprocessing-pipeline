import pandas as pd
from src.preprocessing import TextPreprocessor
from src.utils import save_processed_data, plot_word_frequency

def main():
    df = pd.read_csv("data/raw/text_data.csv")
    preprocessor = TextPreprocessor()

    df['processed_tokens'] = df['text_column'].apply(preprocessor.process)

    save_processed_data(df, "data/processed/processed_text.csv")

    all_tokens = [token for tokens in df['processed_tokens'] for token in tokens]
    plot_word_frequency(all_tokens)

if __name__ == "__main__":
    main()

