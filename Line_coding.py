"""
Delta electro code
Md Touhid Islam
Depertment of CSE, HSTU
https://www.facebook.com/Shourov40
"""


import matplotlib.pyplot as plt
import numpy as np

def nrz_L(data):
    data_nrz = []
    for i in data:
        x = None
        if i==1:
            x=1
        else:
            x=-1
        data_nrz.append(x)
    data_nrz.append(1)
    xs = np.repeat(range(len(data_nrz)), 2)
    ys = np.repeat(data_nrz,2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.grid()
    plt.xlabel(str(data))
    plt.plot(xs,ys)
    plt.ylim(-3,3)
    plt.xlim(0,9)
    plt.title("NRZ-L")
    plt.show()

def nrz_I(data):
    data_nrz_i = []
    temp = True
    for i in range(len(data)):
        x = None
        if data[i]==1 and temp==True:
            x=-1
            temp = False
        elif data[i]==1 and temp==False:
            x=1
            temp = True
        elif data[i]==0 and temp==False:
            x=-1
        elif data[i]==0 and temp==True:
            x=1
        data_nrz_i.append(x)

    if data_nrz_i[0]==0:
        data_nrz_i[0] = 1
    data_nrz_i.append(1)
    xs = np.repeat(range(len(data_nrz_i)), 2)
    ys = np.repeat(data_nrz_i,2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.grid()
    plt.title("NRZ-I")
    plt.xlabel(str(data))
    plt.plot(xs,ys)
    plt.ylim(-3,3)
    plt.xlim(0,9)
    plt.show()

def ami(data):
    data_ami = []
    temp = True
    for i in range(len(data)):
        if data[i] == 1 and temp == True:
            x = 1
            temp = False
        elif data[i] == 1 and temp == False:
            x = -1
            temp = True
        else:
            x = 0
        data_ami.append(x)

    data_ami.append(0)
    xs = np.repeat(range(len(data_ami)), 2)
    ys = np.repeat(data_ami, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.grid()
    plt.xlabel(str(data))
    plt.plot(xs, ys)
    plt.ylim(-3, 3)
    plt.xlim(0, 9)
    plt.title("AMI")
    plt.show()

def pst(data):
    data_pst = []
    temp = True
    for i in range(len(data)):
        if data[i] == 0 and temp == True:
            x = 1
            temp = False
        elif data[i] == 0 and temp == False:
            x = -1
            temp = True
        else:
            x = 0
        data_pst.append(x)

    data_pst.append(0)
    xs = np.repeat(range(len(data_pst)), 2)
    ys = np.repeat(data_pst, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.grid()
    plt.xlabel(str(data))
    plt.plot(xs, ys)
    plt.ylim(-3, 3)
    plt.xlim(0, 9)
    plt.title("Pseudoternary")
    plt.show()

#@@@@@@@@@@@@@@@@@@@@ function call @@@@@@@@@@@@@@@@@@@@@@@@@@@@@


dec = input("Enter decimal data: ")
dec = bin(int(dec))
bin_data = str(dec).replace('0b', '')
data = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(bin_data)):
    data[8 - len(bin_data) + i] = int(bin_data[i])
print("Data in binary format: ",data)
nrz_L(data)
nrz_I(data)
ami(data)
pst(data)

