#funksiya:
#
# def topla(a,b):
#     return a+b
#
# print(topla(5,10))

# def saheni_hesabla(en,uzunluq):
#     sahe=en*uzunluq
#     return sahe
#
# netice=saheni_hesabla(3,4)
# print(netice)


# def ad_soyad(ad,soyad):
#     return f"{ad} {soyad}"
#
# print(ad_soyad("Eli","Eliyev"))

# eded=int(input("Eded daxil edin:"))
# if eded%2==0:
#     print("Cut")
# else:
#     print("Tek")

    #-------------------------
# def tek_yoxsa_cut(eded):
#     if eded%2==0:
#         return "Cut"
#     else:
#         return "tek"
#
# print(tek_yoxsa_cut(42))


#
# def parolu_yoxla(parol):
#     if len(parol)>8:
#         return "ugurludur"
#     else:
#         return "ugursuzdur"
#
# print(parolu_yoxla("gulnar123"))
# print(parolu_yoxla("1232"))


# def enBoyukEded(a,b,c,d):
#     return max(a,b,c,d)
#
# print(enBoyukEded(1,2,3,4))



#
#
#
#
# def hava_yoxla(sheher):
#     return f"{sheher} sheherinde hava 25 derecedir"
#
#
# model=genai.GenerativeModel(
#     model_name="gemini-flash-latest",
#     tools=[hava_yoxla]
# )
#
# chat=model.start_chat(enable_automatic_function_calling=True)
#
# cavab=chat.send_message("Bakida hava necedir?")
# print(cavab.text)