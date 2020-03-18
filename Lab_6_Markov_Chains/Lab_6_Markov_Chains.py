import numpy as np
import matplotlib
import matplotlib.pyplot as plt

##### Problem 1 --- A three-state Markov Chain
states=[1,2,3]
y=['Rain','Nice','Snow']
v=[1/4,0,3/4]
p1=[1/2,1/4,1/4]
p2=[1/4,1/8,5/8]
p3=[1/3,2/3,0]
n=15
N=10000
##### simulation
S=np.zeros(n)
P1=np.zeros(n)
P2=np.zeros(n)
P3=np.zeros(n)
for k in range(N):
    start=np.random.choice(states,1,p=v)
    S[0]=start
    if start==1: P1[0]+=1
    if start==2: P2[0]+=1
    if start==3: P3[0]+=1
    for i in range(1,n):
        if S[i-1]==1: S[i]=np.random.choice(states,1,p=p1)
        if S[i-1]==2: S[i]=np.random.choice(states,1,p=p2)
        if S[i-1]==3: S[i]=np.random.choice(states,1,p=p3)
        if S[i]==1: P1[i]+=1
        if S[i]==2: P2[i]+=1
        if S[i]==3: P3[i]+=1
plt.close('all')
plt.plot(S,':',marker='.',markersize=14,markerfacecolor='r')
plt.yticks(states,y)
plt.xticks(range(n))
plt.title('A sample simulation run of a three-state Markov Chain')
plt.ylabel('State')
plt.xlabel('Step number')
plt.show()
plt.close('all')
plt.plot(P1/N,':',marker='.',markersize=14,label='Rain')
plt.plot(P2/N,':',marker='.',markersize=14,label='Nice')
plt.plot(P3/N,':',marker='.',markersize=14,label='Snow')
plt.legend()
plt.xticks(range(n))
plt.title('Simulated three-state Markov Chain')
plt.xlabel('Step number')
plt.ylabel('Probability')
plt.show()
##### calculation
M=[p1,p2,p3]
S=np.zeros((15,3))
u=v
S[0]=u
for i in range(1,n):
    u=np.dot(u,M)
    S[i]=u
plt.close('all')
plt.plot(S[:,0],':',marker='.',markersize=14,label='Rain')
plt.plot(S[:,1],':',marker='.',markersize=14,label='Nice')
plt.plot(S[:,2],':',marker='.',markersize=14,label='Snow')
plt.xticks(range(n))
plt.xlabel('Step number')
plt.ylabel('Probability')
plt.title('Calculated three-state Markov Chain')
plt.legend()
plt.show()
####### Problem 2 --- The Google PageRank Algorithm
n=20
pages=['A','B','C','D','E']
###[[  0,   1,   0,   0,   0],
### [1/2,   0, 1/2,   0,   0],
### [1/3, 1/3,   0,   0, 1/3],
### [  1,   0,   0,   0,   0],
### [  0, 1/3, 1/3, 1/3,   0]]
P=[[  0,   1,   0,   0,   0],
   [1/2,   0, 1/2,   0,   0],
   [1/3, 1/3,   0,   0, 1/3],
   [  1,   0,   0,   0,   0],
   [  0, 1/3, 1/3, 1/3,   0]]
##### fair start
v=np.ones(5)/5
S=np.zeros((n,5))
S[0]=v
for i in range(1,n):
    v=np.dot(v,P)
    S[i]=v
R=list((zip(S[-1],range(5))))
R.sort(reverse=True)
r=[pair[1] for pair in R]
result=[pages[i] for i in r]
for i in range(5):
    print(result[i],':',R[i][0])
print()
plt.close('all')
plt.plot(S[:,0],':',marker='.',markersize=14,label='A')
plt.plot(S[:,1],':',marker='.',markersize=14,label='B')
plt.plot(S[:,2],':',marker='.',markersize=14,label='C')
plt.plot(S[:,3],':',marker='.',markersize=14,label='D')
plt.plot(S[:,4],':',marker='.',markersize=14,label='E')
plt.title('Calculated five-page webpage rank starting from any webpage fairly')
plt.ylabel('Probability')
plt.xlabel('Step number')
plt.xticks(range(n))
plt.legend()
plt.show()
##### start at E
v=[0,0,0,0,1]
S=np.zeros((n,5))
S[0]=v
for i in range(1,n):
    v=np.dot(v,P)
    S[i]=v
