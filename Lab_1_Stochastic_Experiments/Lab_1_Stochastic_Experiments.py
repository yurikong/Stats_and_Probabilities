import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# 1. Function for a n-sided die
def nSidedDie(p):
    N=10000
    s=np.zeros((N,1))
    n=len(p)
    cs=np.cumsum(p)
    cp=np.append(0,cs)
    for j in range(0,N):
        r=np.random.rand()
        for k in range(0,n):
            if r>cp[k] and r<=cp[k+1]:
                d=k+1
        s[j]=d
    # Plotting
    b=range(1,n+2)
    sb=len(b)
    h1, bin_edges=np.histogram(s,bins=b)
    b1=bin_edges[0:sb-1]
    plt.close('all')
    prob=h1/N
    plt.stem(b1,prob)
    # Graph labels
    plt.title('PMF for a '+str(n)+'-sided die')
    plt.xlabel('Number on the face of the die')
    plt.ylabel('Probability')
    plt.xticks(b1)
    plt.show()
nSidedDie([0.10, 0.15, 0.20, 0.05, 0.30, 0.10, 0.10])

# 2. Number of rolls needed to get a "7" with two dice
def rollOf7(N):
    S=np.zeros((N,1))
    for j in range(0,N):
        count=0
        s=0
        while s!=7:
            s=np.random.randint(1,7)+np.random.randint(1,7)
            count+=1
        S[j]=count
    # Plotting
    b=range(1,32)
    sb=len(b)
    h1, bin_edges=np.histogram(S,bins=b)
    b1=bin_edges[0:sb-1]
    plt.close('all')
    prob=h1/N
    plt.stem(b1,prob)
    # Graph labels
    plt.title('PMF for roll of 7 with 2 dice')
    plt.xlabel('Number of rolls it takes to succeed')
    plt.ylabel('Probability')
    plt.show()
rollOf7(100000)

# 3. Getting 50 heads when tossing 100 coins
def coinToss50Heads(N):
    success=0
    for i in range(0,N):
        coin=np.random.randint(0,2,100)
        if sum(coin)==50:
            success+=1
    print(success/N)
coinToss50Heads(100000)
    
# 4. The password hacking problem
def pwcrack(m,k,N):
    n=26**4
    success=0
    for i in range(0,N):
        pw=np.random.randint(0,n)
        plist=np.random.randint(0,n,m*k)
        if pw in plist:
            success+=1
    print(success/N)
pwcrack(80000,1,1000)
pwcrack(80000,7,1000)
pwcrack(320000,1,1000)
