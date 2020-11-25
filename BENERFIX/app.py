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

##########################################################Sorry im delete this part for personal reason. For additional questions email me at arisanita98@gmail.com
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



