# # Simple Function
# def greet():
#     print("Hello Ahmad")
#     print("How do you do Ilham?")
#     print("Isn't the waether nice today, Habibi?")

# greet()

# # Function with input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"Isn't the waether nice today, {name}?")

# greet_with_name("Ahmad")
# greet_with_name("Ilham")
# greet_with_name("Habibi")

# Function with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the waether nice today in {location}?")

greet_with("Ahmad", "Surabaya")
greet_with(location="Rumah", name="Habibi")