# -*- coding: utf-8 -*-
import numpy as np

# 簡単な実装
# def AND(x1,x2):
#     w1,w2,theta=0.5,0.5,0.7
#     return x1 * w1 + w2 * x2 > theta

# def NAND(x1,x2):
#     w1,w2,theta=-0.5,-0.5,-0.7
#     return x1 * w1 + w2 * x2 > theta

# def OR(x1,x2):
#     w1,w2,theta=0.5,0.5,0.2
#     return x1 * w1 + w2 * x2 > theta

# バイアスの導入とnumpyによる実装
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    return np.sum(x * w) + b > 0

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    return np.sum(x * w) + b > 0

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    return np.sum(x * w) + b > 0

if __name__=="__main__":
    print("AND")
    print(AND(0,0))
    print(AND(0,1))
    print(AND(1,0))
    print(AND(1,1))

    print("NAND")
    print(NAND(0,0))
    print(NAND(0,1))
    print(NAND(1,0))
    print(NAND(1,1))

    print("OR")
    print(OR(0,0))
    print(OR(0,1))
    print(OR(1,0))
    print(OR(1,1))
