with open('../data/notes.txt', 'r') as file:
    lines = file.readlines()
    print(f"Line 1: {lines[0].strip()}")
    print(f"Line 2: {lines[1].strip()}")
    print(f"Line 3: {lines[2].strip()}")
    print(f"Line 4: {lines[3].strip()}")