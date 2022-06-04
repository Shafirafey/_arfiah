# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:05:08 2022

@author: Arfiah
"""

harga = input ("Masukkan Harga Buku =")
Jumlah_buku = input ("Jumlah Buku =")
Uang = input ("Masukkan Uang Anda =") 
total = int(harga) * int(Jumlah_buku)
 
if int(Uang) > int(total):
      print ("Bawa Pulang")
elif int(Uang) == int(total):
      print("jangan dibeli")
else:
      print ("pulang")
