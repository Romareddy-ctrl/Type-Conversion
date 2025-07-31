#type conversions

#int to float,and string
num=27
print(float(num))
print(str(num))


#float to int,str
num=24.0
print(int(num))
print(str(num))
      
#string to int,list,tuple,set
s1='12345'
s2='123abcd12'
print(int(s1))
print(list(s2))
print(tuple(s2))
print(set(s2))

#list to str,set,tuple
lst=[1,2,3,'a',1,'romareddy']
print(str(lst))
print(set(lst))
print(tuple(lst))

#list of tuples of dictionary
l=[('a',1),('b',2),('c',3)]
print(dict(l))

#set to string,list,tuple
s={1,2,3,'abc','reddy'}
print(list(s))
print(str(s))
print(tuple(s))

#tuple to list,set
t=(1,2,3,'hi','hello',1,2)
print(list(t))
print(set(t))
