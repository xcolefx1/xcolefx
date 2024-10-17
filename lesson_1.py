
XBX = ["XBX LEGENDA"]


print(f"{XBX}")


""" Matini qirqish """
# b = "Hello, Xojake"
# print(b[:5])

# b = "H'ello, Xojake"
# print(b[:5])

# b = "Hello, Xojake"
# print(b[-6:-5])


# """ Replace() """
# a = "Hello va aaa oooo aaa"
# print(a.replace("a", "o")) 


# """ Split() """
# a = "Hello va aaa oooo aaa"
# print(a.split("a"))



# /n yangi qator
# /t tab tashlab beradi
# /b boshliqni yoqotib beradi
# /r yangi qator
# '   ' begisi uchun
# "   " belgisi uchun






# """ Append """


# students = ["ali", "maruf", "bahrom"]
# # print(students)

# # students.append("vali")
# # students.append("g'ani")
# # print(students)

# """ Inserttt """

# students.insert(2, "aliw")
# print(students)




# ismlar = ["Ali", "Vali", "Oyna", "Sara", "Bobur"]

# for ism in ismlar:
#     print(f"{ism} nima gap")





# sonlar = [1, -1, 1.5]

# for son in sonlar:
#     print(f"{son+son}")


# for son in sonlar:
#     print(f"{son-son}")

# for son in sonlar:
#     print(f"{son/son}")















""" 1-mashq """

# kinolar = []

# miqdor = int(input("Nechta sevimli kinoyingiz bor: "))


# for kino in range(miqdor):
#     kinolar.append(input(f"{kino+1} - chi kino nomini kiriting: "))

# print(f"Siznig sevimli kinlaringiz: {kinolar}", end=", ")




# """ 2-mashq """

# ism = []

# kimdirlar = int(input("Bugun nechchi kishi bilan suhbatlashdingiz: "))

# for kim in range(kimdirlar):
#     ism.append(input(f"{kim+1} - chi gaplashgan odamingizni ismini kirting: "))

# print(f"Siz bugun quyidagi insonlar bilan suhbat qurdingiz ular: {ism}", end=", ")




# """ 3-mashq """

# sonlar = list(range(9, 100, 2))

# print(sonlar)


# for son in sonlar:
#     print(f"{son**2} - kvadrat")
#     print(f"{son**3} - kubi")
#     print(f"{son-1} - 1 - ga kichik")
#     print(f"{son+3} - 3 - ga katta")


















# """ If-Else """

# a = 4
# b = 3

# if a > b:
#     print(a)
# else:
#     print(b)






# """ Tenglik '==' """

ismlar = ["Ali", "Vali", "Sali", "G'ani"]

# for ism in ismlar:
#     if ism == "Vali":
#         print(f"Salom {ismlar[1]} ")
#     else:
#         print(f"Nima gap {ism}")




# for ism in ismlar:
#     if ism != "Ali":
#         print("NIMA GAp")
#     else:
#         print("IShlar yaxshimi")



# """ Elif """

# sonlar = [1,2,3,4,5,6,7,8,9,10]

# for son in sonlar:
#     if son < 5:
#         print(f"{son} - 5 dan kichik! ")
#     elif son == 5:
#         print(f"{son} - 5ga teng! ")
#     else:
#         print(f"Bu sonlar {son} - 5dan katta")





"""
== - teng
!= - teng bolmasa
> - katta
< - kichik
>= - katta yoki teng bolsa
<= - kichik yoki teng bolsa
or - yoki
and - va

"""








# son = int(input("1-chi sonni kiriting: "))
# son2 = int(input("2-chi sonni kiriting: "))

# if son > son2:
#     print(f"{son}  {son2} - dan katta")
# elif son < son2:
#     print(f"{son} - {son2} -  kichik")
# elif son == son2:
#     print("Bir biriga teng")



# for ism in ismlar:
#     if ism == "Ali":
#         print(f"Salom Ali")
#     elif ism == "Sali":
#         print(f"salom Sali")
#     else:
#         print(f"{ism} tinchmi")







