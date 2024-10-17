# """ 1-mashq """

# yosh = int(input("Yoshingizni kiriting: "))
# yili = 2024 - yosh
# print(yili)
# hisob = yili + 10
# print(hisob)



""" 2-mashq """

# "1"
# from math import sqrt
# amal1 = (sqrt(9876) + 23)
# print(amal1)
# amal2 = (amal1**2) / 21
# amal3 = round(amal2, 3)
# print(amal3)


# "2"
# x = int(input(" X-ni kiriting: "))
# y = 4*(x-3)**5-7*(x-3)**3+2
# print(y)


# "3"
from random import randrange
# son1 = int(input("1-chi sonni kiriting: "))
# son2 = int(input("2-chi sonni kiriting: "))
# print(randrange(son1, son2))


# "4"
# soni1 = int(input("1-chi son kiritaylik: "))
# soni2 = int(input("2-chi son kiritaylik: "))
# soni3 = int(input("3-chi son kiritaylik: "))
# soni4 = int(input("4-chi son kiritaylik: "))

# hisabun = soni1**soni2
# hisabun2 = hisabun / soni3
# print(round(hisabun2), soni4)


# "5"
# liwun = (67365 / 32)
# liwun2 = (round(aliwun), 2)
# liwun3 = (sqrt(liwun2**3))




# """ Sonlarning turlari """

# x = 1 # int
# y = 2.8 # float
# z = 1j # complex


# print(x)
# print(type(z))




# """ O'nlik son turlari """

# xy = 35e3
# zy = 83e4
# yz = 55e5


# print(yz)
# print(type(yz))


# """ Sonni darajaga ko'tarish """

# from math import pow
# print(pow(5, 5))   # pow-power - darajaga ko'tarish


# f = 5**5
# print(f)



# """ Ildizdan chiqarish """

# d = 16

# from math import sqrt

# print(sqrt(d))



# """ Sonni yaxlidlash """

# print(round(5.555, 2))
# print(round(



# """ Random """
# import random
# print(random.randrange(1, 11))




# """ Ko'p xonali sonlar """

# wor = 546_454_581
# zakon = 493_123_744

# print(wor)
# print(zakon)



# """ Bir vaqtning o'zida 5-6 o'zgaruvchi yartish """

# o,k,m = 4 , -4 , 9 
# print(o, k , m)


# """ Butun sonlari """
# l = 5    # int
# v = 3.56  # 
# q = "aliwa"         


""" 1-mashq """


# radius = int(input("Aylananing radiusiini kiriting: "))

# pi = 3.14

# s = 2*pi*radius

# print(s)



# """ 2-mashq """

# radius2 = int(input("Aylananing radiusiini kiriting: "))

# pi = 3.14

# syusu = pi*radius2**2

# print(syusu)



# """ 4-mashq """


# a = int(input("Son kiriting: "))
# b = int(input("Son kiriting: "))

# q = a+b
# w = a-b
# e = a*b
# r = a/b
# t = a**2
# y = a**3
# u = b**2
# i = b**3
# p = (a+b)/2



# # """ Bir ro'yxatni ikkinchi ro'yxatga qo'shish """

# # fruits = ["Apple", "Banana", "Cherry"]

# # tropic_fruits = ["Mango", "Pineapple", "papaya"]

# # fruits.extend(tropic_fruits)

# # print(fruits)

# # print(tropic_fruits)



# # """ "Del' indexi bo'yicha o'chiradi """

# students = ["Muhammadyusuf", "Alisher", "Xojiakbar"]

# # print(students)

# # del students[0]

# # print(students)


# # """ 'Remove' qiymati bo'yicha o'chiradi """

# # students.remove("Alisher")

# # print(students)


# """ Pop  """


# # students.pop(2)




# # """ Len() """

# # family = ["father", "Mother", "Me"]


# # print(f"Bizning oilada {len(family)}-ta odam yashaydi! ")
# # print(f"Ular {family[0]}, {family[1]} and {family[2]}")






# # """ List """

# # country = list() # ro'yxat yaratish





