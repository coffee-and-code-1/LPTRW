# sometimes you watn to to write tests that will check where your program goes wrong

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
    
def absolute_value(n):
    # buggy versionns
    # calculate the value of next
    if n < 0:
        return 1 
    elif n > 0:
        return n  
                  
    
def test_suite():
    # run teh suite of tests for code in this module
    # here we are calling on the function "test" that we defined above. 
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    # why did this fail 
    # because in your absolute value calculation, you return the number 1 for any negative number 
    test(absolute_value(0) == 0)
    # why did this fail 
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)
    # why did this fail 
    
# test_suite()

# write a program that takes one of the four compass points as its parameter and returns the next compass points
# so you probably need some list [1,2,3,4] and then you want to find the index of the 4 points in that list, and then add to the next point on the list 
# you want to look up the index, and then add 1 to it to get the next one. what if that number is at the end thouugh?
# so you would want something like if index is 0-2, then add 1. if index is 3, then go to 0. 

compass_list = ["W", "N", "E", "S"]

def turn_clockwise(x):
    if x not in compass_list:
        return None
    elif compass_list.index(x) < 3 and compass_list.index(x) >= 0:
        new_index = compass_list.index(x) + 1 
        print(compass_list[new_index])
        # here we want to look up the item in the list, given a specific place in index
    elif compass_list.index(x) == 3:
        new_index = 0 
        print(compass_list[new_index])
    else: 
        return None 
        
        
turn_clockwise("N")
turn_clockwise("W")
turn_clockwise(42)
turn_clockwise("rubbish")

# ****** why didn't these work? 
test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")
test(turn_clockwise(42) == None)
test(turn_clockwise("rubbish") == None)

days_of_week = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4:'Thursday', 5: 'Friday', 6: 'Saturday'}

# list out keys and value seperately -- I like this solution the most so far I think it's the most elegant 
key_list = list(days_of_week.keys())
val_list = list(days_of_week.values())

def day_name(num1):
    if num1 in key_list:
        position = key_list.index(num1)
        print(val_list[position])
    else:
        return None 
    
#day_name(5)  

# write a function day_name that converts an integer number 0 to 6 into the name of a day. 
# assume day 0 is "Sunday" 
# return none if the arguments are not valid 

test(day_name(3) == 'Wednesday')
# for some reason this test fails -- why? There is something happening where Python is recognizing Wednesday with Wednesday 

test(day_name(6) == 'Saturday')
test(day_name(42) == None)
# this one works 
# write an inverse function day_num which, given a day name, returns its number

# to print the key based on a value, wednesday
#position = val_list.index('Wednesday')
#print(key_list[position])


def day_num(name_of_day):
    # name of day is a value in this case, so you want to ch eck if it's in list
    if name_of_day in val_list:
        position = val_list.index(name_of_day)
        print(key_list[position])
    else:
        return None
        
        
test(day_name(3) == 'Wednesday')
# test failed
test(day_name(6) == 'Saturday')
# test failed 
test(day_name(42) == None)
# test worked 

# write a function that helps answer questions like 
# Today is Wed. I leave on holiday in 19 days. What day will that be. 

def day_add():
    current_day = input("What day is today? ")
    # this will return the full day 
    if current_day in val_list:
        position = val_list.index(current_day)
        num1 = int(key_list[position]) 
    days_until_holiday = input("How many days before you leave for holiday? ")
    days_to_add = (int(days_until_holiday)% 7)
    # now let's get the new result 
    departure_day = num1 + days_to_add 
    if departure_day > 6:
        final_result = departure_day - 6 - 1
    if departure_day <= 6:
        final_result = departure_day 
    print(val_list[final_result])
    

# day_add()

# can my day_add function work with negative deltas? 
# Let's see 

#print(-10 % 7)
# study what happens to modelo 

# write a function days_in_month which takes the name of a month, returns the number days of the month. 
calendar = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

month_list = list(calendar.keys())
number_of_days_list = list(calendar.values())

def days_in_month(name_of_month):
    if name_of_month in month_list:
        position = month_list.index(name_of_month)
        number_of_days = number_of_days_list[position]
        print(number_of_days)
        
days_in_month('July')

test(days_in_month("February") == 28)
test(days_in_month("December") == 31)

def to_secs(hours, minutes, seconds):
    # want to calculate total number of seconds 
    sec1 = hours * 60 * 60 
    # hours * minutes * seconds 
    sec2 = minutes * 60 
    total_seconds = int(sec1) + int(sec2) + int(seconds) 
    print(total_seconds)
    
to_secs(2.5, 0, 10.71)

