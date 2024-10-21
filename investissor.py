print("Montant initial de l'investissement ?")
inv = int(input())
print("Taux de rendement?")
rend = int(input())
res = (inv * rend) / 100
print(f"gain annuel : {res}")
print("Ajout 5000")
inv += 5000
print(f"nouveau montant : {inv}")
print("Augmentation taux de rdt de 2 %")
rend += 2
res = (inv * rend) / 100
print(f"nouveau gain : {res}")
montant = res + inv
print(f"montant total {montant}")
print("Retrait de 10%")
montant = montant - montant / 10
rend -= 1
print(rend)
res = (inv * rend) / 100
print(f"nouveau montant total : {montant}")