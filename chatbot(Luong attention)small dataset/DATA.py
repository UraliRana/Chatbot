import os 
import random
#data_dir ="data/custom"
import pandas as pd
import csv
df=pd.read_csv("data/custom/train/ch1.txt.csv")
data_src=[]
data_dest=[]
data_test_ques=[]
data_test_ans=[]
data_train_ques=[]
data_train_ans=[]
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

def prepare_seq2seq_files(data_src3,data_dest1,TESTSET_SIZE =20):
    

    # choose 30,000 (TESTSET_SIZE) items to put into testset
    test_ids = random.sample([i for i in range(len(data_src3))],TESTSET_SIZE)
   
    for i in range(len(data_src3)):
        if i in test_ids:
            data_test_ques.append(data_src3[i]+'\n')
            data_test_ans.append(data_dest1[i]+ '\n' )
        else:
            data_train_ques.append(data_src3[i]+'\n')
            data_train_ans.append(data_dest1[i]+ '\n' )
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


