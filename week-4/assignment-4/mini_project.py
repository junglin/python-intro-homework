students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},

# Find the top scorer
highest_score = 0
highest_scoring_student = ""

#Class average - total scores/ number of scores
total = 0
# Number of students
size_of_classes = len(students)
class_average = 0
# Set of unique class subjects
unique_subjects = set()

#Looping through list of students
for student in students:
    score = student["score"]

    #Update total amount of scores
    total += score

    # Get class subjects to sets
    subject = student["subject"]
    unique_subjects.add(subject)

    # calculating highest score
    if score > highest_score:
            highest_score = score
            highest_scoring_student = student["name"]

#list of high scorers
high_scorers = []
for student in students:
    current_score = student["score"]

    if current_score > 75:
        high_scorers.append(student["name"])

class_average = total/ size_of_classes

#printing report
print(f"Top Scorer: {highest_scoring_student} ({highest_score})")
print(f"Class Average: {class_average}")
print(f"Subjects offered: {unique_subjects}")
print(f"High Scorers: {high_scorers}")
