# # Ask user for their name
# name = input("What's your name? ").strip().title()

# # strip -> Remove whitespace from str and capitalize user's name
# # capitalize -> capitalize first letter of the str
# # title -> capitalize first letter of every word in str
# # Split user's name into first name and last name
# first, last = name.split(" ")


# # Say hello to user
# print(f"hello, {first}!")

# Functions

def main():
  name = input("What's your name? ")
  hello(name)

def hello(to="world"):
  print("hello,", to)

main()











 