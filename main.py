from datetime import datetime



def fibonacci(n):
    if n==0 or n==1:
        return(1)
    return(fibonacci(n-1)+fibonacci(n-2))

for i in range(41):
    time_start=datetime.now()
    print(i, fibonacci(i), (datetime.now()-time_start))

