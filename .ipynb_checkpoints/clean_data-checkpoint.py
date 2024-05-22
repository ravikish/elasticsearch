

import pandas as pd
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def clean_data(data):

    cleaned_data = data.drop_duplicates()

    # Handle missing values
    cleaned_data = cleaned_data.dropna()

    return cleaned_data

def preprocess_text(data):
    # Lowercase all columns
    data = data.apply(lambda x: x.astype(str).str.lower())

    # Preprocess 'Overview' column
    def preprocess_overview(text):
        # Remove special characters, numbers, and HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\d+', '', text)

        tokens = word_tokenize(text)

        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]

        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

        # Join the tokens back into a single string
        preprocessed_text = ' '.join(stemmed_tokens)

        return preprocessed_text

    data['Overview'] = data['Overview'].apply(preprocess_overview)

    return data


def concatenate_columns(data):
    concatenated_text = data.apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    return concatenated_text


def main():
    data = pd.read_csv('imdb_top_1000.csv')

    selected_columns = ['Series_Title', 'Genre', 'Overview', 'Director', 'Star1', 'Star2',
                        'Star3', 'Star4']
    data = data[selected_columns]
    cleaned_data = clean_data(data)
    data = preprocess_text(cleaned_data)
    

    data['Concatenated_Text'] = concatenate_columns(data)

    # print(data['Concatenated_Text'])
    data.to_csv('cleaned_imdb_data_new.csv', index=True)
if __name__ == '__main__':
    main()

