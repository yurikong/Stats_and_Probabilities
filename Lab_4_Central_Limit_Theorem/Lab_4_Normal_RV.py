import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Generate the values of the RV X
mu=2.5
sigma=0.75
n=10000
x=np.random.normal(mu,sigma,n)

# Create bins and histogram
nbins=30    # Number of bins
edgecolor='w'   # Color separating bars in the bargraph
#
bins=[float(x) for x in np.linspace(0,mu*2,nbins+1)]
h1, bin_edges = np.histogram(x,bins,density=True)
# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0]    # Width of bars in the bargraph
plt.close('all')

# Plot the bar graph
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

# Plot the normal PDF
def NormalPDF(mu,sigma,x):
    f=1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sigma**2))
    return f

f=NormalPDF(mu,sigma,b1)
plt.plot(b1,f,'r')
plt.title('Normal Random Variable')
plt.xlabel('x')
plt.ylabel('f(x)')

# Calculate the mean and standard deviation
mu_x=np.mean(x)
sig_x=np.std(x)

print(mu_x)
print(sig_x)
plt.show()
