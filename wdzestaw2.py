#Zadanie1
#tekst = input("Wpisz tekst a policze ile jest spacji: ")
#print("Policzylem ze w tym tekscie mamy " + str(tekst.count(' ')) + " spacji")
#Zadanie2
# import sys
# x = sys.stdin.readline()
# y = sys.stdin.readline()
# sys.stdout.write(str(int(x)*int(y)))
#Zadanie4
# x = input("Podaj Liczbe ")
# x = int(x)
# if int(x) < 0:
#     x *= -1
# print(f"Wartosc bezwzgledna z podanej liczby wynosi {x}")
#Zadanie5
# a = int(input("Podaj a "))
# b = int(input("Podaj b "))
# c = int(input("Podaj c "))
# if  a > 0 and a < 10:
#     if a > b or b > c:
#         print(f"Warunki spelnione")
#     else:
#         print(f"Warunki niespelnione")
# else:
#     print(f"Warunki niespelnione")
#Zadanie6
# for x in range(0, 101, 5): #w poleceniu nie jest napisane do kiedy wyswietlac liczby podzielne przez 4
#     print(str(x))
#Zadanie7 - Nie okreslona liczba razy ile petla ma sie wykonac
# while True:
#      x = int(input("Podaj liczbe a policze jej kwadrat "))
#      print(str(x*x))
#      br = input ("Jezeli to ostatni kwadrat ktory chcesz policzyc wpisz t ")
#      if br == "t":
#          break
#Zadanie8
# lista = []
# while 1:
#     x = int(input("Podaj liczbe do dodania do listy "))
#     lista.append(x)
#     print(lista)
#     br = input ("Jezeli to ostatni element listy wpisz t ")
#     if br == "t":
#          break
#Zadanie9
# x = (input("Podaj liczbe a policze sume jej cyfr "))
# l = len(x)
# c = 0
# suma = 0
# while c <= l-1:
#     suma += int(x[c])
#     c+=1
# print(f"Suma cyfr to {suma}")
# #Zadanie10
# x = int(input("Podaj wysokosc wiezy nie wiecej niz 10 "))
# if x > 10 or x < 1:
#     exit()
# for i in range(1, x+1, 1):
#     print("A"*i)
#Zadanie11
# n = int(input("Podaj wysokosc diamentu nie wiecej niz 9 nie mniej niz 3 "))
# if n > 9 or n < 3:
#     exit()
# mid = int((n/2+1))
# for x in range (1, mid+1, 1):
#     if x == mid and n%2 == 0: #Bez tego nie działa dla liczb parzystych - nie wiem jak to lepiej zapisac
#         break
#     else:
#         print((mid-x)*" " + x*"o"+(x-1)*"o")
# for x in range (1, mid, 1):
#     print((x)*" " + (mid-x)*"o"+(mid-x-1)*"o")
#Zadanie12
# for n in range (0, 11, 1):
#     if n == 0:
#         print("*", end = "")
#     else:
#         print(str(n), end = "")
#     for x in range (1, 11, 1):
#         if n == 0:
#             print(" | "+str(x), end = "")
#         else:
#             print(" | "+str(x*n), end = "")
#     print(" |")
#Zadanie14
# import math 
# n = int(input("Podaj liczbe a policze jej pierwiastek "))
# try:
#     math.sqrt(n)
# except ValueError:
#     print("Nie mozna wyliczyc pierwsiasta z liczby ujemnej")
#Zadanie15
# try:
#     n = int(input("Podaj liczbe "))
# except ValueError:
#     print(" To co podales to nie liczba")




