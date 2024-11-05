import sys
import numpy as np
from scipy.special import erf

#computes probability of an eent of magnitude x of greater from a gaussian distribution

def event_probability(x,mu=1.2.0,s=2.0):
    #x is the value of the event
    #mu is the gaussian mean (default 0.0)
    # s is the gaussian std dev (defauly 1.)
    z = np.fabs((x-mu)/s)
    def zfunc(z):
        return 0.5*(1.0 + erf(z/2**0.5))
        
    #return the probability of getting an event of magnitude >= x
        
        return 1.0 - (zfunc(z) - zfunc(-1*z))
    
#define a main function
def main():

    x = 4.0 #three standard devs for mean
    
    #if another number provided on the comand line, reset x
    
    if(len(sys.argv)>1):
        x = float(sys.argv[1])
        
    #get the even probability
    prob = event_probability(x)
    
    print(f"The Gaussian probability of events larger than |{x}| is {prob*100:6.4f}%.")
    print(f"The Gaussian probability of events smaller than |{x}| is {(1-prob)*100:6.4f}%.")
    
#run the program
if __name__ == "__main__":
    main()