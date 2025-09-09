#Task 1: Read a File and Handle Errors

line_number=1
try:
    with open('sample.txt','r') as f:
        print('reading file content: ')
        for l in f:
            print(f'line {line_number}: {l}',end='')
            line_number += 1
except FileNotFoundError as e:
    print(f"error: this file 'sample.txt' does not exist")