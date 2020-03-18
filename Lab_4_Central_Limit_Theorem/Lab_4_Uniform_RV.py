import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Generate the values of the RV X
a=1
b=4
n=10000
x=np.random.uniform(a,b,n)

# Create bins and histogram
nbins=30    # Number of bins
edgecolor='w'   # Color separating bars in the bargraph
bins=[float(x) for x in np.linspace(a,b,nbins+1)]
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

# Plot the uniform PDF
def UnifPDF(a,b,x):
    f=(1/abs(b-a))*np.ones(np.size(x))
    return f

f=UnifPDF(a,b,b1)
plt.plot(b1,f,'r')

# Calculate the mean and standard deviation
mu_x=np.mean(x)
sig_x=np.std(x)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Uniform Random Variable')
##plt.show()
##print('mu_x',mu_x)
##print('sig_x',sig_x)
