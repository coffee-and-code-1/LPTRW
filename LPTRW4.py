# iteration
# while statement 

import sys
import math

def test(did_pass):
    # print the result of a test
    lineum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(lineum)
    else:
        msg = "Test at line {0} FAILED".format(lineum)
    print(msg) 

# a new assignment overwrites the value you ascribed to a variable before and assignes a new value
airtime_remaining = 15
print(airtime_remaining)
airtime_remaining = 17
print(airtime_remaining)

# important to distinguish between an assignment statement and a Boolean expression taht tests for equality. 
# equality test is symmetric, but assigment is not. 
# for example, if a == 7 and 7 == a, but in python teh statement a = 7 is ok while 7 = a is not ok 

a = 5 
b = a
a = 3 

# before you can update a variable, you have to initialize it to some starting value, usually with a simple assignment 

runs_scored = 0 
runs_scored = runs_scored + 1 

# running through all items in a list is called traversing the list, or traversal 

def mysum(xs):
    running_total = 0 
    for x in xs:
        running_total = running_total + x 
    return running_total 
    
test(mysum([1,2,3,4]) == 10)
test(mysum([1.25,2.5,1.75]) == 5.5)
test(mysum(range(11)) == 55)

# interesting -- these tests did work -- why didn't LPTRW3.py work? 

# an endless source of amusement for computer scientists is the observation that the directions on shampoo, "lather, rinse, repeat" are an infinite loop. 
# talk about nerdy humor lol 

# while loop is more work than the for loop because for loop truncates more easily, but while loop is more powerful 

def sum_to(n):
    ss = 0 
    for v in range(n+1):
        ss = ss + v
    return ss 
    
#halve n, or multiply it by 3 and add 1. the sequence terminates when n reaches 1. 

def seq3np1(n):
    # print the 3n+1 sequence from n, terminating when it reaches 1 
    while n != 1:
        print(n, end=", ") 
        # what does this actually mean?
        if n % 2 == 0:
            n = n // 2 
        else:
            n = n * 3 + 1
    print(n, end=".\n")
    
seq3np1(5)

# the following function counts the number of decimal digits in a positive integer 

def num_digits(n):
    count = 0 
    while n != 0:
        count = count + 1 
        n = n // 10
    return count 
    

# if we only wanted to count digits that are either 0 or 5, adding a condition will do the trick 

def num_zero_and_five_digits(n):
    count = 0 
    while n > 0:
        digit = n % 10 
        if digit == 0 or digit == 5:
            count = count + 1 
        n = n // 10 
    return count 
    
test(num_zero_and_five_digits(1055030250) == 7)
test(num_digits(0) == 1)

# this will fail -- why? 

# incrementing is common 
#count += 1 is an abbreviation for count = count + 1 
# we pronounce the oeprator as 'plus-equals' 
# the incremental value does not have to be 1

# *=, -=, //=, %=

# so the equal sign always comes after 

# python comes with lots of documentation about its built-in functions and libraries 
# wh en you see [] that means it's optional
# range ([start,] stop [,step]) -- in this case, start is optional. 
# when letters are italicized, it's a variable/something permutable but regular block letters implies that it's a keyword and should be typed exactly as 

# you could print multiple things at the same time if you desired 
# print([object, object2, object3]) etc. 

# loops are good for generating tables. 

for x in range(13):
    print(x, "\t", 2**x)
    #\ this backlash character in \t indicates the beginning of an escape sequence 
    # escape sequences are used to represent invisible characters like tabs and newlines 
    #\n represnts a newline 

# two dimensional table is where you read the value at the intersection of a row and column 
# write a loop that prints the multiples of 2, all on one line 

for i in range (1,7):
    print(2*i, end=" ")
    # this end supresses the n ewline python would automatically use -- and uses 3 spaces instead. 
    # after the loop is done, the call to print at line 3 finishes the current line and startsa  new line

# next let's encapsulate and generalize 

#encapsulate is process of wrapping a piece of code in a function, allowing you to take advantage of all the things functions are good for
# generalization means taking something specific, and making it more general such as printing the multiples of any integer 

# this function encapsulates previous loop and generalizes it to print multiples of n (instead of 2)
def print_multiples(n):
    for i in range(1,7):
        print(n*i, end="   ")
        # using n instead of 2 is the process of generalizing 
    print()

for i in range(1,7):
    print_multiples(i)
    
    
def print_mult_table():
    for i in range(1,7):
        print_multiples(i)
        # here we are demonstrating encapsulation again, taking the code from teh last section and wrapping it in a function 
        # this process is a common development plan. 
        # we develop code by writing lines of code outside of a function 
        # then when we know it's working, we extract it and wrap it up in a function 
        
# -- local variables
# n being used in three different function is not the same n. variables created inside a function are local and you can't access it from outside its home function. 

# break statement is used to immediately leave the body of its loop. The next statement to be executed is the first one after the body 

#the while boolean expression uses the Boolean to determine whether to iterate ag ain 
# while True: means always do the loop body again. 

import random 
rng = random.Random()
number = rng.randrange(1,1000)

guesses = 0 
msg = ""
# the creation of this 'msg' is to make it so that you have something to add text to -- just like your "guesses" starts at zero so you have some initiaiozation
# you're doing the same thing with a string 

while True:
    guess = int(input(msg + "\nGuess my number between 1 and 1000: "))
    guesses +=1 
    if guess > number:
        msg += str(guess) + " is too high. \n"
    elif guess < number:
        msg += str(guess) + " is too low. \n"
    else:
        break 
        
input("\n\nGreat, you got it in {0} guesses!\n\n".format(guesses))
# this didn't do anything -- there is a call to the input function, but we didn't do anything with the result, not even assign it to a variable. 
# here it has the effect of popping up the input dialog window and waiting for the user to respond before the terminates. 
# programers use the trick of doing some extra input at the end of a script, to keep the window open. 

# th is program makes use of the math law of trichotomy (given real numbers a and b, exactly one of these 3 must be true: a > b, a < b, or a == b)

# the continue statement -- is a flow control statement that causes the program to immediately skip the processing of the rest of hte body of the loop for the current iteration 
# but the loop still carries on [in the background?]

for i in [12,16,17,24,29,30]:
    if i % 2 == 1: 
        continue
    print(i)
print("done")


    
    
    
    




