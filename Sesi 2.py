# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'latihan 1'
x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

if y < x:                            # Falsy
    print('yes')

if x:                                # Falsy
    print('yes')

if y:                                # Truthy
    print('yes')

if 'aul' in 'grault':                # Truthy
    print('yes')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')
    
    
    'latihan 2'
    
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')

'Latihan 3'

if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')  


'latihan 4'

x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

'latihan 5' 

x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


          #  x
#coba-coba

nilaiabsen = int(input("Isi nilai absen anda = "))   
nilaitugas = int(input("isi nilai tugas anda = "))
nilaiuts = int(input("isi nilai uts anda = "))
nilaiuas = int(input("isi nilai uas anda ="))
nilaitotal = (nilaiabsen*0.1)+(nilaitugas*0.2)+(nilaiuts*0.3)+(nilaiuas*0.4)
if nilaitotal >80:
    print ("cie dapat A") 
elif nilaitotal >70 <80:
    print("Cie dapat B")
elif nilaitotal >60 <70:
    print("yahhhh dapat C")
elif nilaitotal >50 <60:
    print("Dodol")     
else: 
    print("Ehehehehe")
    
    
    
