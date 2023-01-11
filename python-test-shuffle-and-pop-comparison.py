import random
import time

numtoshuffle = 10000000
numruns = 100


start = time.time()

for run in range (0, numruns):
    mylist = list(range(numtoshuffle))
    random.shuffle(mylist)
    while (len(mylist) > 0):
        nextitem = mylist.pop()
    
end = time.time()
print("Finished ", numruns, " runs of shuffling and popping from ", numtoshuffle, " elements in ", end - start, "seconds.");


start = time.time()

# this time advance a headat starting at 0, it is like a pointer saying where we are in the shuffled list.

for run in range (0, numruns):
    headat = 0

    mylist = list(range(numtoshuffle))
    random.shuffle(mylist)
    while (headat < (numtoshuffle)):
        nextitem = mylist[headat]
        headat += 1
    
end = time.time()
print("Finished ", numruns, " runs of shuffling and manually 'popping' via headat tracking from ", numtoshuffle, " elements in ", end - start, "seconds.");


