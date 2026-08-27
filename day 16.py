def prime_numbers():
    n=int(input())
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print("prime")
    else:
        print("not prime")
    prime_numbers()

def while_condition():
    i=int(input())
    while i<=10:
        print(i)
        i=i+1
    while_condition()

def while_condition():
    i=int(input())
    while i>=1:
        print(i)
        i=i-1
    while_condition()

def reverse_a_number_using_while_loop():
    n=int(input())
    r=0
    while n!=0:
        d=n%10
        r=r*10+d
        n=n//10
    print(r)
reverse_a_number_using_while_loop()
    
