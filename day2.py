# ---ROCK PAPER SCISSORS---



#PART 1

#Part 1 Answer: 10718

#Input data (these are pairs of letters):

#input1 = ```Input data goes here```

#Solution:

possible_endings_1 = {'A X' : 4, 'A Y' : 8, 'A Z' : 3, 'B X' : 1, 'B Y' : 5, 'B Z' : 9, 'C X' : 7, 'C Y': 2, 'C Z': 6}
#I created a dictionaries with every possible outcome and its corresponding score as key-value pairs.

strategy = input1.splitlines()
#get each line of the strategy input

print (sum([possible_endings_1[each] for each in strategy]))
#using the dictionary, parse through to get the score for each ending in the strategy, and find its sum.



#PART 2


#Part 2 Answer: 14652

#Input data same as part 1

possible_endings_2 = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}
#follow same logic to create dict of possible endings and scores.
#calculate cumulative score from win/draw/lose and the points you get from choosing Rock/Paper/Scissors.

print (sum([possible_endings_2[each] for each in strategy]))


