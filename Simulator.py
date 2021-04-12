#Rakshak Adhikari
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt


NumberofEvents=10000

Lambda_values=[10,25,50,100] #list of parameter values

for Lambda in Lambda_values:


    #CREATES THE DISTRIBUTION

    data = np.random.poisson(Lambda, NumberofEvents)


    #WRITES THE OUTPUT IN A TEXTFILE
    np.savetxt("Data_"+str(Lambda)+".txt", data,fmt='%u')


