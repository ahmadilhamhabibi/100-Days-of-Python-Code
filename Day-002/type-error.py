num_char = len(input("What is your name? "))

# print("Your name has " + num_char + " characters") ==> type error "can only concatenate str (not "int") to str"

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters")

# Type convertion

a = str(123)
print(type(a))

b = float(123)
print(type(b))