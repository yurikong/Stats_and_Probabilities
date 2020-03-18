# 1. Probability of erroneous transmission
import numpy as np
def nSidedDie(p,N):
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
    return s
p0=0.6
e0=0.05
e1=0.03
N=100000
failure=0
S=nSidedDie([p0,1-p0],N)-1
R=np.zeros((N,1))
for i in range(0,N):
    if S[i]==0: R[i]=nSidedDie([1-e0,e0],1)-1
    if S[i]==1: R[i]=nSidedDie([e1,1-e1],1)-1
    if R[i]!=S[i]:
        failure+=1
print(failure/N)
# 2. Conditional probability: P(R=1|S=1)
import numpy as np
def nSidedDie(p,N):
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
    return s
p0=0.6
e0=0.05
e1=0.03
N=100000
success=0
S=nSidedDie([p0,1-p0],N)-1
R=np.zeros((N,1))
for i in range(0,N):
    if S[i]==0:
        R[i]=nSidedDie([1-e0,e0],1)-1
    if S[i]==1:
        R[i]=nSidedDie([e1,1-e1],1)-1
        if R[i]==1:
            success+=1
print(success/np.sum(S))
# 3. Conditional probability: P(S=1|R=1)
import numpy as np
def nSidedDie(p,N):
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
    return s
p0=0.6
e0=0.05
e1=0.03
N=100000
success=0
S=nSidedDie([p0,1-p0],N)-1
R=np.zeros((N,1))
for i in range(0,N):
    if S[i]==0: R[i]=nSidedDie([1-e0,e0],1)-1
    if S[i]==1: R[i]=nSidedDie([e1,1-e1],1)-1
    if R[i]==1:
        if S[i]==1:
            success+=1
print(success/np.sum(R))
# 4. Enhanced transmission method
import numpy as np
def nSidedDie(p,N):
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
    return s
p0=0.6
e0=0.05
e1=0.03
N=100000
failure=0
S=nSidedDie([p0,1-p0],N)-1
R1=np.zeros((N,1))
R2=np.zeros((N,1))
R3=np.zeros((N,1))
D=np.zeros((N,1))
for i in range(0,N):
    if S[i]==0:
        R1[i]=nSidedDie([1-e0,e0],1)-1
        R2[i]=nSidedDie([1-e0,e0],1)-1
        R3[i]=nSidedDie([1-e0,e0],1)-1
    if S[i]==1:
        R1[i]=nSidedDie([e1,1-e1],1)-1
        R2[i]=nSidedDie([e1,1-e1],1)-1
        R3[i]=nSidedDie([e1,1-e1],1)-1
    if R1[i]+R2[i]+R3[i]<2:
        D[i]=0
    else:
        D[i]=1
    if D[i]!=S[i]:
        failure+=1
print(failure/N)
    
