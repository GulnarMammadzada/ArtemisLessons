# meyveler=["alma","armud","banan","alma"]
# meyveler2=("alma","armud","banan","alma")
# meyveler3={"alma","armud","banan","alma"}
#
# print(meyveler)
# print(meyveler2)
# print(meyveler3)

# a=set()
# print(type(a))



# istirak = ["Anar", "Günel", "Anar", "Nicat", "Günel", "Anar", "Fidan"]
#
# a=set(istirak)
# print(a)


# hobiler = {"oxumaq", "idman", "musiqi"}
# hobiler.add("proqlamlasdirma")
# hobiler.remove("oxumaq")
# print(hobiler)



# meyveler={"alma","armud","banan","alma"}
#
# if "alma" in meyveler:
#     print("Alma var")


# sinif_A = {"Anar", "Günel", "Nicat"}
# sinif_B = {"Günel", "Fidan", "Ramin"}
#
# print(sinif_A | sinif_B)
# print(sinif_A & sinif_B)
# print(sinif_B - sinif_A)

#| & -



# telebe={
#     "name":"Ali",
#     "Yash":20,
#     "email":"test"
# }
# telebe.update({"Yash":23})
# telebe.pop("Yash")
# telebe.popitem()
# telebe.clear()
# print(telebe.items())
# print(telebe.get("name"))
# print(telebe.get("Yash"))



metn = "Bu gün hava çox günəşlidir."
tokenler = metn.split()

print(tokenler)
# Çıxış: ['Bu', 'gün', 'hava', 'çox', 'günəşlidir.']