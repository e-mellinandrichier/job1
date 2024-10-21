print("Inventaire :")

print("Créez un nouveau produit")
print("Nom ?")
name = input()
print("Prix ?")
price = int(input())
print("Quantité ?")
quant = int(input())

print(f"Nom de l'article : {name}, prix : {price} euros, quantité disponible : {quant}")

print(f"Combien voulez-vous acheter de {name}?")
new_quant = int(input())
quant -= new_quant
print(f"Nouvelle quantité de {name} : {quant}")

new_price = price
new_price += new_price / 10
print(f"L'inflation a frappé... Le nouveau prix de {name} est : {new_price} euros au lieu de {price} euros")