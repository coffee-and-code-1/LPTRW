# Chapter 7: Iteration 

# count how many things of something you have 
# count how many notebooks you have 
# let this be a list of notebooks you have and attributes about them 
import turtle

notebooks = [
    ("Moleskin", ["Black", "Leather", "Unlined"]), 
    ("Midori", ["Unlined", "White", "Paper"]), 
    ("Travelers", ["Leather", "Brown", "Unlined"])]
    
counter = 0 
for (brand, qualities) in notebooks:
    for q in qualities:
        if q == "Leather":
            counter +=1 
            
print("The number of notebooks you have that are leather is", counter)

def sqrt(n):
    approx = n/2.0 # starting with a guess
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        approx = better 

# write a function to count how many odd numbers are on a list 
numbers_list = [1,3,5,6,7,8,9,10,13]

odds = 0 
for i in numbers_list:
    if i % 2 != 0:
        odds += 1

print("There are {0} odd numbers in your list".format(odds))

# sum up all the even numbers on a list 
total_sum = 0 
for i in numbers_list:
    if i % 2 == 0:
        total_sum += i 
        
print("The total of all even numbers in the list is {0}.".format(total_sum))

# sum up all negative numbers in the list
total_sum_odds = 0 
for i in numbers_list:
    if i < 0:
        total_sum_odds += i 

if total_sum_odds < 0:
    print("The total of all negative numbers in the list is {0}.".format(total_sum_odds))
else:
    print("There were no negative numbers in the list.")

# sum up all the elements in a list up to, but not including the first even number. 
# Why doesn't this work when I do a while loop? It seems like there is something else that you need to "activate" a while loop 

elements = 0 
for i in numbers_list:
    elements += i 
    if i % 2 == 0:
        break 
print("The total sum of odd numbers until the first even number is {0}.".format(elements))
    
# count how many words in a list have a length of 5 

words_list = ["Mango", "Pineapple", "Peach", "Apple", "Grape", "Papaya", "Dragonfruit"]

five_letter_words = 0 
for i in words_list:
    if len(i) == 5:
        five_letter_words += 1 
print("There are {0} five-letter words in our list.".format(five_letter_words))

# count how many words occur in a list up to, and including, the first occurance of the word "sam". What if "sam" does not occur? 

name_words_list = ["Ingrid", "Margo", "Yowei", "Paul", "Peter", "Andrew", "Sam"]

non_sam = 0 
for i in name_words_list:
    non_sam += 1
    if i == "Sam":
        break 

if non_sam == 0:
    print("There are no names that appear in the list before Sam.")
else:
    print("The number of names that appear before Sam is {0}.".format(non_sam))
    
# add a print function to Newton's sqrt function that prints out beter each time it is calculated. Call your m odified function with 25 as an argument and record the results. 

def modified_sqrt(n):
    approx = n/2.0 # starting with a guess
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better
            # here it means that if you satisfy this condition, you stop the loop, and "better" is your final result. otherwise, you continue on where you set approx to better
        approx = better 
 
modified_sqrt(25)

# write a function that prints out the first N triangular numbers. a call to print the function(5) would produce
# triangular number is any of the series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc.
def triangular_number(n):
    sum_tri_number = 0 
    for i in range (n+1):
        sum_tri_number += i 
    print(n,",",sum_tri_number)
        
triangular_number(5)
        
# now we have the specific unit calculation correct. but we want to print out all iterations of the resulting triangular numbers within a range so you'll want to call that function within a nother function
def triangular_number_set(n):
    for i in range(1,(n+1)):
        triangular_number(i) 
        
triangular_number_set(5)

# write a function, is_prime, which takes a singular integer argument and returns T rue when the argument is a prime # and false otherwise. add tests for cases like this


def is_prime(n):
    flag = True 
    for i in range (2,n):
        if (n%i) == 0:
            flag = False 
            break 
    if flag == True:
        print("This number is prime.")
    else:
        print("This number is not prime.")

is_prime(5)

# were you born on a prime day? 5151988? 

is_prime(5151988)

# let's revisit a drunk pirate problem from exercises in Chapt 3. drunk pirate makes a turn, takes some steps forward, and repeats this 

turn_data = [(160,20),(-43,10),(270,8),(-43,12)]
# where each pair represents the angle of each turn, and the number of steps taken in tha direction

#wn = turtle.Screen()
#wn.bgcolor("lightgreen")

#tess = turtle.Turtle()
#tess.color("pink","blue")
#tess.pensize(5)

# use right, left, forward to pivot and move 
#for angle, steps in turn_data:
    #tess.right(angle)
    #tess.forward(steps)

