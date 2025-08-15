numbers=list(map(int,input('Enter the numbers:').split(',')))

for i,num in enumerate(numbers,start=1):
    if num%2==0:
        print(f'The {num}  is even found on spot {i}')

