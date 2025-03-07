import argparse
import pandas as pd
from src.preprocessing import TextPreprocessor
from src.utils import save_processed_data, plot_word_frequency

def main(input_file, output_file):
    df = pd.read_csv(input_file)
    preprocessor = TextPreprocessor()

    df['processed_tokens'] = df['text_column'].apply(preprocessor.process)

    save_processed_data(df, output_file)

    all_tokens = [token for tokens in df['processed_tokens'] for token in tokens]
    plot_word_frequency(all_tokens)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process text data.")
    parser.add_argument('input_file', type=str, help="Path to the input CSV file.")
    parser.add_argument('output_file', type=str, help="Path to save the processed CSV file.")
    
    args = parser.parse_args()
    
    main(args.input_file, args.output_file)

