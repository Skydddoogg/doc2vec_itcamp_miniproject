from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
import pandas as pd
import argparse
import sys
import numpy as np

SIZE_OF_VECTOR = 20

def process_doc2vec(csv_file):

    # Load model
    model = Doc2Vec.load("d2v.model")

    # Prepare data
    df = pd.read_csv(csv_file).head(5)
    data = df['Message'].head(5).as_matrix()
    vectors = [[] for i in range(SIZE_OF_VECTOR)]

    # Perform the vectors of the documents
    for doc_index in range(len(data)):
        doc = word_tokenize(data[doc_index].lower())
        vector = model.infer_vector(doc)
        for i in range(SIZE_OF_VECTOR):
            vectors[i].append(float(vector[i]))

    for i in range(SIZE_OF_VECTOR):
        df['vector' + str(i)] = vectors[i]

    return df

def main():

    args = (sys.argv)[1]
    print(args)

    dataframe = process_doc2vec(args)

    dataframe.to_csv("data.csv", sep='\t', encoding='utf-8')

main()