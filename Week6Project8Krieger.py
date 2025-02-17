firstFile = input("Enter the name of the first file: ")
secondFile = input("Enter the name of the second file: ")
try:
    with open(firstFile, 'r') as f, open(secondFile, 'w') as w:
        for line in f:
            w.write(line)
except FileNotFoundError:
    print(filename + " does not exist!")
