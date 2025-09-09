#Task 2: Write and Append Data to a File
with open('output.txt','w') as f:
    a=input('Enter text to write to the file: ')
    f.write(a)
    print('Data successfully written to output.txt')

with open('output.txt','a') as d:
    b=input('Enter the additional text to append: ')
    d.write('\n'+b)
    print('Data successfully appended.')

with open('output.txt','r') as g:
    print('final content of output.txt: ')
    c=g.read()
    print(c)

