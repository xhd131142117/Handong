#file4.py     writing to files
##from random import *
##
##names=["emma","ali","john","hamza","george","jake"]
##
##
##tennisFile=open("tennis.txt","w")
##
##shuffle(names)
##print("After shuffling: ",names)
##
##for i in range(0,len(names),2):
##    #print(names[i]+" vs "+names[i+1])
##    #tennisFile.write(names[i]+" vs "+names[i+1]+"\n")
##    tennisFile.write("%-15s vs %-15s\n" %(names[i],names[i+1]))
##    
##    
##print("done")
##
##tennisFile.close()


###########################################################
#In file4.py we are not separating data from algorithm (file4.py
#only works for even number of elements in the list

#We will fix this in file5.py


##from random import *
##
##names=["emma","ali","john","hamza","george","jake","helen"]
##
##if len(names)%2==1: #odd number of elements
##    names.append("bye")
##
##
##tennisFile=open("tennis.txt","w")
##
##shuffle(names)
##print("After shuffling: ",names)
##
##for i in range(0,len(names),2):
##    #print(names[i]+" vs "+names[i+1])
##    #tennisFile.write(names[i]+" vs "+names[i+1]+"\n")
##    tennisFile.write("%-15s vs %-15s\n" %(names[i],names[i+1]))
##    
##    
##print("done")
##
##tennisFile.close()


####file6.py  - read from one file, write to another file
from random import *
namesFile=open("names.txt","r")

myList=namesFile.readlines()
namesFile.close()


if len(myList)%2==1: #odd number of elements
    myList.append("bye")


tennisFile=open("tennis.txt","w")

shuffle(myList)
print("After shuffling: ",myList)

for i in range(0,len(myList),2):
    #print(names[i]+" vs "+names[i+1])
    #tennisFile.write(names[i]+" vs "+names[i+1]+"\n")
    tennisFile.write("%-15s vs %-15s\n" %(myList[i],myList[i+1]))
    
    
print("done")

tennisFile.close()




















