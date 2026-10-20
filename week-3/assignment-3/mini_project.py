day = input("What day of the week is it?").lower()
time = input("Is it the morning, afternoon, or evening?").lower()

if day == "monday" and time == "morning":
    print("It's time to get ready for work!")
elif day == "monday" and time == "afternoon":
    print("It's time to take your 30 minute lunch break!")
elif day == "tuesday" and time == "afternoon":
    print("It's time to take a walk!")
elif day == "wednesday" and time == "evening":
    print("It's time to study Python before bed!")
elif day == "thursday" and time == "evening":
    print("It's time to put a face mask on!")
elif day == "friday" and time == "evening":
    print("Get ready for date night!")
elif day == "saturday" and time == "afternoon":
    print("It's time to study and complete your weekly assignments.")
elif day == "sunday" and time == "morning":
    print("Get ready for the farmer's market.")
elif day == "sunday" and time == "afternoon":
    print("Great time to meal prep for the week.")
else:
    print("Sorry, I don't recognize that day. Please try something else.")




