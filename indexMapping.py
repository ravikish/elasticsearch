
indexMapping = {
    "properties":{
        "Series_Title":{
            "type":"text"
        },
        "Genre":{
            "type":"text"
        },
        "Overview":{
            "type":"text"
        },
        "Director":{
            "type":"text"
        },
        "Star1":{
            "type":"text"
        },
        "Star2":{
            "type":"text"
        },
        "Star3":{
            "type":"text"
        },
        "Star4":{
            "type":"text"
        },
        "Concatenated_Text":{
            "type":"text"
        },
        "embed_data":{
            "type":"dense_vector",
            "dims": 768,
            "index":True,
            "similarity": "l2_norm"
        }

    }
}