# # """ Clear """

# # students.clear()





# """ Vazifa-1 """

# aktyorlar = ["Ali", "Vali", "Sali"]

# xonandalar = ["Guli", "Suli", "Duli"]


# del aktyorlar[0]

# xonandalar.remove("Guli")

# aktyorlar.pop(1)


# print(aktyorlar)
# print(xonandalar)





# aktyorlar.append("G'ani")
# aktyorlar.append("Gani")
# aktyorlar.append("Qani")


# insonlar = []

# insonlar.extend(aktyorlar)
# insonlar.extend(xonandalar)

# print(insonlar)




# """ Vazifa-2 """

# friends = []

# friends.append("Ali")
# friends.append("Vali")
# friends.append("Sali")
# friends.append("G'ali")
# friends.append("Kal")
# friends.append("Tepa kal")





# friends.remove("Ali")
# friends.remove("Vali")
# friends.remove("Sali")
# friends.remove("Kal")



# # friends.insert(0, "Sakom")

# # friends.insert(-1, "Vakom") 


# # sonlar = list(range(12, 34))

# # print(sonlar)


# # """ Ro'yxatdan nusxa olish """

# # son = list(range(50, 100))
# # print(son)


# # son2 = son[60:80]

# # print(son2)





# # family= []

# # family.append(input("Otangizni ismini kiriting: "))

# # family.append(input("Onangizni ismini kiriting: "))

# # print(f"Siz oilada {len(family)} - tasiz. Ular {family[0]}, {family[1]}")





# # """ Sort """

# name = ["Ali", "Vali", "Sali", "Qani"]

# # print(name)
# # name.sort()
# # print(name)
# # name.sort(reverse=True)
# # print(name)


# """ Sorted """

# print(name)
# print(sorted(name))
# print(sorted(name, reverse=True))


# """ Reverse """

# country = ["Uzbekistan", "Afrika", "Afganistan"]

# print(country)


# country.reverse()

# print(country)




# """Don don ziki """
# from random import randrange
# manbalar = ["Tosh", "Qaychi", "Qog'oz"]
# print("Dondon ziki o'yinimizga xush kelibsiz bo'lmasa boshladik! ")

# print(randrange)

# manba = int(input("Manba kiriting: "))




# """ 'Max' 'Min' 'Sum' """

# number = list(range(1, 45))

# print(max(number))
# print(min(number))
# print(sum(number))



# number2 = [1, 45, -54, 34, 56]
# number2.sort()
# print(number2)
# print(f"Bizning ro'yxatdagi eng katta son {max(number2)} va eng kichigi {min(number2)}")





""" 1-mashq """

# davlatlar = ["Uzbekistan", "Russia", "America", "Europa", "Germany"]

# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# davlatlar.sort(reverse=True)



""" 2-mashq """

# sonlar = list(range(120, 1200, 2))

# print(sum(sonlar))
# print(max(sonlar) - min(sonlar))
# print(len(sonlar))
# print(sonlar[:20])
# print(sonlar[250:270])
# print(sonlar[450:490])





""" 3-mashq """

# taomlar = ["Sho'rva", "Osh", "Norin"]
# nonushta = []
# nonushta = taomlar.copy()
# print(nonushta)
# nonushta.append("Non")
# nonushta.append("Choy")
# jami = []
# jami.extend(nonushta)
# jami.extend(taomlar)
# print(jami)










""" For """

# ismlar = ["Ali", "Sali", "Vali", "G'ani", "Qani"]

# for ism in ismlar:
#     print(f"Salom {ism}, Nima gaplar")

# print("Xurmat bilan Mr.Xojake")






# ism = "Aziz bacha"
# for i in ism:
#     print(i)


# for son in range(1, 11):
#     print(son)


"10.10.2024"

"topic: Lugat"

" mashq 1 "

# lugat = {"olma":"apple",
#          "nok":"pear",
#          "tarvuz ":"watermelon",
#          "telefon":"mobile phone",}
# soz_kirit = input("Biror soz kirit:  "  )
# for  k , v in lugat.items():
    