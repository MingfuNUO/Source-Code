import gensim
from gensim import corpora
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')  # To ignore all warnings that arise here to enhance clarity

from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel

data_all = pd.read_csv(".csv")
data=data_all['review_final']
data=[eval(a) for a in data.values]

dictionary = corpora.Dictionary(data)
corpus = [dictionary.doc2bow(text) for text in data]

def perplexity(num_topics):
    ldamodel = LdaModel(corpus, num_topics=num_topics, id2word = dictionary, passes=30)
    print(ldamodel.print_topics(num_topics=num_topics, num_words=15))
    print(ldamodel.log_perplexity(corpus))
    return ldamodel.log_perplexity(corpus)

def coherence(num_topics):
    ldamodel = LdaModel(corpus, num_topics=num_topics, id2word = dictionary, passes=30, random_state = 1)
    print(ldamodel.print_topics(num_topics=num_topics, num_words=15))
    ldacm = CoherenceModel(model=ldamodel, texts=data, dictionary=dictionary, coherence='c_v')
    print(ldacm.get_coherence())
    return ldacm.get_coherence()

x = range(1,30)
z = [perplexity(i) for i in x]
y = [coherence(i) for i in x]
plt.plot(x, z)
plt.xlabel('num topics')
plt.ylabel('perplexity score')
plt.rcParams['font.sans-serif']=['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False
plt.title('perplexity score under different number of topics (US User)')
plt.show()

x = range(1,30)
z = [perplexity(i) for i in x] 
y = [coherence(i) for i in x]
plt.plot(x, y)
plt.xlabel('num topics')
plt.ylabel('coherence score')
plt.rcParams['font.sans-serif']=['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False
plt.title('coherence score under different number of topics (Chinese User)')
plt.show()