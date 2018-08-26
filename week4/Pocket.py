#coding:utf8
# 增加一行注释

import numpy as np
import random
import pandas as pd

class Pocket(object):

    def test_pocket(self,train, data):
        X = data[['fea0','fea1','fea2','fea3','fea4']].values
        y = data['label']
        max_iter = 2000
        ite = 1
        err = 0
        while ite <= max_iter:
            count = 0
            W = self.train_pocket(train)
            for i in range(data.shape[0]):
                if np.dot(X[i,:], W[0]) * y[i] <=0 :
                    W[0] +=  y[i] * X[i]  #y[i] * X[i]
                    count += 1
            # print  'err',count / (1.* data.shape[0])        
            err += count / (1.* data.shape[0]) 
            # print err
            ite += 1
        print err/(1.* max_iter)


    def train_pocket(self, data):
            
        X = data[['fea0','fea1','fea2','fea3','fea4']].values
        y = data['label']
        count = 0
        W = np.zeros((1,X.shape[1]))
        orders = range(data.shape[0])
        random.shuffle(orders)
        bestW = np.zeros((1,X.shape[1]))
        maxCount = X.shape[0]
        while True:
            for i in orders:
                if np.dot(X[i,:], W[0]) * y[i] <=0 :
                    W[0] +=  y[i] * X[i]
                    count += 1
                    num = 0
                    for i in range(data.shape[0]):
                        if np.dot(X[i,:], W[0]) * y[i] <=0 :
                            num += 1
                    if num < maxCount:
                        maxCount = num
                        bestW = W
                           
                    if count == 50:
                        break
            if count == 50:
                break
        return bestW



if __name__ == '__main__':
    # init the class
    my_Percetron = Pocket()
    # get the data by pandas 
    data = pd.read_csv('./pocket_train.txt',sep='\s+', names=['fea1','fea2','fea3','fea4','label'])
    testData = pd.read_csv('./pocket_test.txt',sep='\s+', names=['fea1','fea2','fea3','fea4','label'])
    # add x0 =1
    data['fea0'] = 1
    testData['fea0'] = 1
    # get hea data
    print data.head()
     
    #test
    my_Percetron.test_pocket(data, testData)

