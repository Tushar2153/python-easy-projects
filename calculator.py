import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

x={
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}

def calculations():
    
    n1=float(input("Enter first number :"))
    for symbol in x:
        print(symbol)
        
    flag=False
    
    while not flag:
        pick=input("pick an operation")
        n2= float(input("Enter second number"))

        oper=x[pick]
        output=oper(n1,n2)
        print(f"{n1} {pick} {n2} = {output}")

        same=input(f"type 's' if you want to calculate using {output} or type 'x' to exit or type 'n' for new calculation ")

        if same=='s':
            n1=output
        elif same=='x':
            flag=True
        elif same=='n':
            flag=True
            os.system('cls')
            calculations()
            
calculations()
 


