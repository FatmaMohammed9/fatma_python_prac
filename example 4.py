num_of_rows = 5
for c in range(1,num_of_rows+1):
    n =''
    for l in range(num_of_rows-c):
        n +=' '
    for l in range(2*c-1):
        n += '*'
        print(n)