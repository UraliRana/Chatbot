import os 
import random
#data_dir ="data/custom"
import pandas as pd
import csv
import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn 
df=pd.read_csv("ch1.txt.csv")
data_src=[]
data_dest=[]
data_test_ques=[]
data_test_ans=[]
data_train_ques=[]
data_train_ans=[]
data_train_ans1=[]
data_train_ques1=[]
data_test_ques1=[]
data_test_ans1=[]
data_test_ques2=[]
data_test_ans2=[]
data_train_ques2=[]
data_train_ans2=[]
a=len(df['source'])

def load_data(string="",robot="",start="", end=""):
        for i in range(a):
            if df.loc[i].at['source']=='human':
                string=string+df.loc[i].at['text']
                if robot!="":
                    data_dest.append(start + robot + end)
                    robot=""
                #print(type(string))
            else:
                if string!="":
                    data_src.append(string)
                    string=""  
                if df.loc[i].at['source']=='robot':
                         robot=robot+df.loc[i].at['text']
        if robot!="":
            data_dest.append(start + robot + end)
            robot=""
        if string!="":
            data_src.append(string)
            string="" 
                 
                
        print(len(data_src))
        #print("human:",data_src)
        #print("robot:",data_dest)
        print(len(data_dest))

def input1(input1=True):
    return data_src
def output1(output1=True):
    return data_dest     


def word_syns(data_dest1,data_src3):
    
    for idx in range(len(data_dest1)):
        answer=data_dest1[idx]
        n_answer1=answer
        #sentences=[]
        words = word_tokenize(answer)
        taged_tokens=nltk.pos_tag(words)
        
        #print("Pos tag of word answer:",taged_tokens1)
        sentence=data_src3[idx]
        for word,tag in taged_tokens:
            #print(word)
            synonymList ={}
            syno=[]
            if word!='ssss' and word!='r' and word!='i'and word!='o'and word!='t' and word!='y'and word!='af' and word!='s' and word!='d'and word!='c'and word!='ti' and word!='u' and word!='da' and word!='te'and word!='si'and word!='la' and word!='le'and word!='el' and word!='al' and word!='se'and word!='e'and word!='n' and word!='se' and word!='es'and word!='d':
                if tag=='NN'or tag== 'VBN':
                    wordNetSynset = wn.synsets(word)                
                    if len(wordNetSynset) != 0:
                        #print("word:",word)
                        #print("Pos tag of word:",tag)
                        for synSet in wordNetSynset:
                            for synWords in synSet.lemma_names():
                                 if synWords not in syno:
                                    syno.append(synWords)
                            synonymList[word]=syno
                            #print("list of syno:",syno)
                            #print("list of syno:",synonymList)
                            ns='/'.join(syno)
                        #print(ns)
                        n_answer1=n_answer1.replace(word,ns)
                    #print("sentence:",sentence)
                    #print("augmented_sentence:",n_sentence)
                    for key in synonymList:
                        for i in range(len(synonymList[key])):
                            n_answer=answer
                            n_answer = n_answer.replace(word,synonymList[word][i])
                                #sentences.append(n_sentence)
                            if n_answer not in data_train_ans1:
                                
                                data_train_ans1.append(n_answer)

                                data_train_ques1.append(sentence)
                     
                    else:
                        if answer not in data_train_ans1:
                            
                            data_train_ans1.append(answer)
                        
                            data_train_ques1.append(sentence)
                        
                    
    #print(sentence)
    #print("lis of sentence:",data_train_ques2)
    #print("lis of sentence:",data_train_ans2)
    #print(n_sentence)
        #data_train_ques1.append(n_sentence)
    #print("new list:",data_train_ans1)
    print(len(data_train_ques1))
    print(len(data_train_ans1))
    return data_train_ques1,data_train_ans1

def word_syn1(data_train_ques1,data_train_ans1):
    
    for idx in range(len(data_train_ques1)):
            #print(idx)
            answer1=data_train_ans1[idx]
            question=data_train_ques1[idx]
            words1 = word_tokenize(question)
            taged_tokens=nltk.pos_tag(words1)
            for word,tag in taged_tokens:
                #print(word)
                synonymList1 ={}
                syno1=[]
                if word!='ssss'and word!='r' and word!='i'and word!='o'and word!='t' and word!='y'and word!='af' and word!='s' and word!='d'and word!='c'and word!='ti' and word!='u' and word!='da' and word!='te'and word!='si'and word!='la' and word!='le'and word!='el' and word!='al' and word!='se'and word!='e'and word!='n' and word!='se' and word!='es'and word!='d':
                    if tag=='NN'or tag== 'VBN':
                        wordNetSynset = wn.synsets(word)                
                        if len(wordNetSynset) != 0:
                            #print("word:",word)
                            #print("Pos tag of word:",tag)
                            for synSet in wordNetSynset:
                                for synWords in synSet.lemma_names():
                                     if synWords not in syno1:
                                        syno1.append(synWords)
                                synonymList1[word]=syno1 

                        #print("sentence:",syno1)
                        #print("augmented_sentence:",n_sentence)
                        for key in synonymList1:
                            for i in range(len(synonymList1[key])):
                                n_sentence=question
                                n_sentence=n_sentence.replace(word,synonymList1[word][i])
                                #if question in data_train_ques3:
                                data_train_ques2.append(n_sentence)
                                data_train_ans2.append(answer1)

                                #if question not in data_train_ques3:

                        else:
                                 if question not in data_train_ques2:
                                    data_train_ques2.append(question)
                                    data_train_ans2.append(answer1)


            #print(data_train_ques3)
    print(len(data_train_ques2))
    print(len(data_train_ans2))  
    return data_train_ques2,data_train_ans2

