# ---RUCKSACK REORGANIZATION---



#PART 1

#Part 1 Answer : 7990

#Input data (These are lines of strings mixed with uppercase and lowercase characters):

#input1 = ```Input data goes here```

#Solution :

rucksacks = input1.splitlines() 
#getting each rucksack's string as a separate item in a list 'rucksacks'

common = []
#I think it's easier to create a list to store common letters directly instead of creating and calling a function later.

for line in rucksacks:
    part1 = line[0 : (len(line)//2)] #get each half of the string
    part2 = line[(len(line)//2) : ]
    common.append(list(set(part1) & set(part2))) #use sets to find common letter! (regular loops could be used but that's tedious and faulty, leading to index related errors all the time.)

    #sets are great data structures to find common letters between strings. 
    #Sets, characterized in Python by {} brackets, are like lists but with no two common elements, sets only contain distinct items. 
    #So, by converting both strings to sets and using the & operator, we can easily get the letter contained in both strings.
    #convert everything to a list from a set with the list() method, because sets are not subscriptable and we cannot access the individual element.

sum = 0

for letter_list in common : #parse through each list letter_list in the list common
    letter = str(letter_list[0]) #convert content of each list in the list to a string
    if letter.islower():
        sum += ord(letter) - 96 #ord() returns ascii value of a letter. Adjust according to the priority guide in the problem.
    else:
        sum += ord(letter) - 38 #for example, ord('Z') is 90, 90 - 38 = 52, which is the value of Z in the priorities.

print(sum)


#PART 2

#Part 2 Answer : 2602

#Input data same as before

def groups_of_3(list, n) : #function to break our list into groups of 3
    for i in range(0, len(list), n) : #parse over the list in steps of 3
        yield list[i : i + n] #yield separate lists of each set of 3 in successive iterations

common2 = []

for i in groups_of_3(rucksacks, 3): #use defined function to break rucksacks in sets of 3
    line1 = list(i)[0]
    line2 = list(i)[1]
    line3 = list(i)[2]
    common2.append(list((set(line1) & set(line2)) & set(line3))) #same logic using sets, as part 1


sum2 = 0

for letter_list in common2 : #parse through each list letter_list in the list common2
    letter = str(letter_list[0]) #convert content of each list in the list to a string
    if letter.islower():
        sum2 += ord(letter) - 96 #ord() returns ascii value of a letter. Adjust according to the priority guide in the problem.
    else:
        sum2 += ord(letter) - 38 #for example, ord('Z') is 90, 90 - 38 = 52, which is the value of Z in the priorities.

print(sum2)



