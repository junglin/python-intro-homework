#Create two hardcoded lists of programming languages (some overlap, some unique to each list). 
#Convert each to a set and print:

list1 = ["python", "c++", "java", "html"]
list2 = ["html", "javascript", "ruby", "python"]

list1_set = set(list1)
list2_set = set(list2)

#The union (all languages from both lists, no duplicates)
print(f"combined: {list1_set.union(list2_set)}")

#The intersection (languages in both lists)
print(f"intersection: {list1_set.intersection(list2_set)}")

#The difference (languages only in the first list)
print(f"difference: {list1_set.difference(list2_set)}")