# mevalar = ["Banan", "Ananas", "Gilos", "Bexi", "Sabzi", "Kartoshka"]



# for meva in mevalar:
#     if meva != "Sabzi" and  "Kartoshka":
#         print(f"{meva.capitalize()}")
#     else:
#         print(f"{mevalar[4].upper()} {mevalar[5].upper()}")








# son = int(input("Son kiriting: "))

# if son > 0:
#     print(f"{son} - musbat")
#     if son%2 == 0:
#         print(f"{son} - juft")
#     else:
#         print(f"{son} - toq")
# elif son < 0:
#     print(f"{son} - manfiy")





















# son = int(input("Son kiriting: "))


# if son % 2 == 0 and son >= 1:
#     print(f"{son} - juft va musbat")
# elif son % 2 == 1 and son <= -1:
#     print(f"{son} - toq va manfiy")
# elif son % 2 == 0 and son < 0:
#     print(f"{son} - juft va manfiy")
# elif son % 2 == 1 and son >= 1:
#     print(f"{son} - toq va musbat")



# ism = input("Ismingizni kiriting: ")
# baxo = int(input("Maktabdagi baxoyingizni kiriting: "))

# if baxo == 0 or baxo == 1:
#     print("Juda yomon")
# elif baxo == 2:
#     print("Qoniqarsiz")
# elif baxo == 3:
#     print("Qoniqarli")
# elif baxo == 4:
#     print("YAxshi")
# elif baxo == 5:
#     print("BArakalla")
# else:
#     print("Xato")
















# ball = int(input("Imtihondan olgan balingizni kiriting: "))

# if  0 <= ball <=40:
#     print(f"Sizning natijangiz juda yomon!")
# elif  41 <= ball <=60:
#     print(f"Sizning natijangiz qoniqarli!")
# elif  61 <= ball <=80:
#     print(f"Sizning natijangiz yaxshi!")
# elif  81 <= ball <=99:
#     print(f"Sizning natijangiz udar!")
# elif ball == 100:
#     print("Udar cotki!")
# else:
#     print("Xato natija kiritildi! ")






# from math import sqrt

# sonlar = list(range(201, 500, 2))

# for son in sonlar:
#     if 200 <= son <= 300:
#         print(f"{son} - 4 darajasi - {son**4} - ga teng! ")
#     elif 350 <= son <= 400:
#         print(f"{son} - ning iliz ostisi {sqrt(son)} - ga teng! ")
#     elif 420 <= son <= 480:
#         print(f"{son} - 3.5 ga bolingani {son/3.5} - ga teng, uch xona yaxlitlangani {round(son, 3)} - ga teng")
#     elif 480 <= son <= 500:
#         print(f"{son} - 6 darajasi - {son**6} - ga teng! ")









ball = int(input("Imtihondan olgan balingizni kiriting: "))

if  0 <= ball <=20:
    print(f"Sizning natijangiz juda yomon!")
elif  21 <= ball <=35:
    print(f"Sizning natijangiz qoniqarli!")
elif  36 <= ball <=45:
    print(f"Sizning natijangiz yaxshi!")
elif  46 <= ball <=49:
    print(f"Sizning natijangiz udar!")
elif ball == 50:
    print("Udar cotki!")
else:
    print("Xato natija kiritildi! ")








# savat = []
# bori = []
# yogi = []
# mahsulotlar = ["olma", "non", "choy", "bexi", "nok", "uzum"]

# print(f"Assalomu aleytkum do'konimda bor narsalar , Ular {mahsulotlar}")

# nectaligi = int(input("Nechta narsa harid qilmoqchisiz: "))

# for x in (range(nectaligi)):
#     savat = input(f"{x+1} - chi mahsulot nomini kiriting: ")
#     if savat  in mahsulotlar:
#         bori.append(savat)
#     else:
#         yogi.append(savat)



# print(f"Bizda bor mahsulotlar {bori}")

# print(f"Bizda yo'q mahsulotlar {yogi}")





# saud abdulwahed



















""" Tub son topuvchi dastur """
