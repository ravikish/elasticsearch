
import pandas as pd
from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
from indexMapping import indexMapping



def store_embeddings(data, username, password, url):
    es = Elasticsearch([url], http_auth=(username, password), verify_certs=False)
    es.indices.create(index="mymovies", mappings=indexMapping)
    record_list = data.to_dict("records")

    for record in record_list:
        try:
            es.index(index="mymovies", document=record)
        except Exception as e:
            print(e)
    print(es.count(index="mymovies"))
def main():
    # Load the preprocessed data
    data = pd.read_csv('cleaned_imdb_data_new.csv')

    # Embed the text
    # embeddings = embed_text(data['Concatenated_Text'])
    model = SentenceTransformer('all-mpnet-base-v2')
    data['embed_data'] = data["Concatenated_Text"].apply(lambda x: model.encode(x))
    username = 'elastic'
    password = '52iDVZd4y+g2H1J8Xi*l'
    url = 'https://localhost:9200'
    store_embeddings(data, username=username, password=password, url=url)
    print(data.head(1));

    

if __name__ == "__main__":
    main()
