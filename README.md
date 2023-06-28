# statera_faker_data

#Ajouter les 8 fichiers json dans le dossier data

#Créer une base de donnée mongo DB compass en local

#executer le fichier mongo_db.py pour créer les collections sur mongo db

Pour générer des id utilisateurs exectuer insert.py et modifier le nombre d'utilisateur que vous voulez,
par deffaut il est à 150 .


for i in  tqdm(range(0,150)): <-- changer la valeur numéro 2

Ensuite Allez dans Processing_data puis exectuer Processing__data.py 

cette fonction demande un peu de temps en terme d'exectuion car elle apelle les fichiers les plus volumineux.
UNe fois l'execution finit vous pouvez allez voir votre BDD mongo db

