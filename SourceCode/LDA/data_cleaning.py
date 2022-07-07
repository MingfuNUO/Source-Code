# 导入算法包
import nltk
import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer       #词干化
from nltk.stem import WordNetLemmatizer   #词形还原
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag

#import files
data_all = pd.read_csv("").astype(str)
data=data_all['review']

#Keep English lowercase text only
def clear_character(sentence):
    sentence = re.sub(r"\s*[^A-Za-z]+\s*", " ", str.lower(sentence))
    return sentence
train_text = [clear_character(data_all) for data_all in data_all['review']]
data_all['review_clear'] = train_text

#word separation
a=[]
for i in train_text:
    train_seg_text = word_tokenize(i)
    a.append(train_seg_text)
data_all['review_seg'] = a

#remove stopwords
#stops = set(stopwords.words("english"))
stop_words_path = "SMART_stopwords.txt"
def get_stop_words():
    return set([item.strip() for item in open(stop_words_path,'r').readlines()])
stopwords = get_stop_words()
def drop_stopwords(line):
    line_clear = []
    for word in line:
        if word in stopwords:
            continue
        line_clear.append(word)
    return line_clear
train_st_text = [drop_stopwords(s) for s in a]
data_all['review_st'] = train_st_text

#keep JJ,JR,JJS,NN,NNS,NNP,NNPS,RB,RBR,RBS
cixing=[]
for i in train_st_text:
    a=nltk.pos_tag(i)
    cixing.append(a)

data3=[]
for i in cixing:
    data2 = []
    for word in i:
        if word[1]=='NN'or'JJ'or'JJR'or'JJS'or'NN'or'NNS'or'NNP'or'NNPS'or'RB'or'RBR'or'RBS':
            data2.append(word[0])
    data3.append(data2)
data_all['review_fin'] = data3

#stemming and lexical domestication
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

data4=[]
for i in data3:
    tagged_sent = pos_tag(i)
    data4.append(tagged_sent)
wnl = WordNetLemmatizer()

data5=[]
for i in data4:
    lemmas_sent = []
    for tag in i:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos)) # 词形还原
    data5.append(lemmas_sent)


data_all['review_final'] = data5

#Export results
data_all.to_csv('',encoding="utf-8")


