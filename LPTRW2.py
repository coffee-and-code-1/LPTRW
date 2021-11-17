

#week_dictionary = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}


#def get_key_from_value(d, val):
    #keys = [k for k, v in d.items() if v == val]
    #if keys:
        #return keys[0]
        # I think if you don't put a [0] after keys, then it's returning a list, and not an integer 
    #return None
# what is this function saying?
# it's saying that with the parametesr, d and value -- where d is your dictionary, and val is the values associated with your ikeys 
# we are assigning k and v to the keys and values in dictionary items if the value we've input here is equivalent to the values in our dictionary 
# if keys exists, 
# not sure what this code is saying exactly now that I think about it. 
# ok now I think I got it
# your parameters are dictionary and values
# your keys is assigned as k, and v assigned as values in your dictionary items if and only if they find the value is located in your dictionary 
# then under those circumstances, if the key exists, they want to return the key at position zero? What about not position zero? 

#depart_day = input("What day of the week are you leaving for vacation? Please fully spell out the day ")

#print(get_key_from_value(week_dictionary, depart_day))
#print(type(get_key_from_value(week_dictionary, depart_day)))
# this will return the key to your answer -- 1, 2, 3, 4, etc. 
    
# this method is saying, within the dictionary and age, return the key after searching among the values for your age 



#vacation_duration = input("How many days will you be gone for? ")
#days_after_depart = (int(vacation_duration) % 7)
#print(days_after_depart)

#def get_new_day(sz):
    #new_day = (sz + get_key_from_value(week_dictionary, depart_day))
    # now that you've calculated the new day, you want to find the value that corresponds to this key in your dictionary 
    #print(week_dictionary.get(new_day))
 
    # you want to take the values you already got from get_key_from_value result 
    # so you want to feed in the original assumptions it had 
    
#get_new_day(days_after_depart)




#you want the code to be something like 
#mon = 1 
#tues = 2 
#wed = 3 
#thurs = 4
#fri = 5 
#saturday = 6
#sun = 7 

#and then the remainder, is added to your number

#so you need to assign a code to th e initial input
#then add the two numbers
#and then look back to the mapping code 
#so possibly you want to create a dictionary with key/code type thing 



import math 
import statistics 


def resulting_grade(mark):
    if mark >= 75:
        print("first")
    elif mark < 75 and mark >= 70:
        print("upper second")
    elif mark < 70 and mark >= 60:
        print("second")
    elif mark < 60 and mark >= 50:
        print("third")
    elif mark < 50 and mark >= 45:
        print("F1 Supp")
    elif mark < 45 and mark >= 40:
        print("F2")
    else:
        print("F3")
        
#test_grade = int(input("What was your test grade? "))

#resulting_grade(test_grade)

#class_grades = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

#for grades in class_grades:
    #resulting_grade(grades)
    
    
def find_hypot(a,b):
    c = math.sqrt((a**2)+(b**2))
    print(int(c))

find_hypot(10,10)

# write a function that given 3 sides, you can determine if it's right angle. i.e. if you c**2, does that equal to a**2 + b**2 

def right_angle(a,b,c):
    if abs(c**2 - ((a**2)+(b**2))) < 0.0001: 
        print("True")
    else:
        print("False")
        
right_angle(10,10,math.sqrt((10**2)+(10**2)))
  
# extend this program to take sides of any function -- so you need to add a "max" function if you will 

def sorted_angles(a,b,c):
    data1_list = [a,b,c]
    hypotneuse_side = max(data1_list)
    side_1 = min(data1_list)
    side_2 = statistics.median(data1_list)
    if abs(hypotneuse_side**2 - ((side_1**2)+(side_2**2))) < 0.0001: 
        print("True")
    else:
        print("False")

sorted_angles(math.sqrt((10**2)+(10**2)),10,10)

# Python code to demonstrate the 
# working of median() function.

a = math.sqrt(2.0)
print(a, a*a)
print(a*a == 2.0)

# fruitful functions -- more functions that return value 

# first example is area, which returns the area of a circle with the given radius: 
def area(radius):
    b = 3.14 * radius**2
    return b 
    
    
area(5)