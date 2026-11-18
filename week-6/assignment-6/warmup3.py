#Warmup 3: Scope in Action
#Demonstrate variable scope with two short examples in one file:
#Define a variable inside a function. 
#Try to access it outside the function and show the NameError — paste the error in a comment, 
#then remove or comment out the line that causes it.
#Show how return solves the problem: return the value from the function 
#and assign it to a variable in the outer scope. Print it to confirm it worked.

#coffees_sold = 167 #If I remove this, then it will cause the NameError
#example 1
#def sold_drinks():
    #coffees_sold = 86
    #print("Inside:", coffees_sold)

#sold_drinks()

#print("Outside:", coffees_sold)
#NameError: name 'coffees_sold' is not defined

def sold_drinks():
    coffees_sold = 86
    return coffees_sold

result = sold_drinks()
print("Outside:", result) #print("Outside:", coffees_sold) #NameError: name 'coffees_sold' is not defined
#NameError: name 'coffees_sold' is not defined
