# This is the program which is generate the random number for the any credentials :--

import random
lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="123456789"
symbol="@#$%&*?\/"
Use_for =lower_case + upper_case + number + symbol
length_for_pass = 8
password = "".join(random.sample(Use_for,length_for_pass))
print("Your Generated Password is :",password)
