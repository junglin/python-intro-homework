#Create a hardcoded dictionary representing a student with these keys: 
#name, grade, and subjects (a list of subject strings). Then:
student = {
    "name": "wendy",
    "grade": 12,
    "subjects": ["calculus", "american government", "chemistry"]
}

#Print each key-value pair using .items() in a for loop
for key, value in student.items():
    print(key, value)

#Add a new key "graduated" with the value False
student["graduated"] = False

#Print the updated dictionary
print(student)