import string
import random
def opp(s, op):
	k = string.punctuation
	l = string.ascii_lowercase
	l_ = string.ascii_uppercase
	m = string.digits
	h = []
	for i in range(3):
		h.append((random.choice(s) + random.choice(k + l + l_ + m)))
	return "".join(h)

n = input().split()
#print("this is s: ", n)
j = int(input("Do you want any special characters in your password?"+ "\n"+ "1 for yes"+ "\n" + "0 for no"))
print(opp(n, j))