# write three functions that are "inverses" of to_secs: 
def hours_in(seconds):
    # returns the whole integer number of hours represented by a total number of seconds 
    # take the number of seconds, divide it by 60 to get minutes, then divide by another 60 to get hours. 
    hours = (int(seconds)/60)/60
    limit_float = round(hours, 3)
    print(limit_float) 

hours_in(9010)

def minutes_in(seconds):
    # take the total number of seconds, get to total hours + minutes, and then take out the hours
    # you want the modulo function -- leftover minutes from the hours so something like x % 60 = what? since that is the hours. so you need to convert to minutes first 
    minutes = int(seconds)/60 
    leftover_minutes = minutes % 60 
    limit_float = round(leftover_minutes, 3)
    return limit_float 
    
print(minutes_in(9010))

def seconds_in(seconds):
    # returns the left over seconds represented by a total number of seconds 
    leftover_seconds = minutes_in(seconds) * 60
    new_leftover_seconds = leftover_seconds % 60 
    return new_leftover_seconds

print(seconds_in(9010))

test(3 % 4 == 0)
# fail
test(3 % 4 == 3)
# true 
test(3 / 4 == 0)
# fail 
test (3 // 4 == 0)
# what does this operator do? 
test (3+4 * 2 == 14)
# fail? should be 11 
test(4-2+2 == 0)
test(len("hello, world!") == 13)

# write a compare function that returns 1 if a > b, and 0 if a == b, and -1 if a < b 

def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0 
    else: 
        return -1 
        
print(compare(0,5))

test(compare(5,4) == 1)
test(compare(7,7) == 0)
test(compare(2,3) == -1)
test(compare(42,1) == 1)

def hypotenuse(a,b):
    # return length of hypotenuse of a right triangle given lengths of the two legs as parameters
    hyp = math.sqrt((a**2)+(b**2))
    hyp_cleaned = round(hyp, 3)
    return hyp_cleaned
    
print(hypotenuse(5,7))

test(hypotenuse(3,4) == 5.0)
test(hypotenuse(12,5) == 13.0)
test(hypotenuse(24,7) == 25.0)
test(hypotenuse(9,12) == 15.0)

def intercept(x1,y1,x2,y2):
    # returns the slope of the line through the points (x1,y1) and (x2,y2) 
    slope_m = (y2-y1)/(x2-x1)
    # now let's use the y = mx + b to find out what b is.  you just calculcated m, so plug in x and y. b = y1 - m(x1)
    y_intercept = (y1 - int(slope_m)*(x1))
    print(y_intercept)
    
    
test(intercept(1,6,3,12) == 3.0)
# failed - why? Is this an 'approximate' issue? 
test(intercept(6,1,1,6) == 7.0)
test(intercept(4,6,1,8) == 5.0)
    
# write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number
def is_even(n):
    if n % 2 == 0:
        print(True)
        return True 
    else:
        print(False)
        return False 

is_even(5)

def is_odd(n):
    if n % 2 == 0:
        print(True)
    else:
        print(False)
        
    
        
# modify is_odd to call is_even 
def is_odd_1(n):
    if is_even(n) == False:
        print(True)
    else:
        print(False) 

is_odd_1(5)

# write a function that passes these test 
def is_factor(f,n):
    if n % f == 0:
        return True
    else:
        return False 

print(is_factor(3,12))
test(not is_factor(5,12))
# these test that  yield true/false work -- it's just the tests that are somehow returning values that are not working properly based on how I coded them 

# create a function that can act as unambiguous specifications of what is expected 
# regardless of the ways the variables are put in, you know how to use it 

def is_multiple(a,b):
    if is_factor(min(a,b),max(a,b)) == True:
    # this was really interesting when i put only called the function factor(min(a,b),max(a,b)), the "return" was None, even though the return of the function is_factor itself was True/False
    # why is that? Why did I have to set th is result equal to True to return something else? 
    # maybe its because it's a function of our function, but t cannot be replicated as the entire function itself 
        return True 
    else:
        return False
    

print(is_multiple(12,3))
# interesting -- this result returns None -- why is that? 
test(is_multiple(12,4))
test(not is_multiple(12,5))
test(is_multiple(12,6))
test(not is_multiple(12,7))

# can we find a way to use is_factor in our defition of is_multiple? 

# write function f2c(t) that returns the integer value of the nearest degree Celsius for a given temp in F. use round()
def f2c(t):
    celcius = (t-32)*(5/9)
    final_celcius = round(celcius)
    print(final_celcius)
    print(type(final_celcius))
    if final_celcius == 100:
        print(True)
    else:
        print(False) 
    
    
test(f2c(212) == 100)



