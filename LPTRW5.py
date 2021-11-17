# the continue statement -- is a flow control statement that causes the program to immediately skip the processing of the rest of hte body of the loop for the current iteration 
# but the loop still carries on [in the background?]

for i in [12,16,17,24,29,30]:
    if i % 2 == 1: 
        continue
    print(i)
print("done")


#def print_multiples(n):
    #for i in range(1,7):
        #print(n*i, end="   ")
        # using n instead of 2 is the process of generalizing 
    #print()

# another example of generalization (which is the making variables more flexible) 
# imagine you want a program th at prints out m ultiplcation table of any size, not just 6x6 table
#def print_mult_table(high):
    #for i in range(1, high+1):
        #print_multiples(i)
        

# the result of this is fine, except we might want the table to be square with the same # of rows and columns. 
# to do that, we add another parameter to print_multiples to specify how many columns the table should have 

# just to be annoying, we call this parameter high, demonstrating the different functions can have parametesr with the same name 

def print_multiples(n, high): 
    for i in range(1, high+1):
        print(n*i, end="   ")
    print()
    
def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, high) 
        
print_mult_table(7)