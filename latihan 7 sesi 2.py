# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:04:21 2022

@author: Arfiah
"""

nama = input("nama kamu ?")
usia = input("usia kamu ?")
pengeluaran = input("berapa pengeluaran per bulan ?")


if int(pengeluaran)>100000 and int (usia)<20:
    print("ditolak")
elif int(pengeluaran)<100000 and int(usia)<20:
    print("selamat anda dapat subsidi")
else: print("coba lagi")