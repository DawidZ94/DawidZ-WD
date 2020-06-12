#zad1
# plik = open("rakor.txt","w")
# for x in range(0,21,1):
#     if x % 4 == 0:
#         plik.write(str(x))
#         plik.write("\n")
# plik.close()
# #zad2
# plik = open("rakor.txt","r")
# liczby = plik.readlines()
# plik.close()
# print(liczby)
#zad3
# with open("dwojka.txt", "w") as plik:
#     plik.write("linijka1")
#     plik.write("linijka2")
#     plik.write("linijka3")
# with open("dwojka.txt", "r") as plik:
#     for linia in plik:
#         print(linia, end="")