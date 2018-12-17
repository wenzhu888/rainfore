#-*- coding:utf-8 -*-
#author:wenzhu

import scipy.io
import matplotlib.pyplot as plt
import pandas as pd


def save_data(file_dir,filename,data):
    #scipy.io.savemat(file_dir + filename + '.mat', {filename: data})
    save = pd.DataFrame(data, columns=[filename])
    save.to_csv(file_dir + filename + '.csv',index=False)

def load_data():
    pass

def plot_fig(data1,data2,label1,label2):
    plt.plot(data1,label=label1)
    plt.plot(data2,label=label2)
    plt.legend()
    plt.show()


#计算MSE/R^2
def score(real_y, pred_y):
    pass
 


if __name__ == "__main__":
    pass
