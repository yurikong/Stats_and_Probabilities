import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

N=1500000
mu=55
sig=5
n=200
B=np.random.normal(mu,sig,N)
x_bar=np.zeros((n,1))
s_hat=np.zeros((n,1))
for i in range(n):
    x=B[random.sample(range(N),i+1)]
    x_bar[i]=np.mean(x)
    s_hat[i]=np.std(x,ddof=1)
def f1(mu,sig,n,flag):
    if flag==1:
        return mu+1.96*sig/np.sqrt(n)
    else:
        return mu-1.96*sig/np.sqrt(n)
def f2(mu,sig,n,flag):
    if flag==1:
        return mu+2.58*sig/np.sqrt(n)
    else:
        return mu-2.58*sig/np.sqrt(n)
fig1=plt.figure(1)
plt.close('all')
plt.scatter(range(n),x_bar,marker='x')
plt.plot(f1(mu,sig,range(n),1),'r--')
plt.plot(f1(mu,sig,range(n),0),'r--')
plt.title('Sample Means and 95% Confidence Intervals')
plt.xlabel('Sample Size')
plt.ylabel('x_bar')
plt.show()
fig2=plt.figure(2)
plt.close('all')
plt.scatter(range(n),x_bar,marker='x')
plt.plot(f2(mu,sig,range(n),1),'g--')
plt.plot(f2(mu,sig,range(n),0),'g--')
plt.title('Sample Means and 99% Confidence Intervals')
plt.xlabel('Sample Size')
plt.ylabel('x_bar')
plt.show()
