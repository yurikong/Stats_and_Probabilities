import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Generate the values of the RV X
N=10000
n=24
beta=40
mu_x=beta
sig_x=beta
X=np.zeros((N,1))
for k in range(0,N):
    x=np.random.exponential(beta,n)
    w=np.sum(x)
    X[k]=w

# Create bins and histogram
##nbins=1095
nbins=30    # Number of bins
edgecolor='w'   # Color separating bars in the bargraph
#
bins=[float(x) for x in np.linspace(0,n*beta*2,nbins+1)]
h1, bin_edges = np.histogram(X,bins,density=True)
# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0]    # Width of bars in the bargraph
plt.close('all')

# Plot the bar graph
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

# Plot the Gaussian function
def gaussian(mu,sig,z):
    f=np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
    return f

f=gaussian(mu_x*n,sig_x*np.sqrt(n),b1)
plt.plot(b1,f,'r')

plt.title('PDF of battery carton lifetime and comparison with Gaussian')
plt.xlabel('Battery carton lifetime for n='+str(n)+' batteries')
plt.ylabel('PDF')
plt.show()

# Plot the CDF
cs=np.cumsum(h1*barwidth)
##print(1-cs[1094])
##print(cs[911]-cs[729])
fig2=plt.figure(2)
plt.plot(b1,cs,'y')
plt.xlabel('Battery carton lifetime for n='+str(n)+' batteries')
plt.ylabel('CDF')
plt.title('CDF of battery carton lifetime')
plt.show()
