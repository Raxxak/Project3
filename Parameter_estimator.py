#Rakshak Adhikari
# imports packages
from natsort import natsorted

from scipy.optimize import minimize

import numpy as np
import matplotlib.pyplot as plt
import glob # this is needed to read all the files recursively  

Lambdas=[10,25,50,100]
Lambda_estimated=[]
y_error=[]
files=natsorted(glob.iglob("*.txt"))
for file in files:
    print(file)
    f = open(file, "r")


    array=[]
    for line in f:
        array.append(int(line))
    array=np.array(array)

    x_sum=np.sum(array) #this is the sum of the x values
    #Define negative log (base e) Likelihood function (without the factors)     
    def Likelihood(x):
        return  len(array)*x-x_sum*np.log(x)
    #It minimizes the  function

    maximum_value = minimize(Likelihood,1)
    Lambda_estimated.append(float(maximum_value.x))
    y_error.append(np.power(5*float(maximum_value.hess_inv),0.5))
    
Lambda_estimated=np.array(Lambda_estimated)
print(Lambda_estimated)
print(y_error)


#Plotting
fig,ax=plt.subplots()
ax.errorbar(Lambdas,Lambda_estimated,yerr=y_error,linewidth=0.5, markersize=2, marker='o')

plt.title("True vs estimated Lambda for small Lambdas")
plt.xlabel("True Lambda")
plt.ylabel("Estimated Lambda")

plt.savefig("fig2.pdf")


   




