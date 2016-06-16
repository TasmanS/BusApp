# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''


# PROBLEM 1

class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        
        self.maxBirthProb=maxBirthProb
        self.clearProb=clearProb


    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        if random.random()<=self.clearProb:
            return True
        else:
            return False

    
    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        if random.random()<=self.maxBirthProb*(1-popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException()



class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        self.viruses=viruses
        self.maxPop=maxPop


    def getTotalPop(self):

        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)      


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
                              
        ## Check if virus is cleared in time step
        ## if not, add to surviving virus list
                                                    
        surVirus=[]
                              
        for v in self.viruses:
            if v.doesClear():
                pass
            else:
                surVirus.append(v)

        self.viruses=surVirus[:]

        ## Calculate population density
                              
        popDensity=0                      
        popDensity=len(surVirus)/self.maxPop

        ## Check if reproduces, return new child virus
        ## Add new virus to surVirus list
        
        for v in surVirus:
            try:
                self.viruses.append(v.reproduce(popDensity))
            except:
                pass

#
# PROBLEM 2
#
def simulationWithoutDrug():

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    
    #create list of 0's to add virus pops to    
    plotViruses=[]
    for n in range(300):
        plotViruses.append(0)

    #create list of 100 virus instances    
    viruses=[]
    for n in range(100):
        viruses.append(SimpleVirus(0.1,0.05))

    # Do 10 trials of simulation
    for n in range(1000):  
         
        #create patient class with 100 viruses and pop=1k        
        Troy=SimplePatient(viruses,1000)

        #updates to 300 time units
        for n in range(300):
            Troy.update()
            plotViruses[n]=plotViruses[n]+Troy.getTotalPop()

    # divided by trials for average pops
    for n in range(300):
        plotViruses[n]=plotViruses[n]/1000
        

    #plot and visualize
    pylab.plot(plotViruses)
    pylab.title('Virus Reproduction')
    pylab.xlabel('Time')
    pylab.ylabel('Virus Population')
    pylab.show()



## Problem 3


def MonteCarlo(tests):
    resultArray=[]
    for test in range(tests):
        yes=0
        for trials in range(100000):
            dieRoll=[]
            for roll in range(5):
                dieRoll.append(random.randint(1,6))
            if dieRoll[0]==dieRoll[1] and dieRoll[0]==dieRoll[2] and \
            dieRoll[0]==dieRoll[3] and dieRoll[0]==dieRoll[4]:
                yes+=1
        resultArray.append(yes)

    average=sum(resultArray)/len(resultArray)

    ratio=average/100000
    
    print(average)
    print(ratio)



## Results from 200 trials:
    # 77.7
    # 0.000777
    # Which is very close to right:
    # >>(1/6)**4
    #0.0007716049382716048


    
    

