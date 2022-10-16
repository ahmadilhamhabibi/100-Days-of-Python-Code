# Dictionary {Key:Value}
# Dictionary {
#   Key1:Value1,
#   Key2:Value2,
#   Key3:Value3
# }

pancasila_dictionary = {
    "Satu" :"Ketuhanan",
    "Dua" : "Kemanusiaan",
    "Tiga" : "Persatuan",
    "Empat" : "Kerakyatan",
}

# mengambil data dari dictionary
print(pancasila_dictionary["Dua"])

# menambah item pada dictionary
pancasila_dictionary["Lima"] = "Keadilan"
print(pancasila_dictionary)

# membuat dictionary kosong
kosong = {}

# menghapus dictionary 
# pancasila_dictionary = {}
# print(pancasila_dictionary)

# mengedit item pada dictionary
pancasila_dictionary["Empat"] = "Kerakyatan dan Permusyawaratan"
print(pancasila_dictionary)

# Looping pada dictionary
for key in pancasila_dictionary:
    print(key)
    print(pancasila_dictionary[key])