R=list((zip(S[-1],range(5))))
R.sort(reverse=True)
r=[pair[1] for pair in R]
result=[pages[i] for i in r]
for i in range(5):
    print(result[i],':',R[i][0])
print()
plt.close('all')
plt.plot(S[:,0],':',marker='.',markersize=14,label='A')
plt.plot(S[:,1],':',marker='.',markersize=14,label='B')
plt.plot(S[:,2],':',marker='.',markersize=14,label='C')
plt.plot(S[:,3],':',marker='.',markersize=14,label='D')
plt.plot(S[:,4],':',marker='.',markersize=14,label='E')
plt.title('Calculated five-page webpage rank starting from user\'s own webpage')
plt.ylabel('Probability')
plt.xlabel('Step number')
plt.xticks(range(n))
plt.legend()
plt.show()
##### Problem 3 --- Simulate a five-state absorbing Markov Chain
##  [[  1,   0,   0,   0,   0],
##   [0.3,   0, 0.7,   0,   0],
##   [  0, 0.5,   0, 0.5,   0],
##   [  0,   0, 0.6,   0, 0.4],
##   [  0,   0,   0,   0,   1]]
##### simulation
states=[0,1,2,3,4]
v =[0, 1/3, 1/3, 1/3, 0]
p0=[  1,   0,   0,   0,   0]
p1=[0.3,   0, 0.7,   0,   0]
p2=[  0, 0.5,   0, 0.5,   0]
p3=[  0,   0, 0.6,   0, 0.4]
p4=[  0,   0,   0,   0,   1]
n=15
S=np.zeros(n)
start=np.random.choice(states,1,p=v)
S[0]=start
for i in range(1,n):
    if S[i-1]==0: S[i]=np.random.choice(states,1,p=p0)
    if S[i-1]==1: S[i]=np.random.choice(states,1,p=p1)
    if S[i-1]==2: S[i]=np.random.choice(states,1,p=p2)
    if S[i-1]==3: S[i]=np.random.choice(states,1,p=p3)
    if S[i-1]==4: S[i]=np.random.choice(states,1,p=p4)
plt.close('all')
plt.plot(S,':',marker='.',markersize=14,markerfacecolor='r')
plt.xticks(range(n))
plt.yticks(states)
plt.title('A sample of Drunkard\'s Walk')
plt.ylabel('State')
plt.xlabel('Step number')
plt.show()
plt.close('all')
plt.show()
##### Problem 4 --- Compute the probability of absorption using the simulated chain
##  [[  1,   0,   0,   0,   0],
##   [0.3,   0, 0.7,   0,   0],
##   [  0, 0.5,   0, 0.5,   0],
##   [  0,   0, 0.6,   0, 0.4],
##   [  0,   0,   0,   0,   1]]
##### simulation
states=[0,1,2,3,4]
v=[0,0,1,0,0]
p0=[  1,   0,   0,   0,   0]
p1=[0.3,   0, 0.7,   0,   0]
p2=[  0, 0.5,   0, 0.5,   0]
p3=[  0,   0, 0.6,   0, 0.4]
p4=[  0,   0,   0,   0,   1]
n=15
N=10000
endAt0=0
endAt4=0
for k in range(N):
    S=np.zeros(n)
    start=np.random.choice(states,1,p=v)
    S[0]=start
    for i in range(1,n):
        if S[i-1]==0: S[i]=np.random.choice(states,1,p=p0)
        if S[i-1]==1: S[i]=np.random.choice(states,1,p=p1)
        if S[i-1]==2: S[i]=np.random.choice(states,1,p=p2)
        if S[i-1]==3: S[i]=np.random.choice(states,1,p=p3)
        if S[i-1]==4: S[i]=np.random.choice(states,1,p=p4)
    if S[n-1]==0: endAt0 += 1
    if S[n-1]==4: endAt4 += 1
print('b20 =',endAt0/N)
print('b24 =',endAt4/N)








