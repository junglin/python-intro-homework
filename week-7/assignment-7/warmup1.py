with open('../data/notes.txt', 'r') as file:
    for i, line in enumerate(file, 1):
        print(f"Line {i}: {line.strip()}")