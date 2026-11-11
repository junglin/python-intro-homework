#Warmup 4: Validation Function

#Write a function is_valid_score(score) that returns True if score is an integer between 0 and 100 
#(inclusive), and False otherwise. 
def is_valid_score(score):
    return score >= 0 and score <= 100

#Then use input() to ask the user for a score and 
#convert it to an integer with int() before you check it. 
score = int(input("Enter a score: "))

#Call your function inside an if statement and 
#print either "Valid score." or "Invalid score — must be between 0 and 100.".
if is_valid_score(score):
    print("Valid Score")
else:
    print("Invalid score — must be between 0 and 100.")