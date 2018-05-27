from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
import pandas as pd
import argparse
import sys
import numpy as np

SIZE_OF_VECTOR = 20

def process_doc2vec(csv_file_path):

    # Load model
    model = Doc2Vec.load("d2v.model")

    # Prepare data
    df = pd.read(csv_file_path)
    data = df['Message'].as_matrix()
    vectors = [[] for i in range(SIZE_OF_VECTOR)]

    # Perform the vectors of the documents
    for doc_index in range(len(data)):
        doc = word_tokenize(data[doc_index].lower())
        vector = model.infer_vector(doc)
        for i in range(SIZE_OF_VECTOR):
            vectors[i].append(float(vector[i]))

    for i in range(SIZE_OF_VECTOR):
        df['vector' + str(i)] = vectors[i]

    df.to_csv("data.csv", sep='\t', encoding='utf-8')

process_doc2vec()