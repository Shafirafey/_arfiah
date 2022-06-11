# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:13:11 2022

@author: Arfiah
"""

#Sesi 3
#latihan-1
def my_function(p, l):
    "Function untuk mengitung luas"
    print(p * l)
my_function(2,4)

#latihan-2
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

#latihan-3
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)

#latihan-4
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = ([10,20,30]);
changeme( mylist );
print("Values outside the function: ", mylist)

#latihan-5

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)


#Trial


# Now you can call changeme function
mylist = [10,20,30];
mylist = [20,40,80];
changeme( mylist );
print("Values outside the function: ", mylist)

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print("Values inside the function: ", mylist)
   return


#Latihan-6

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme(6)

#latihan-7

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme(str = 1234)
printme(str="123")

#latihan-8
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=24, name="arfiah" )

#trial
# Function definition is here
def printinfo( name, n1, n2, n3, n4, Nakhir ):
   "This prints a passed info into this function"
   Nakhir = (n1*0.1)+(n2*0.2)+(n3*0.3)+(n4*0.4)
   print("Name: ", name)
   print("Age: ", n1)
   print("Age: ", n2)
   print("Age: ", n3)
   print("Age: ", n4)
   print("Age: ", Nakhir)
   return;

# Now you can call printinfo function
printinfo( name ="Arfiah", n1=100, n2=90, n3=80, n4=95, Nakhir=0 )



#Contoh
# Function definition is here
def printinfo( name, nilai1,nilai2,nilai3,nilai4, nakhir):
   "This prints a passed info into this function"
   
   nakhir = (nilai1*0.1)+(nilai2*0.2)+(nilai3*0.3)+(nilai4*0.4)
   
   print("Name: ", name)
   print("nilai 1: ", nilai1)
   print("nilai 2: ", nilai2)
   print("nilai 3: ", nilai3)
   print("nilai 4: ", nilai4)
   print("nilai akhir: ", nakhir)

   return;

# Now you can call printinfo function
printinfo( name='a', nilai1=100, nilai2=80, nilai3=75, nilai4=88, nakhir=0)

#Latihan-9
# Function definition is here
def printinfo( name, age = 26 ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )


# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )

def printinfo(name, age, gender = "Female", Education = "Sarjana"):
    print("Name : ", name)
    print("Age : ", age)
    print("gender : ", gender)
    print("Education : ", Education)
printinfo(name="Arfiah",age="24",gender="Female",Education="Sarjana")

#Latihan-10
# Function definition is here
def printinfo( arg1, *vartule ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartule:
      print(var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )


#Latihan-11

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

#def sum(arg1, arg2):
   # arg1 + arg2
    
# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))


#Trial
# Function definition is here
sum = lambda arg1, arg2, arg3, arg4, arg5: arg1 + arg2 + arg3 + arg4 + arg5;

#def sum(arg1, arg2):
   # arg1 + arg2
    
# Now you can call sum as a function
print("Value of total : ", sum( 10, 20, 20, 15,0 ))
print("Value of total : ", sum( 20, 20, 30,20,25 ))




#Latihan-11
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    total2 = total + arg1
    print("Inside the function : ", total)
    return total2

# Now you can call sum function
total = sum(10, 20)
print("Outside the function : ", total)



#Contoh
total = 0; 

def sum( arg1, arg2 ):

   total = arg1 + arg2; 
   print("Inside the function local total : ", total)
   return total;

def min():
    

    sum( 10, 20 );
print("Outside the function global total : ", total)

#cONTOH

jumlahKucing = 20

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing
jumlahKelinci()
jumlahHewan()
print(jumlahHewan())
print(jumlahKelinci())





















