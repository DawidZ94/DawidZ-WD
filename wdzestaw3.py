#Zadanie1
# A=[1/x for x in range(1,11)]
# print(A)
# B=[2**x for x in range(0,11)]
# print(B)
# C=[x for x in B if x % 4 == 0]
# print(C)
# #Zadanie2
# from numpy import random #zaimportowana biblioteka do macierzy
# M = random.randint(50, size=(4, 4))
# P = [M[x][y] for x in range(0,4) for y in range(0,4) if x == y]
# print(M)
# print(P)
# #Zadanie3
# zakupy = {"piwo": "sztuki",
#         "wino": "sztuki",
#         "tacki": "opakowania",
#         "karkówka": "kg"}
# sztuki = {klucz: wartosc for klucz, wartosc in zakupy.items() if wartosc == "sztuki"}
# print(sztuki)
# #Zadanie4
# def mono(a, b):
#     if a > 0:
#         print("Funkcja rosnie")
#     elif a == b:
#         print("Funkcja stala")
#     else:
#         print("Funkcja maleje")
# mono(5,3)
# #Zadanie5
# def pt(a1,b1,a2,b2):
#     if a1==a2:
#         print("Funkcje rownolegle")
#     elif a1*a2 == -1:
#         print("Funkcje prostopadle")
# pt(2,0,-1/2,4)
# #Zadanie6
# import math
# def kan(a = 2,b = 4, x = 1, y = 2):
#     r = math.sqrt((x - a)**2 + (y - b)**2)
#     print(r)
# kan()
# kan(2,3,4,5)
# #Zadanie7
# import math
# def tpp(x = 3, y = 4):
#     pp = math.sqrt(x**2 + y**2)
#     print(pp)
# tpp()
# tpp(5,12)
# #Zadanie8
# def ca(a1 = 1, r = 1, ile = 10):
#     sn = ((2*a1 + (ile - 1) * r)/2)*ile
#     print(sn)
# ca()
# ca(7,4,20)
# #Zadanie9
# def cg(a1 = 1, q = 1, ile = 10):
#     if q == 1:
#         sn = a1*ile
#         print(sn)
#     else:
#         sn = a1*((1-q**ile)/(1-q))
#         print(sn)
# cg()
# cg(2,2,9)
#Zadanie10
# def zliczzak(** zakupy):
#     liczba = 0
#     for produkt in zakupy:
#         liczba = zakupy.get(produkt) + liczba
#     print(liczba)
# zliczzak(Woda = 6, Platki = 4,Chleb = 1)
# Zadania z pakietami ciężko jest mi panu przedstawić