# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:34:45 2022

@author: Arfiah
"""

if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x


kangkung = input ("berapa ikat kangkung =")
bayam = input("berapa ikat bayam =")
ikan =input("berapa kilo ikan =")
ayam = input ("berapa ekor ayam =")
uang = input ("uang yg dimiliki =")
total = int(kangkung*5000)+int(bayam*5000)+int(ikan*40000)+int(ayam*30000)
if int(uang) < int(total):
    print("Maaf Uangnya kurang")
elif int(uang) > int(total):
    print("Alhamdulillah terimakasih")
else:
    print("Bhay")
    
              

 
          
          
          
          