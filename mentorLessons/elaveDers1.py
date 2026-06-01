from cryptography.x509 import name
#1ci-variable(deyisen),2ci gelen value(deyer)
# ad="Aysel"  #string
# yash=20      #int
# qiymet=20.50  #float
# kecmek_Olarmi_Isiqda=False  #boolean
# print( not kecmek_Olarmi_Isiqda)



#
#
# print("Xosh gelmisiniz!,",ad)
#
#
#
#
# print(type(ad))
# print(yash)
# print(type(qiymet))
# print(kecmek_Olarmi_Isiqda)




# istifadecininAdi #olar
# istifadcinin_adi #olar
# istifadcinin-adi # olmaz
# istifadecinin adi #olmaz
# masa5="X"  #OLAR
# 5masa  #olmaz
# @#%&(^$^$^&$ # olmaz



# a=-20
# b=3
# print(a+b)
# print(abs(a+b))
# # print(a-b)
# # print(a*b)
# # print(a**b)
# print(a/b)
# print(round(a/b,2))
# print(a//b)
# print(a%b)




imtahan_bali=90
davamiyyet_bali=75

#
# print(imtahan_bali,davamiyyet_bali)
# print(imtahan_bali==davamiyyet_bali)
# print(imtahan_bali>davamiyyet_bali)


#and her iki sert True - cavab True olsun,1i True 1i False Cavab:False,2si de False cavab False
#or her iki sert True -cavab True,1i True 1i False cavab yene True,2si de False cavab False
# print(imtahan_bali>80 and davamiyyet_bali>80)  #1ci True,True
# print(imtahan_bali>80 or davamiyyet_bali>80)



# ad="Aysel"

# ad=input("Sizin adiniz nedir?")
# soyad=input("Bes soyadiniz nedir?")
#
# print(ad,soyad)
# print("Xosh gelmisiniz",ad,soyad)


# yash=int(input("yashinizi daxil edin"))
# #if else elif  ---sert
# if yash>18:
#     print("vesiqe ala bilersiniz")
# else:
#     print("vesiqe ala bilmezsiniz")


imtahan_bali=int(input("Imtahan baliniz?"))

if imtahan_bali>90:
    print("Elachi")
elif imtahan_bali>80:
    print("zerbeci")
elif imtahan_bali>70:
    print("Adi")
else:
    print("Kesildiz")


