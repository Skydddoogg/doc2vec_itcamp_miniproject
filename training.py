#Import all the dependencies
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from pythainlp.tokenize import word_tokenize
import pandas as pd
import nltk
nltk.download('punkt');

df = pd.read_csv('sky_thoth.csv')
data = df['Message'].as_matrix()

tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data) if type(_d) is str]

max_epochs = 100
vec_size = 20
alpha = 0.025

model = Doc2Vec(size=vec_size,
                alpha=alpha,
                min_alpha=0.025,
                min_count=1,
                dm=1)

model.build_vocab(tagged_data)

for epoch in range(max_epochs):
        print('iteration {0}'.format(epoch))
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.iter)
        # decrease the learning rate
        model.alpha -= 0.0002
        # fix the learning rate, no decay
        model.min_alpha = model.alpha

model.save("d2v.model")
print("Model Saved")