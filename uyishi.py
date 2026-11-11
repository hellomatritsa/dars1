##1-masala

# n=int(input("Son kiriting: "))
# sum=0

# for i in range(1, n+1):
#     sum+=i**i
# print(sum)

##2-masala

# yosh=29

# for i in range(201):
#     print(i)
#     if i==yosh:


#         print("Bu sizning yoshingizga teng!")

##3-masala

# for i in range(100, 1000):
#     birlik=i%10
#     onlik=i//10%10
#     yuzlik=i//100

#     if birlik == onlik or onlik == yuzlik:
#         print(i)

##4-masala
import random

n=int(input("Nechchigacha: "))

son=random.randint(1,n)

for i in range(3):
    raqam=int(input("Nechchi: "))
    if son == raqam:
        print("winner")
        break
    

print("looser")    

##5-File dagi masalalrning barchasi sinf ishida



