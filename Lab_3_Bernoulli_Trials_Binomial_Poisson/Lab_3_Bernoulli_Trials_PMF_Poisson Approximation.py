# 1.
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
p=[0.2,0.1,0.15,0.3,0.2,0.05]
c=[1,2,3,4,5,6]
n=1000
N=10000
X=np.zeros((N,1))
for i in range(0,N):
    success=0
    s1=np.random.choice(c,n,p=p)
    s2=np.random.choice(c,n,p=p)
    s3=np.random.choice(c,n,p=p)
    for j in range(0,n):
        if s1[j]==1 and s2[j]==2 and s3[j]==3:
            success+=1
    X[i]=success
title='Bernoulli Trials: PMF - Experimental Results'
xlabel='Number of successes in n='+str(n)+' trials'
ylabel='Probability'
len_x=18
b=range(0,len_x+2)
sb=len(b)
h1, bin_edges=np.histogram(X,bins=b)
b1=bin_edges[0:sb-1]
plt.close('all')
prob=h1/len(X)
plt.stem(b1,prob)
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.xticks(b1)
plt.show()

# 2.
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
def nCk(n,k,p):
    q=1-p
    return (math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))*(p**k)*(q**(n-k))
p=0.003
n=1000
S=[]
for i in range(0,n+1):
    S.append(nCk(n,i,p))
len_x=18
b=range(0,len_x+1)
plt.close('all')
plt.stem(b,S[0:len_x+1])
title='Bernoulli Trials: PMF - Binomial Formula'
xlabel='Number of successes in n='+str(n)+' trials'
ylabel='Probability'
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.xticks(b)
plt.show()

# 3.
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
from decimal import Decimal
def poisson(l,k):
    return Decimal(Decimal(l)**Decimal(k))*Decimal(math.exp(Decimal(-l)))/Decimal(math.factorial(Decimal(k)))
n=1000
p=0.003
l=n*p
S=[]
for i in range(0,n):
    S.append(poisson(l,i))
len_x=18
b=range(0,len_x+1)
plt.close('all')
plt.stem(b,S[0:len_x+1])
title='Bernoulli Trials: PMF - Poisson Approximation'
xlabel='Number of successes in n='+str(n)+' trials'
ylabel='Probability'
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.xticks(b)
plt.show()
