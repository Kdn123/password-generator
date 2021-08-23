import string
import random
symb = "!@#$%^&*()<>?:|\/"
# length_paswd = 12
a=("".join(random.sample(string.ascii_uppercase,4))+
"".join(random.sample(string.ascii_lowercase,4))+
"".join(random.sample(string.digits,2))+
"".join(random.sample(symb,2))
)
# a = "".join(random.sample(length_paswd))
print(f"Your Random Password is {a}")
