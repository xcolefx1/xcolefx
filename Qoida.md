
### Kod misoli:

```python
# Foydalanuvchidan ikkita son kiritishni so'rash
birinchi_son = float(input("Birinchi sonni kiriting: "))
ikkinchi_son = float(input("Ikkinchi sonni kiriting: "))

# Kiritilgan sonlarni chiqarish
print("Siz kiritgan birinchi son:", birinchi_son)
print("Siz kiritgan ikkinchi son:", ikkinchi_son)
```

### Kodni qanday ishlatish:

1. **`input()` funksiyasi**: Bu funksiya foydalanuvchidan ma'lumot oladi. Foydalanuvchi kiritgan har qanday ma'lumot, satr (string) turida keladi.
   
2. **`float()` funksiyasi**: Foydalanuvchidan olingan satrni real son (float) turiga o'giradi. Agar foydalanuvchi butun son kiritsa, bu ham mumkin. 

3. **O'zgaruvchilar**: 
    - `birinchi_son` - foydalanuvchi kiritgan birinchi sonni saqlaydi.
    - `ikkinchi_son` - foydalanuvchi kiritgan ikkinchi sonni saqlaydi.

4. **Natijani chiqarish**: `print()` funksiyasi yordamida foydalanuvchi kiritgan sonlarni chiqaramiz.

### Quydagi nuqtalarga e'tibor bering:
- Agar foydalanuvchi son kiritmasa yoki noto'g'ri ma'lumot kiritgan bo'lsa, dastur xato beradi. Buni oldini olish uchun qo'shimcha tekshirish funksiyalarini kiritish mumkin.

Agar sizda boshqa savollar yoki qo'shimcha misollar kerak bo'lsa, bemalol so'rang!

""" Tug'ilgan yil """
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        if int(yosh) >= 10 and int(yosh) <= 110:
            print(f"Siz {2023-int(yosh)}-yilda tug'ilgansiz")
        else:
            print("Siz noto'g'ri yosh oralig'ini kiritingiz")
    elif yosh == "exit":
        print("Dastur tugadi")
        break
    else:
        print("Siz son kiritmadingiz !!!")