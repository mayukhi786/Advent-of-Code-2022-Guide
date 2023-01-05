# ---CALORIE COUNTING---




#PART 1

#Part 1 Answer: 73211

#Input data (these are \n\n separated blocks of individual \n separated integers):

#input1 = ```Input data goes here```


#Solution:

calorie_blocks = input1.split("\n\n")
#get each big block by splitting at each double newline

calories = [[int(line) for line in block.splitlines()] for block in calorie_blocks]
#list comp. is cool! 
#For each block of integers, use splitlines() to get each integer as a string and then parse it as an int.
#This creates a list of all the calories per block as integers.

print(max(sum(each) for each in calories))
#find max of the sum of elements in each list calories.


#PART 2


#Part 2 Answer: 213958

#Input data same as part 1

#Solution: 

import heapq #very handy dandy tool :)

#heapq comes with the .nlargest function whose usecase is exact problems like these!

max_3 = sum(heapq.nlargest(3, (sum(each) for each in calories)))
#.nlargest(n: int, list: List[]) returns the n largest items in list
print(max_3)




