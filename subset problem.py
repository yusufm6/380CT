from random import randint, sample
import itertools
from time import time
import math
class SSP():
    #initializing the SSP object
    def __init__(self, S=[], t=0):
        self.S = S #empty set to  start with
        self.t = t #target set to 0 initially
        self.n = len(S) #length of the set (i.e. number of elements)
        #
        self.decision = False 
        self.total    = 0
        self.selected = [] #empty set for the selected subset
    def __repr__(self):
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
    
    def random_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = randint(0,n*max_n_bit_number)
        self.n = len( self.S )
    #generate random SSP instance which will generate a solution
    def random_yes_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        #generate a random set of integers of length n
        #and store as reverse sorted
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=False)
        #set the target value to the sum of a sample subset of the set
        #where the length of the sample set is a randint between 0 and n (4)
        self.t = sum( sample(self.S, randint(0,n)) )
        #set n property of object to length of the set 
        self.n = len( self.S )
    ###
    #try generating a solution randomly (greedy algorithm)
    def try_at_random(self):
        #initialise a empty set for the candidate
        candidate = []
        #current total of sum of subset
        total = 0
        #whilst the total sum is not equal to target keep trying
        while total != self.t:
            #get a random sample of between 0 and 4 elements to test
            candidate = sample(self.S, randint(0,self.n))
            #evaluate the total of the subset
            total     = sum(candidate)
            print( "Trying: ", candidate, ", sum:", total )
    
    #function to perform the brute force         
    def brute_force(self, n, bitlength=10):
       max_n_bit_number = 2**bitlength-1
       #calls the function getSubsets to generate all the subsets for the initial set and return the subsets
       subsets =  self.getSubsets()
       total = 0
       #loop through every set of the subsets
       for set in subsets:
            #set the total to equal the sum of the current set
           total = sum(set)
           #print the set that is currently being tested
           print("Trying: ", set, ", sum:", total )
           #if the total does not match the value of t which is the target value then solution has been found
           if (total == self.t):
            #print the solution out
              print("Solution: " +str(set))
              return True
    def Dynamic_Programming(self, n, bitlength=10)


    def GreedyAlgorithm(self, n, bitlength=10):
        total = 0
        subsets = []
        for i in range(0, len(self.S)):
            if (sum(subsets) + self.S[i]<= self.t):
                subsets.append(self.S[i])
                total = total + self.S[i]
            else:
                print(total-self.t)
                break
        return subsets
    
    #function to generate all the subsets of the initial set
    def getSubsets(self):
        #empty array to store all the subsets, len will be equal to 2^n where n is the length of the initial set
        results = []
        #loops through the length of the set and generates a non repeated array of subsets
        for i in range(0,len(self.S)+1):
            #use combinatorics to find all possible non repeated combinations (subsets) of the initial set 
            results += itertools.combinations(self.S,i)
        #loop through the results array and print all the subsets
        for x in results:
            print(list(x))
        return results
        
instance = SSP() #generate instance of SSP Class and initialise
instance.random_yes_instance(4)
print( instance )
##instance.try_at_random()
#call the brute force method passing in a length  for the array instance to be generated
print("Solution: " +str(sum((instance.GreedyAlgorithm(4)))))
