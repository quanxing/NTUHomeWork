#coding:utf8

import numpy as np
import random
import pandas as pd

class PLA(object):
    def train_pla_random(self, data):
        X = data[['fea0','fea1','fea2','fea3','fea4']].values
        # # print X[0]
        y = data['label']
        max_iter = 2000
        ite = 1
        count = 0

        while ite <= max_iter:
            orders = range(data.shape[0])
            random.shuffle(orders)
            W = np.zeros((1,X.shape[1]))
            print 'ite', ite
            # print '---start count---',count

            while True:
                flag = 0
                for i in orders:
                    if np.dot(X[i,:], W[0]) * y[i] <=0 :
                        W[0] +=  0.5*y[i] * X[i]  #y[i] * X[i]
                        count += 1
                        flag = 1
                if flag == 0:
                    break
            ite += 1
            # print '---end count---',count
        print count/(1.* max_iter)
        # return count


    def train_pla(self, data):
            
        X = data[['fea0','fea1','fea2','fea3','fea4']].values
        y = data['label']
        count = 0
        W = np.zeros((1,X.shape[1]))

        while True:
            flag = 0
            for i in range(data.shape[0]):
                if np.dot(X[i,:], W[0]) * y[i] <=0 :
                    W[0] +=  y[i] * X[i]
                    count += 1
                    flag = 1
            if flag == 0:
                break
        print count
        # return count


if __name__ == '__main__':
    # init the class
    my_Percetron = PLA()
    # get the data by pandas 
    data = pd.read_csv('./train.dat',sep='\s+', names=['fea1','fea2','fea3','fea4','label'])
    # add x0 =1
    data['fea0'] = 1
    # get hea data
    print data.head()

    #train PLA
    my_Percetron.train_pla(data)

