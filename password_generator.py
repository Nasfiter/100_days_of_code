#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


len_letters = len(letters)
sym_len = len(symbols)
password = []
strong_pasword = []

for letter in range(nr_letters):
    position = random.randint(0, len_letters -1)
    password.append(letters[position])

for num in range(nr_numbers):
    password.append(str(random.randint(0, 9)))

for sym in range(nr_symbols):
    pos = random.randint(0, sym_len -1)
    password.append(symbols[pos])
pasword_len = len(password)

for symbol in range(pasword_len):   # mixing elements in password
    r_chois = random.randint(0, pasword_len -1)
    strong_pasword.append(password[r_chois])
    del password[r_chois]
    pasword_len -= 1


final_pasword = ""
for i in strong_pasword:
    final_pasword += i

print(f"Here is your password: {final_pasword}")
