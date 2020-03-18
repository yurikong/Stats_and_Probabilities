import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def clt_plot(a,b,n,N):
    # Generate the values of the RV X
    mu_x=(a+b)/2
    sig_x=np.sqrt((b-a)**2/12)
    X=np.zeros((N,1))
    for k in range(0,N):
        x=np.random.uniform(a,b,n)
        w=np.sum(x)
        X[k]=w

    # Create bins and histogram
    nbins=30    # Number of bins
    edgecolor='w'   # Color separating bars in the bargraph
    #
    bins=[float(x) for x in np.linspace(n*a,n*b,nbins+1)]
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
    plt.title('PDF of book stack height and comparison with Gaussian')
    plt.xlabel('Book stack height for n='+str(n)+' books')
    plt.ylabel('PDF')
    plt.show()

a=1
b=4
N=10000
clt_plot(a,b,1,N)
clt_plot(a,b,5,N)
clt_plot(a,b,15,N)
