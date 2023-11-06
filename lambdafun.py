# Positional arguments
arithmetic = lambda x, y: (x * y , x / y)
print(arithmetic(5, 10))  
#output (50,0.5)

#if else
number = lambda age : "eligible for voting " if age >= 18 else "not eligible"
no = number(int(input("enter age")))
print(no)
# enter age 22
#eligible for voting

#Default Arguments
power = lambda x, y=2: x ** y
print(power(3)) 
print(power(3, 3)) 

min = (lambda a , b=10 : a if(a < b) else b) #(50,60)#Can Put here also.
print(min (50,60))

#Keyword Arguments
arithmetic1 = lambda a,b,c : (a+b+c)
print(arithmetic1(a=10,b=20,c=30))



# Variable length with positional arguments

args = lambda *a:a
print(args(20+1,22,23))
     
     
# Variable length with kewords argument:
args1 = lambda **ab:ab
print(args1(a=10,b=20,c=30))



