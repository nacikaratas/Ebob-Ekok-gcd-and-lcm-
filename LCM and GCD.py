# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 18:53:46 2022

@author: Naci Karataş
"""

#Ebob-Ekok bulan program

def ebob(a,b):
    if a == b:
        return a
    elif a > b:
        return ebob(a-b,b)
    else:
        return ebob(a,b-a)
def ekok(a,b):
    return a*b//ebob(a,b)

sayi1 = int(input("1.sayıyı giriniz:"))
sayi2 = int(input("2.sayıyı giriniz:"))

print("Ebob:",ebob(sayi1,sayi2))
print("Ekok:",ekok(sayi1,sayi2))