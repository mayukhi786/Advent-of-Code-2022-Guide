#---CAMP CLEANUP---



#PART 1

#Part 1 Answer: 424

#input data (these are pairs of ranges):

#input1 = ```Input data does here```


#Solution: 

#spliteach line of input into a list of pairs
data = input1.splitlines()

count = 0

for pairs in data:

    #we set up string slicing to obtain each component: each pair, and the two numbers in each pair
    first_pair = pairs[0 : pairs.index(',')]
    second_pair = pairs[pairs.index(',') + 1: ]

    first_number1 = first_pair[0 : first_pair.index('-')]
    second_number1 = first_pair[first_pair.index('-') + 1 : ]

    first_number2 = second_pair[0 : second_pair.index('-')]
    second_number2 = second_pair[second_pair.index('-') + 1 : ]


    #the condition for any one range being contained in another:
    #test if the start of the second is lower than the start of the first and the end of the second is lower than the end of the first, and vice versa.

    if (((int(first_number2) >= int(first_number1)) and (int(second_number1) >= int(second_number2))) or ((int(first_number1) >= int(first_number2)) and (int(second_number1) <= int(second_number2)))) :
        count += 1

#print (count)



#PART 2

#Part 2 Answer: 804

#input data same as before

count2 = 0

for pairs in data:
    #we set up string slicing to obtain each component: each pair, and the two numbers in each pair
    first_pair = pairs[0 : pairs.index(',')]
    second_pair = pairs[pairs.index(',') + 1: ]

    first_number1 = first_pair[0 : first_pair.index('-')]
    second_number1 = first_pair[first_pair.index('-') + 1 : ]

    first_number2 = second_pair[0 : second_pair.index('-')]
    second_number2 = second_pair[second_pair.index('-') + 1 : ]


    #the condition for the ranges to overlap (test if the end of one is greater than the start of the other, and that the start of one is lower than the end of the other):

    if ((int(first_number2) <= int(second_number1))) and ((int(first_number1) <= int(second_number2))):
        count2 += 1

print (count2)