def prepare_seq2seq_files(data_train_ques2,data_train_ans2,TESTSET_SIZE =50000):
    

    # choose 30,000 (TESTSET_SIZE) items to put into testset
    test_ids = random.sample([i for i in range(len(data_train_ques2))],TESTSET_SIZE)
   
    for i in range(len(data_train_ques2)):
        if i in test_ids:
            data_test_ques.append(data_train_ques2[i]+'\n')
            data_test_ans.append(data_train_ans2[i]+ '\n' )
        else:
            data_train_ques.append(data_train_ques2[i]+'\n')
            data_train_ans.append(data_train_ans2[i]+ '\n' )
        #if i%100== 0:
         #   print ("written lines",i)

def train_encoder(input1=True):
    return data_train_ques

def train_decoder(output1=True):
    return data_train_ans  

def test_encoder(input1=True):
    return data_test_ques

def test_decoder(output1=True):
    return data_test_ans 
    



def word_syns2(data_dest3,data_src5):
    
    for idx in range(len(data_dest3)):
        answer2=data_dest3[idx]
        n_answer2=answer2
        #sentences=[]
        words3 = word_tokenize(answer2)
        taged_tokens3=nltk.pos_tag(words3)
        
        #print("Pos tag of word answer:",taged_tokens1)
        sentence2=data_src5[idx]
        for word,tag in taged_tokens3:
            #print(word)
            synonymList3 ={}
            syno3=[]
            if word!='ssss' and word!='r' and word!='i'and word!='o'and word!='t' and word!='y'and word!='af' and word!='s' and word!='d'and word!='c'and word!='ti' and word!='u' and word!='da' and word!='te'and word!='si'and word!='la' and word!='le'and word!='el' and word!='al' and word!='se'and word!='e'and word!='n' and word!='se' and word!='es'and word!='d':
                if tag=='NN'or tag== 'VBN':
                    wordNetSynset = wn.synsets(word)                
                    if len(wordNetSynset) != 0:
                        #print("word:",word)
                        #print("Pos tag of word:",tag)
                        for synSet in wordNetSynset:
                            for synWords in synSet.lemma_names():
                                 if synWords not in syno3:
                                    syno3.append(synWords)
                            synonymList3[word]=syno3 
                            #print("list of syno:",syno)
                            #print("list of syno:",synonymList)
                            ns3='/'.join(syno3)
                        #print(ns3)
                        n_answer2=n_answer2.replace(word,ns3)
                    #print("sentence:",sentence)
                    #print("augmented_sentence:",n_sentence)
                    for key in synonymList3:
                        for i in range(len(synonymList3[key])):
                            n_answer3=answer2
                            n_answer3 = n_answer3.replace(word,synonymList3[word][i])
                                #sentences.append(n_sentence)
                            if n_answer3 not in data_test_ans1:
                                
                                data_test_ans1.append(n_answer3)

                                data_test_ques1.append(sentence2)
                     
                    else:
                        if answer2 not in data_test_ans1:
                            
                            data_test_ans1.append(answer2)
                        
                            data_test_ques1.append(sentence2)
                        
                    
    #print(sentence)
    #print("lis of sentence:",data_train_ques2)
    #print("lis of sentence:",data_train_ans2)
    #print(n_sentence)
        #data_train_ques1.append(n_sentence)
    #print("new list:",data_train_ans1)
    print(len(data_test_ques1))
    print(len(data_test_ans1))
    return data_test_ques1,data_test_ans1

def word_syn3(data_test_ques1,data_test_ans1):

    for idx in range(len(data_test_ques1)):
            #print(idx)
            answer2=data_test_ans1[idx]
            question1=data_test_ques1[idx]
            words1 = word_tokenize(question1)
            taged_tokens1=nltk.pos_tag(words1)
            for word,tag in taged_tokens1:
                #print(word)
                synonymList5 ={}
                syno5=[]
                if word!='ssss'and word!='r' and word!='i'and word!='o'and word!='t' and word!='y'and word!='af' and word!='s' and word!='d'and word!='c'and word!='ti' and word!='u' and word!='da' and word!='te'and word!='si'and word!='la' and word!='le'and word!='el' and word!='al' and word!='se'and word!='e'and word!='n' and word!='se' and word!='es'and word!='d':
                    if tag=='NN'or tag== 'VBN':
                        wordNetSynset = wn.synsets(word)                
                        if len(wordNetSynset) != 0:
                            #print("word:",word)
                            #print("Pos tag of word:",tag)
                            for synSet in wordNetSynset:
                                for synWords in synSet.lemma_names():
                                     if synWords not in syno5:
                                        syno5.append(synWords)
                                synonymList5[word]=syno5 

                        #print("sentence:",syno5)
                        #print("augmented_sentence:",n_sentence)
                        for key in synonymList5:
                            for i in range(len(synonymList5[key])):
                                n_sentence1=question1
                                n_sentence1=n_sentence1.replace(word,synonymList5[word][i])
                                #if question in data_train_ques3:
                                data_test_ques2.append(n_sentence1)
                                data_test_ans2.append(answer2)



                                #if question not in data_train_ques3:

                        else:
                                 if question1 not in data_test_ques2:
                                    data_test_ques2.append(question1)
                                    data_test_ans2.append(answer2)


            #print(data_train_ques3)
    print(len(data_test_ques2))
    print(len(data_test_ans2))  
    return data_test_ques2,data_test_ans2
