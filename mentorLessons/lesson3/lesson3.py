#for
#while


# meyve="alma"
#

#
# adlar=["Ali","Aynur","Fidan"]
#
# for ad in adlar:
#     print(ad)
#
# for index,ad in enumerate(adlar,start=1):
#     print(index,ad)



# for i in range(-14,-6):
#     print(i)


# reqem=2
#
# while reqem<5:
#     print(reqem)
#     reqem+=2     #reqem=reqem+1


# for i in range(1,11):
#     if i%2==0:
#         print(i)


# ededler = [3, 0, 7, 0, 2, 0, 9]
#
# for eded in ededler:
#     if eded==0:
#         continue
#     print(eded)
#
# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print(i)

# limit=30
#
# for i in range(1,limit+1):
#     if i%5==0:
#         print(i)


# cem=0
# qiymetler = [2, 5, 3]
#
# for i in qiymetler:
#     cem=cem+i
#     print(cem)

limit=int(input("reqem daxil edin:"))
cem=0

for i in range(1,limit+1):
    if i%2==0:
        cem=cem+i
        print(cem)

        #limit=4  (1,5)--1,2,3,4