# let's now try to draw a house 
#tess.forward(100)
#tess.left(360/3)
#tess.forward(100)
#tess.left(360/3)
#tess.forward(100)
#tess.left(30)
#tess.forward(100)
#tess.left(90)
#tess.forward(100)
#tess.left(90)
#tess.forward(100)
#tess.left(135)
#tess.forward(sqrt((100**2)+(100*2)))
# you need to go a further distance

#wn.mainloop()

# write a function sum_of_squares(xs) that computes the sum of squares of the number in a list, xs. 
# sumsquares [2,3,44] should return 4+9+16 which is 29 

sum_squares_list = [2,3,4]

def sum_of_squares(xs):
    total_sum = 0 
    for i in xs:
        squared_number = i*i
        total_sum += squared_number 
    print(total_sum)
    
sum_of_squares(sum_squares_list)

# you and a friend are on a team to write a 2-player game, human vs computer like tic-tac-toe
# your friend will write the logic to play round 1 while you write the logic to allow many rounds of play, keep score, decide who plays first, etc. 
import sys 

def play_one(human_plays_first):
    # dummy scaffolding for now just to generate a "win" for either the human or the computer
    # the assumption here is that the human gets to take the first turn 
    import random 
    rng = random.Random()
    # pick a random result between -1 and +1
    # -1 means human wins, 0 is game drawn, +1 is computer wins 
    result = rng.randrange(-1,2)
    print("{0} plays first this round.".format(human_plays_first))
    if result == -1:
        print("Computer wins! {0} loses {1} point.".format(human_plays_first,result))
    elif result == 0:
        print("It's a draw!")
    else:
        print("{0} wins 1 point!".format(human_plays_first))
    return result 

def play_two(computer_plays_first):
    # dummy scaffolding for now just to generate a "win" for either the human or the computer
    # the assumption here is that the human gets to take the first turn 
    import random 
    rng = random.Random()
    # pick a random result between -1 and +1
    # -1 means human wins, 0 is game drawn, +1 is computer wins 
    result = rng.randrange(-1,2)
    print("Computer plays first this round.") 
    if result == -1:
        print("Human player wins!")
    elif result == 0:
        print("It's a draw!")
    else:
        print("Computer wins!")
    return result 
    
def main_game(name_of_player):
    
    total_human_points = 0 
    total_computer_points = 0 
    number_of_draws = 0 
    human_won_games = 0 
    computer_won_games = 0 
    import random
    rng = random.Random()
    
    while True:
            
            who_goes_first = rng.randrange(1,3)
            if who_goes_first == 1:
                additional_points = play_one(name_of_player) 
            # something is happening where the total human points is taking the same value as the result of the game 
            # i think it's because the total_human_points is being reset to ZERO each time you go through the "while True" -- how do we take the total_human points out? 
            # once we took the total_human_points = 0 and placed it BEFORE the 'while True' statement, it worked! The counter is now counting properly 
                if additional_points == 0:
                    number_of_draws += 1
                # we added this additional if statement to temporary pause the workflow to check if something else is there before continuing on
                if additional_points == 1:
                    total_human_points += additional_points
                    total_computer_points -= additional_points
                    human_won_games += 1
                if additional_points == -1:
                    total_human_points += additional_points
                    total_computer_points -= additional_points
                    computer_won_games += 1 
            # print(total_human_points) -- this was just to test we were on the right track / can take it out after we confirm we are
            if who_goes_first == 2:
                more_points = play_two(name_of_player)
                if more_points == 0:
                    number_of_draws += 1
                if more_points == 1:
                    total_human_points -= more_points
                    total_computer_points += more_points
                    computer_won_games += 1
                if more_points == -1:
                    total_human_points -= more_points
                    total_computer_points += more_points
                    human_won_games += 1     
            
            continue_or_not = input("Do you want to continue with this game? ")
            
            if continue_or_not == "yes":
                print("great, let's continue. ")
                print("the current score is {0} points for {1}, {2} points for the computer.".format(total_human_points,name_of_player,total_computer_points))
                print("the number of games the human and computer have won, respectively, are {0} and {1}. There have been {2} draws.".format(human_won_games, computer_won_games, number_of_draws))
            else:
                print("no worries, we'll play another day. goodbye.")
                print("the total points you generated were {0}, while the computer player generated {1} points. The were {2} draws.".format(total_human_points,total_computer_points,number_of_draws))
                percentage_wins = (human_won_games)/(human_won_games + computer_won_games + number_of_draws)
                adj_perc_wins = "{:.0%}".format(percentage_wins)
                print("The percentage win for the human player out of all games was {0}.".format(adj_perc_wins))
                exit()


main_game("Dave")
