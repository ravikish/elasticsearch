import kaggle
import pandas as pd
import zipfile
import os

# Authenticate with Kaggle API
kaggle.api.authenticate()

# Specify the dataset to download
dataset = "harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows"

try:
    # Download dataset files
    kaggle.api.dataset_download_files(dataset, path=".", unzip=True)

    # Extract downloaded files from zip archive
    with zipfile.ZipFile("imdb-dataset-of-top-1000-movies-and-tv-shows.zip", "r") as zip_ref:
        zip_ref.extractall(".")

    # Read CSV file into DataFrame
    movies = pd.read_csv("imdb_top_1000.csv")

    # Display columns and first 10 rows of DataFrame
    print("Columns:")
    print(movies.columns)
    print("\nFirst 10 rows:")
    print(movies[["Series_Title", "Overview"]].head(10))

except Exception as e:
    print("An error occurred:", e)
