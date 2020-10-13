# Media-Tech
Mon application d'achat et de vente de livre réalisée pour ma certification informatique en 2020

# mise en place de l'application 
Pour que l'application fonctionne il va falloir créer un environnement virtuel python sur lequel travailler. 
-clic droit -> creer un dossier --> l'appeler env 
-ouvrir l'invit de commande et importer le virtual env -->  pip install virtualenv 
-Creer l'application dans l'environnement  virtualenv env/myshop 
-activer l'environnement virtuel  --> cd C:\Users\AppData\Local\Programs\Python\env\myshop\Scripts --> et faire activate 
- Telecharger Django  --> pip install Django==2.0.5
- Lancer le serveur avec une commande --> manage.py runserver 


# Explication de l'application 
L'application est un modèle de création d'un eshop via python et le framework django 
-Il référence des livres rares/ leurs prix / leurs disponibilités i ls'agit d'un site factice qui peut-être facilement modelé selon les besoins 

# Interface admin 
Pour pouvoir facilement utiliser l'interface admin de django et ajouter des articles il faut creer un superuser 
- Aller dans la console et faire --> python manage.py createsuperuser --> Rentrer les informations 
- Il suffira juste d 'ajouter par la suite les éléments avec le add product/groups/category

# Version 
python 3.6.5 
django 2.0.5
Pillow 5.1.0
