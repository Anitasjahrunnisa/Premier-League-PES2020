import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import warnings
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import pickle
warnings.filterwarnings('ignore')
import string
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances
import math
from scipy.spatial import distance
from math import sqrt
from flask import Flask,render_template
import numpy as np
from flask import Flask, request, jsonify, render_template,Blueprint,url_for
#from flask_paginate import Pagination, get_page_parameter, get_page_args
import os
import pickle


data= pd.read_csv("barubuat.csv",sep=";", encoding="ISO-8859-1")
#data.head(10)
data2=data.drop(['league', 'region', 'nationality', 'condition','weight'], axis=1)
data2.index+=1
###mengubah huruf jd lowercase
data2["name"] = data2["name"].str.lower()
data2["team"] = data2["team"].str.lower()
data2["position"] = data2["position"].str.lower()
data2["playingstyle"] = data2["playingstyle"].str.lower()
#########nambah data
data2["positions"] = data2["position"]

######menjadikan label position jadi tipe kategori
data2["positions"]= data2.position.astype("category").cat.codes
data2['positions'] = data2['positions'].astype('category')

# label_encoder object knows how to understand word labels. 
label_encoder = preprocessing.LabelEncoder()
#Create a label (category) encoder object
le = preprocessing.LabelEncoder()
# Fit the encoder to the pandas column
le.fit(data2['positions'])

#1->0.5 ,0-1
#scaler = MinMaxScaler()

#kategori angka
data2['binage'] = pd.cut(x=data2['age'], bins=[15, 23, 35, 55], labels=['1','2','3'])
data2['binhei'] = pd.cut(x=data2['height'], bins=[160, 169, 179, 189, 210], labels=['1','2','3','4'])
bins = [100000, 11999999, 41999999, 81999999, 125999999, 170999999]#value
labels = [1,2,3,4,5]
data2['binval'] = pd.cut(data2['value'], bins,labels=labels)
bins2 = [100, 999999, 15999999, 35999999, 56999999, 90000000]
labels2 = [1,2,3,4,5]
data2['binsa'] = pd.cut(data2['salary'], bins2,labels=labels2)
bins3 = [60, 67, 75, 83, 91, 100]
labels3 = [1,2,3,4,5]
data2['binov'] = pd.cut(data2['overall'], bins3,labels=labels3)


data2[['binage','binhei','binval','binsa','binov']] = data2[['binage','binhei','binval','binsa','binov']].values.astype(float)
data2[['binage','binhei','binval','binsa','binov']] = data2[['binage','binhei','binval','binsa','binov']].fillna(0.0).astype(int)
#data2[['positions']].values.astype(float)
#data2[['binage','binhei','binval','binsa','binov']] = scaler.fit_transform(data2[['binage','binhei','binval','binsa','binov']].values)
######rumus euclidean distance
#data2[['positions']]=scaler.fit_transform(data2[['positions']])
#a3= data2['positions']
b3= data2['binhei']
c3= data2['binage']
d3= data2['binov']
e3= data2['binval']
f3= data2['binsa']
############################
#data2['dst3']= np.sqrt((a3 - b3 - c3 - d3 - e3 - f3)**2)
#data2=data.drop(['binage','binhei','binval','binsa','binov'], axis=1)
#print(data2)


###flask
app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index():  
    
    return render_template('index.html')


@app.route('/form', methods=['POST','GET'])
def form():  
    if request.method == 'POST':
        ar = request.form['ar'] #int di sini mengubah inputan menjadi int
        us = int(request.form['us'])
        hi = int(request.form['hi'])
        va = int(request.form['va'])
        sa = int(request.form['sa'])
        ov = int(request.form['ov'])

        data2['dst4']= np.sqrt( ((b3-hi)**2) + ((c3-us)**2) + ((d3-ov)**2) + ((e3-va)**2) + ((f3-sa)**2) )
        iki= data2.iloc[:,:9]
#iki
        iki['dst4']=data2['dst4']

        
        a=iki.loc[(iki['team']== ar )& (iki['age'] >= us)& (iki['height'] >= hi)& (iki['value'] >= va)& (iki['salary'] >= sa)& (iki['overall'] >= ov)]
#b=iki.loc[(iki['team']=='chelsea') & (iki['height'] >= 181)& (data2['age'] >= c)]
        a=a.sort_values(by='dst4', ascending=True)
        a.to_csv(r'a.csv', index = False)
        df1= pd.read_csv('a.csv') #membaca file .csv
        dd = list(df1.values) #mengubah file a.csv menjadi list supaya dpt d convert ke table
       
        return render_template('hasil.html', dd = dd)
    
    else:
        return render_template('form.html')

#print(a)

if __name__ == "__main__":
    app.run(debug=True)



