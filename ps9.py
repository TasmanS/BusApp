# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#
import copy
import itertools

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # splits lines, turns them into a dictionary of Course name and then two remaining values
    
    inputFile = open(filename)
    subjectDict={}
    for line in inputFile:
        listS=line.split(",")
        subjectDict[str(listS[0])]=(int(listS[1]),int(listS[2]))
    return subjectDict



def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    for s in subNames:
        val = subjects[s][0]
        work = subjects[s][1]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += int(val)
        totalWork += int(work)
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print(res)

#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    return subInfo1[0]>subInfo2[0]


def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    return subInfo1[1]<subInfo2[1]


def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    return (subInfo1[0]/subInfo1[1])>(subInfo2[0]/subInfo2[1])



def updatetotWork(selectedSubjects):
    totWork=0
    for entry in selectedSubjects:
        totWork+=selectedSubjects[entry][1]
    return totWork

    
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """

    # In general, greedy algorithms have five components:
    # A candidate set, from which a solution is created
    # A selection function, which chooses the best candidate to be added to the solution
    # A feasibility function, that is used to determine if a candidate can be used to contribute to a solution
    # An objective function, which assigns a value to a solution, or a partial solution, and
    # A solution function, which will indicate when we have discovered a complete solution

    
    #create a dict for the selections, and a copy of subjects to pair down 
    selectedSubjects={}
    subjectsDict=copy.copy(subjects)
    totWor=0
    removeDict={}
    
    
    while totWor<maxWork and len(subjectsDict)!=0:
        
        selection=0
        totWor=updatetotWork(selectedSubjects)

        #this is where the list is paired down based on >15 hours or already in the selected courses
        for entry in subjectsDict.keys():
            if subjectsDict[entry][1]+totWor>15 or entry in selectedSubjects:
                removeDict[entry]=subjectsDict[entry]

        # takes the removed entries out
        for removed in removeDict.keys():
            subjectsDict.pop(removed,0)


        # now when we go over all the remaining entries, they should all work if picked
        # we can go one by one and find the best choice based on comparatar
        for subject in subjectsDict.keys():

            #if this is the first time through the list or the first time after a selection is made, the first item up is the default
            if selection==0:
                selection=subject
                continue

            # if the next iteration is better than selection, changes selection to the iteration, subject
            elif comparator(subjectsDict[subject],subjectsDict[selection]):
                selection=subject
                print(selection)
                                   
            else:
                pass        

        #breaks the loop so the default 0 value doesn't get added
        if selection==0:
            break

        # the bottleneck (i think) this whole time was the dang GET() method
        selectedSubjects[selection]=subjectsDict.get(selection)

    print(selectedSubjects)        
    printSubjects(selectedSubjects)        
          

# Problem 3: Subject Selection By Brute Force

def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # splits lines, turns them into a dictionary of Course name and then two remaining values
    
    inputFile = open(filename)
    subjectDict={}
    for line in inputFile:
        listS=line.split(",")
        subjectDict[str(listS[0])]=(int(listS[1]),int(listS[2]))
    return subjectDict

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # first, create a data type of each permutation of 20 combos 


def createBruteList(filename):
    """
    create list to use in the Bruce force advisor combination method  
    """

    # Creates a list to make combos out of
    
    inputFile = open(filename)
    bruteList=[]
    for line in inputFile:
        listS=line.split(",")
        bruteList+=[listS[0]]
    inputFile.close()
    return bruteList

# combo maker
def createCombinations(bruteList):
    return itertools.combinations(bruteList,3)

#now check the entries - same process
# pair down first, then score
def evaluateCombos(iterableList,scoringDict):
    """ given these inputs, will spit out a list(?) with score=max possible"""

    updateList=[]

    #Goes through the genned Tuples, cleans out any that total too much time (current=8)
    for entry in iterableList:
        selectTime=0
        for course in entry:
            selectTime+=scoringDict[course][1]
        if selectTime<=8:
            updateList.append(entry)

    print(updateList)

    ### this is where I left off. Need to take the winners in update list and score them to see which is best
    #once this code is all in it should be pretty easy to point these at the big lists/dicts and COMPLETELY CRASH MY SHIT
            



        
scoringDict=loadSubjects(SHORT_SUBJECT_FILENAME)
iterableList=createCombinations(createBruteList(SHORT_SUBJECT_FILENAME))

evaluateCombos(iterableList,scoringDict)





