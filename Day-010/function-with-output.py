# function with output

def format_name(f_name, l_name):
    """(Menambahkan docstring atau keterangan pada function)
    Fungsi ini akan mengembalikan nama depan dan nama belakang kemudian akan diformat menjadi Title Case"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("AHMAD", "habibi"))


# function with multiple output

def format_name(f_name, l_name):
    if f_name == "" or l_name == "" :
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "),
input("What is your last name? ")))