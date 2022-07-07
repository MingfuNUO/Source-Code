from gensim.models import LdaModel
import pandas as pd
import gensim.corpora as corpora
import csv
import pyLDAvis
import gensim
import pyLDAvis.gensim_models

data_all = pd.read_csv(".csv")
data=data_all['']
data=[eval(a) for a in data.values]

id2word = corpora.Dictionary(data)
corpus = [id2word.doc2bow(text) for text in data]

lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=14, passes=20, random_state=1, eta=0.035, alpha='asymmetric')
topic_list = lda.print_topics()

print(lda.alpha)
print(lda.eta)
print(topic_list)
d = pyLDAvis.gensim_models.prepare(lda,corpus,id2word)
pyLDAvis.show(d,local=False)