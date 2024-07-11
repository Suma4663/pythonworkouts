import my_module
my_module.printme("hellow cutie")
print(my_module.PI_VALUE)
my_module.sayhello("Suma")
my_module.sayhello("Ratheesh")

print(dir(my_module))

var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
print("my name is %s and age is %d"%("suma",40))

var4="askjksjdfjgjdfj1kz"
print(len(var4))
print(max(var4))
print(min(var4))
print(var4[-1])

l1 = 'WORD'
l2 = list(l1)

l2.insert(3,'L')
print(l2)
l3 = ''.join(l2)
print(l3)

name = "Tutorialspoint"
print("Welcome to %s!" % name)
print("Welcome to {}!".format(name))
print(f"Welcome to {name}!")
print(r"hello\n")

vowels="aeiou"
count=0
for i in name:
    if i in vowels: count+=1

print ("Vowels: ",count)


list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list) # Prints complete list
print (list[0]) # Prints first element of the list
print (list[1:3]) # Prints elements starting from 2nd till 3rd
print (list[2:]) # Prints elements starting from 3rd element
print (tinylist * 2) # Prints list two times
print (list + tinylist) # Prints concatenated lists
list[2]="hello"
print (list)
del list[3]
print (list)

list2 = [2,3,4]
list3=list+list2
list4=list2*3
print(list3)
list4.append(5)
list4.sort()
print(list4)
print(5 in list4)


a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(id(a))
print(id(b))

x=True
print(x)
print(type(x))



helloStr = "hello world"
uppercase_letters = [i.upper() for i in helloStr if i.isalpha()]
print(uppercase_letters)

lst=[1,2,3,4,5]
sqr = [i*i for i in lst if i.is_integer()]
print(sqr)

sqrlmb = [(lambda i:i*i)(i) for i in lst if i.is_integer()]
print(sqrlmb)





