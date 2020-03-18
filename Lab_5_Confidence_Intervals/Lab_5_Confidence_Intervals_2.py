import numpy as np
import random

N=1500000
mu=55
sig=5
B=np.random.normal(mu,sig,N)
M=10000
r1=[]
r2=[]
r3=[]
def normal_95(n):
    success=0
    for i in range(M):
        x=B[random.sample(range(N),n)]
        x_bar=np.mean(x)
        s_hat=np.std(x,ddof=1)
        if mu>=x_bar-1.96*s_hat/np.sqrt(n) and mu<=x_bar+1.96*s_hat/np.sqrt(n):
            success+=1
    return success/M
def normal_99(n):
    success=0
    for i in range(M):
        x=B[random.sample(range(N),n)]
        x_bar=np.mean(x)
        s_hat=np.std(x,ddof=1)
        if mu>=x_bar-2.58*s_hat/np.sqrt(n) and mu<=x_bar+2.58*s_hat/np.sqrt(n):
            success+=1
    return success/M
def studentT_95(n):
    if n==5:
        t=2.78
    if n==40:
        t=2.02
    if n==120:
        t=1.98
    success=0
    for i in range(M):
        x=B[random.sample(range(N),n)]
        x_bar=np.mean(x)
        s_hat=np.std(x,ddof=1)
        if mu>=x_bar-t*s_hat/np.sqrt(n) and mu<=x_bar+t*s_hat/np.sqrt(n):
            success+=1
    return success/M
def studentT_99(n):
    if n==5:
        t=4.60
    if n==40:
        t=2.71
    if n==120:
        t=2.62
    success=0
    for i in range(M):
        x=B[random.sample(range(N),n)]
        x_bar=np.mean(x)
        s_hat=np.std(x,ddof=1)
        if mu>=x_bar-t*s_hat/np.sqrt(n) and mu<=x_bar+t*s_hat/np.sqrt(n):
            success+=1
    return success/M
n=[5,40,120]
r=[r1,r2,r3]
for i in range(len(n)):
    r[i].append(normal_95(n[i]))
    r[i].append(normal_99(n[i]))
    r[i].append(studentT_95(n[i]))
    r[i].append(studentT_99(n[i]))
print(r1)
print(r2)
print(r3)
