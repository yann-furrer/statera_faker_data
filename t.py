import random

def prob_moyenne(liste):
    if not liste:
        return 0.0
    moyenne = sum(liste) / len(liste)
    #print("moyenne ",moyenne)
    ecart_type = (sum((x - moyenne)**2 for x in liste) / len(liste))**0.5
    #print("ecart type ",ecart_type)
    if ecart_type == 0:
        return 0.0
    proba = (moyenne - min(liste)) / (max(liste) - min(liste))
    proba = proba*2 - 1
    return proba
#liste = [random.uniform(-1,1) for _ in range(16)]

# print("--------------------------------")
# print("liste:", liste)
# print("prob",prob_moyenne(liste))
# print("--------------------------------")

c = 0

for i in range(100):
    liste = [random.uniform(-1,-0.2) for _ in range(16)]
    data = prob_moyenne(liste)
    if data < 0:
      #  print(liste)
        print(data)
        c +=1
print("ratio négatif :",c,"%")
# La fonction prend une liste de nombres en entrée, calcule la moyenne et l'écart-type de la liste,
# puis normalise la moyenne pour obtenir une probabilité. Cette probabilité est normalisée pour être dans l'intervalle [-1, 1],
# où -1 correspond à la moyenne la plus basse dans la liste et 1 correspond à la moyenne la plus élevée.
# Notez que la fonction retourne 0.0 si la liste est vide ou si l'écart-type est égal à 0.
# Cela évite les erreurs de division par zéro et renvoie une probabilité neutre lorsque les données sont constantes.