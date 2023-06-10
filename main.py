import random
import string

password = string.ascii_letters+string.punctuation+string.digits

length_password = int(input("Please input length of password: "))

x = "".join(random.sample(password, length_password))

print("Random Password : "+x)
