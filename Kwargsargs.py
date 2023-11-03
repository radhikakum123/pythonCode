def keywords(a,b,*,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
    
keywords(10,11,c=12,d=13)

def defualt_args(a,b=5,c=6):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    
defualt_args(3,6,8)

#args vs kwargs

def args(*a):
    for element in a:
        print(element)
        
args(32,34,45,56)

def kwargs(**b):
    for element in b.items():
        print(element)

kwargs(a="15",b="05",c="65")

#positional 

def positional(a,b,/,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
    
positional(10,11,c=23,d=65)

#keywords

def keywords(a,b,*,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
    
keywords(100,119,c="radhika",d="kumbhojkar")    
