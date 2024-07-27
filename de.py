from random import randint;

for i in range(0, 10) :
	x = randint(1, 6)
	if x==2 or x==5 : 
		print("vous avez gagné") 
	else : 
		print("vous avez perdu")

nbre = 0
for i in range(0, 100) :
		x = randint(1, 6)
		if x==2 or x==5 :
			nbre+=1
print("vous avez gagné ", nbre, "fois en 100 jets de dé successifs")

