#!/usr/bin/python
# -*- coding: UTF-8 -*-

import codecs
import pandas as pd
import numpy as np
import re

def data2pkl():
    datas = list()
    labels = list()
    linedata=list()
    linelabel=list()
    tags = set()

    input_data = codecs.open('./wordtagsplit.txt','r','utf-8')
    for line in input_data.readlines():
        line = line.split()
        linedata=[]
        linelabel=[]
        numNotO=0
        for word in line:
            word = word.split('/')
            linedata.append(word[0])
            linelabel.append(word[1])
            tags.add(word[1])
            if word[1]!='O':
                numNotO+=1
        if numNotO!=0:
            datas.append(linedata)
            labels.append(linelabel)

    input_data.close()
    print len(datas),tags
    print len(labels)
    from compiler.ast import flatten
    all_words = flatten(datas)
    sr_allwords = pd.Series(all_words)
    sr_allwords = sr_allwords.value_counts()
    set_words = sr_allwords.index
    set_ids = range(1, len(set_words)+1)


    tags = [i for i in tags]
    tag_ids = range(len(tags))
    word2id = pd.Series(set_ids, index=set_words)
    id2word = pd.Series(set_words, index=set_ids)
    tag2id = pd.Series(tag_ids, index=tags)
    id2tag = pd.Series(tags, index=tag_ids)

    word2id["unknow"] = len(word2id)+1
    print word2id
    max_len = 60
    def X_padding(words):
        ids = list(word2id[words])
        if len(ids) >= max_len:  
            return ids[:max_len]
        ids.extend([0]*(max_len-len(ids))) 
        return ids

    def y_padding(tags):
        ids = list(tag2id[tags])
        if len(ids) >= max_len: 
            return ids[:max_len]
        ids.extend([0]*(max_len-len(ids))) 
        return ids
    df_data = pd.DataFrame({'words': datas, 'tags': labels}, index=range(len(datas)))
    df_data['x'] = df_data['words'].apply(X_padding)
    df_data['y'] = df_data['tags'].apply(y_padding)
    x = np.asarray(list(df_data['x'].values))
    y = np.asarray(list(df_data['y'].values))

    from sklearn.model_selection import train_test_split
    x_train,x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=43)
    x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train,  test_size=0.2, random_state=43)

    
    import pickle
    import os
    with open('../Bosondata.pkl', 'wb') as outp:
	    pickle.dump(word2id, outp)
	    pickle.dump(id2word, outp)
	    pickle.dump(tag2id, outp)
	    pickle.dump(id2tag, outp)
	    pickle.dump(x_train, outp)
	    pickle.dump(y_train, outp)
	    pickle.dump(x_test, outp)
	    pickle.dump(y_test, outp)
	    pickle.dump(x_valid, outp)
	    pickle.dump(y_valid, outp)
    print '** Finished saving the data.'
    
    
    
def origin2tag():
    input_data = codecs.open('./origindata.txt','r','utf-8')
    output_data = codecs.open('./wordtag.txt','w','utf-8')
    for line in input_data.readlines():
        line=line.strip()
        i=0
        while i <len(line):
	        if line[i] == '{':
		        i+=2
		        temp=""
		        while line[i]!='}':
			        temp+=line[i]
			        i+=1
		        i+=2
		        word=temp.split(':')
		        sen = word[1]
		        output_data.write(sen[0]+"/B_"+word[0]+" ")
		        for j in sen[1:len(sen)-1]:
			        output_data.write(j+"/M_"+word[0]+" ")
		        output_data.write(sen[-1]+"/E_"+word[0]+" ")
	        else:
		        output_data.write(line[i]+"/O ")
		        i+=1
        output_data.write('\n')
    input_data.close()
    output_data.close()


def tagsplit():
    with open('./wordtag.txt','rb') as inp:
	    texts = inp.read().decode('utf-8')
    sentences = re.split('[，。！？、‘’“”（）]/[O]'.decode('utf-8'), texts)
    output_data = codecs.open('./wordtagsplit.txt','w','utf-8')
    for sentence in sentences:
	    if sentence != " ":
		    output_data.write(sentence.strip()+'\n')
    output_data.close()


origin2tag()
tagsplit()
data2pkl()
