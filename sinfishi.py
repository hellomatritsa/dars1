

##1-m
# a=int(input("son "))
# b=int(input("son "))
# c=int(input("son "))

# if a<b<c or c<b<a:
#     print("O'rtada")
# else:
#     print("O'rtada emas")  

##2-m
# a=int(input("son "))
# b=int(input("son "))
# c=int(input("son "))

# count=0

# if a>0:
#     count+=1
# if b>0:
#     count+=1
# if c>0:
#     count+=1

# print(count)

##3-m

# a=int(input("son "))
# b=int(input("son "))
# c=int(input("son "))

# if a < b  and a<c:
#     print(b+c)
# elif b <a and b<c:
#     print(a+c)
# elif c<a and c<b:
#     print(a+b)

##4-m

# a=int(input("son "))
# count=0

# x=1

# while x<=a:
#     if  a//x:
#         count+=1
   

#     x+=1

# if count == 2:
#     print("Tub son")
# else:
#     print("Tub son emas")

##5-m

# a=int(input("son "))
# b=int(input("son "))

# if a%2 and b%2:
#     print("Toq ")

##6-m

# a=int(input("son "))
# b=int(input("son "))

# if a%2:
#     print(f"{a} Toq")
# if b%2:
#     print(f"{b}  Toq")

##7-m
# a=int(input("son "))
# b=int(input("son "))
# c=int(input("son "))

# if a>0 and b>0 and c>0:
#     print("Musbat sonlar")

##8-m

# a=int(input("son "))

# if a%2==0 and len(str(a))==2:
#     print(f"{a} juft va ikki xonlai son")

##9-m
# a=int(input("son "))

# if a%2 and len(str(a))==3:
#     print(f"{a} toq va uch xonlai son")

##10
# son=int(input("Uch xonali son "))
# a=son%10
# b=son//10%10
# c=son//100

# if a!=b and a!=c:
#     print("bir xil emas")

##11

# import random
# n= random.randint(1,999)

# natija=len(str(n))

# print(f"{n} {natija} xonali son")

##12-m

# son=input("SOn: ")
# b=son%10
# o=son//10%10
# y=sonn//100

# if y<o<b:
#     print("O'sish tartibida")

##fayldagi 1-m

# kino=input("Kino nomi: ")
# yosh=int(input("Yoshingiz: "))

# if yosh <= 12:
#     print(f'{yosh} yoshli foydalanuvchi uchun "Animatsiya" yoki "Oila" janrini tavsiya qilamiz!')
# elif 12 < yosh <18:
#     print(f'{yosh} yoshli foydalanuvchi uchun "Action" yoki "Sarguzasht" janrini tavsiya qilamiz!')
# elif 18<yosh<60:
#      print(f'{yosh} yoshli foydalanuvchi uchun "Drama" yoki "Komediya" janrini tavsiya qilamiz!')
# elif yosh>=60:
#     print(f'{yosh} yoshli foydalanuvchi uchun "Dokumental" yoki "Klassik" janrini tavsiya qilamiz!')

##2-m
# sum=0

# for i in range(3):
#     n=int(input(f"{i+1} -mahsulot narxini kiriitng: "))
#     sum+=n


# if sum>500:
#     print(f"Jami narx: ${sum}\nChegirma: 20%\nYakuniy narx: ${sum*0.8}")
# elif sum>200:
#     print(f"Jami narx: ${sum}\nChegirma: 15%\nYakuniy narx: ${sum*0.85}")
# elif sum>100:
#     print(f"Jami narx: ${sum}\nChegirma: 10%\nYakuniy narx: ${sum*0.9}")
# else:
#      print(f"Jami narx: ${sum}\nChegirma: 0%\n")

##3-m

# harorat=input("Elsiyda harorat kiriting: ")

# while harorat.lower() != "exit":
#     harorat=float(harorat)
#     f=harorat*(9/5)+32

#     if f>85:
#         print(f"{harorat}C ={f:.0f}F. Issiq ")
#     elif 32 < f <=85:
#         print(f"{harorat}C ={f:.0f}F. Yaxshi ")
#     else:
#         print(f"{harorat}C ={f:.0f}F. Muzlash")

#     harorat=input("Elsiyda harorat kiriting: ")

##4-masala

# yosh=int(input("Yoshingiz: "))
# yil=int(input("Necha yildan beri obuna bo'lasiz? "))
# sum=15
# yosh_chegirma=0
# obuna_chegirma=0

# for i in range(1):
#     if yosh >=55:
#         sum= sum*0.8
#         yosh_chegirma=20
        
#         if yil >5:
#             sum=sum*0.85
#             obuna_chegirma=15
#         elif yil >3:
#             sum=sum*0.9
#             obuna_chegirma=10  
#     else:
#         if yil >5:
#             yosh_chegirma=0
#             sum=sum*0.85
#             obuna_chegirma=15
#         elif yil >3:
#             sum=sum*0.9
#             obuna_chegirma=10 



# print("Asosiy narx: $15")
# print(f"Yosh bo'yicha chegirma: %{yosh_chegirma}\nObuna davomiyligi bo'yicha chegirma: %{obuna_chegirma}\nYakuniy narx: ${sum}")


    
##5-m

##5-masala

# while True:
#     parol = input("Parol kiriting: ")

#     katta = False
#     raqam = False
#     maxsus = False

#     if len(parol) < 8:
#         print("Parol juda qisqa.")

#     for belgi in parol:
#         if belgi.isupper():
#             katta = True

#         if belgi.isdigit():
#             raqam = True

#         if belgi in "@#$":
#             maxsus = True

#     if len(parol) >= 8:
#         if not katta:
#             print("Paroldan katta harf yetishmayapti.")

#         if not raqam:
#             print("Paroldan raqam yetishmayapti.")

#         if not maxsus:
#             print("Paroldan maxsus belgi yetishmayapti.")

#     if len(parol) >= 8 and katta and raqam and maxsus:
#         print("Parol kuchli!")
#         break


##6-m

for i in range(1, 4):
    kompaniya = input(f"Kompaniya {i}: ")
    narx = float(input("Narx: "))

    if narx > 100:
        print(f"{kompaniya} aktsiyasi qimmat.")
    elif narx < 50:
        print(f"{kompaniya} aktsiyasi arzon.")
    else:
        print(f"{kompaniya} aktsiyasi o'rtacha.")





































