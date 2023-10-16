# print("meow")
# print("meow")
# print("meow")

## While

# i = 3 # -> counter
# while i != 0:
#   print("meow")
#   i = i - 1

## For Loop

# for _ in range(3):
#    print("meow")

# print("meow\n" * 3, end="")

# while True:
#   n = int(input("What's n? "))
#   if n > 0:
#     break

# for _ in range(n):
#   print("meow")

def main():
  number = get_number()
  meow(number)

def get_number():
   while True:
      n = int(input("What's n? "))
      if n > 0:
         break
   return n

def meow(n):
   for _ in range(n):
      print("meow")  


main()
