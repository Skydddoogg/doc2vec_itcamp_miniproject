import pandas as pd
import argparse
import sys
import numpy as np
import nltk
nltk.download('punkt')
from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
from urllib.parse import urljoin
from urllib.request import pathname2url

SIZE_OF_VECTOR = 20

def path2url(path):
    return urljoin('file:', pathname2url(path))

def process_doc2vec(csv_file_path):
    # Load model
    model = Doc2Vec.load("d2v.model")
    # Prepare data
    df = pd.read_csv(csv_file_path)
    data = df['Message'].as_matrix()
    vectors = [[] for i in range(SIZE_OF_VECTOR)]
    # Perform the vectors of the documents
    for doc_index in range(len(data)):
        if type(data[doc_index]) is str:
            doc = word_tokenize(str(data[doc_index].lower()))
        else:
            doc = word_tokenize(str(data[doc_index]))
        vector = model.infer_vector(doc)
        for i in range(SIZE_OF_VECTOR):
            vectors[i].append(float(vector[i]))
    for i in range(SIZE_OF_VECTOR):
        df['vector' + str(i)] = vectors[i]
    df.to_csv("extracted.csv", index=False)
