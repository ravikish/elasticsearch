
import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import requests
from PIL import Image
from io import BytesIO
indexName = "mymovies"

try:
    es = Elasticsearch(
        "https://localhost:9200",
        basic_auth=("elastic", "52iDVZd4y+g2H1J8Xi*l"),
        ca_certs="C:/Users/kethanaravi/PycharmProjects/pythonProject/http_ca.crt"
    )
except ConnectionError as e:
    print("Connection Error:", e)

if es.ping():
    print("Succesfully connected to ElasticSearch!!")
else:
    print("Oops!! Can not connect to Elasticsearch!")


def search(input_keyword):
    model = SentenceTransformer('all-mpnet-base-v2')
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
        "field": "embed_data",
        "query_vector": vector_of_input_keyword,
        "k": 4,
        "num_candidates": 1000,
    }


    res = es.knn_search(index="mymovies", knn=query, source=["Series_Title", "Overview", "Poster_Link"])
    results = res["hits"]["hits"]

    return results


def main():
    st.title("My movie search")

    # Input: User enters search query
    search_query = st.text_input("query")

    # Button: User triggers the search
    if st.button("Search"):
        if search_query:
            # Perform the search and get results
            results = search(search_query)

            # Display search results
            st.subheader("movie results")
            for result in results:
                with st.container():
                    if '_source' in result:
                        try:
                            st.header(f"{result['_source']['Series_Title']}")
                        except Exception as e:
                            print(e)

                        try:
                            st.write(f"Description: {result['_source']['Overview']}")
                        except Exception as e:
                            print(e)
                        try:
                            # Fetch and display poster image
                            poster_link = result['_source']['Poster_Link']
                            response = requests.get(poster_link)
                            if response.status_code == 200:
                                image = Image.open(BytesIO(response.content))
                                st.image(image, caption='Poster', use_column_width=True)
                            else:
                                st.write("Failed to fetch poster image")
                        except Exception as e:
                            print(e)
                        st.divider()


if __name__ == "__main__":
    main()
