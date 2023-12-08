s="viraj"
print(s,len(s))
#+ve indexing
print(s[2])
#-ve indexing
print(s[-1])
#slicing
print(s[:])
print(s[1:3])
print(s[:3])
print(s[2:5])
print(s[::1])
print(s[::])
print(s[::-1])
print(s[0::-1])
print( s[300:])
print(s[1:3:-1])
print(s[1:-5:-1])
print(s[::2])
addr = 'Near Rest house Patan 455677'
print(addr[-6:])
a="amitabh bachchan"
print(a,len(a))
print(a[2],a[-3])
#amit ,amitabh ,bachchan,chan,mit,abh,bh ba,chch
print(a[0:4])
print(a[0:7])
print(a[7:16])
print(a[11:14])
print(a[1:4])
print(a[4:7])
print(a[4:6])
print(a[5:10])
print(a[10:14])
print(a[-5:-2])

# Methods of a string
b= "radhika kumbhojkar"
print(b.capitalize())
print(b.title())
print(b.upper())

d="rAdhIka"
print(d.swapcase())
print(d.casefold())

r="--radhika--"
e=" radhika"
print(r.strip('-'))
print(e.strip( ))

g= "i am radhika Kumbhojkar"
print(g.split())
 
ip="756.252.14.14"
print(ip.split('.'))


# Convert list fo string to str
# use join() method
n = ['198', '162', '12', '3']
print('.'.join(n))

f = ['I','am','Radhika']
print(' '.join(f))
c = '    198.162.12.3   '
print(c.strip())
u = '198.162.12.3'
print(u.split('.'))
print(u.replace('.','-'))
print( '-'.join(u.split('.')))