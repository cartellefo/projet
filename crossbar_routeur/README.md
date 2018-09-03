


# fehler docker image nicht genannt
-docker run -d -p 8000:80 --name="crossbar-router"  ici ne marche pas car le premier argument est  obligatoire et le deuxieme optionnel


-docker run -d -p 8000:80  crossbario/crossbar : on le faire sans nom
-docker stop brave_kilby: le croosbar etant crée avec un nom alleatoire on le stoppe
-docker rm brave_kilby: on stoppe et on l'efface de la memoire
run -d -p 8000:8080 --name="crossbar-router" crossbario/crossbar 
-run -d -p 8080:8080 --name="crossbar-router" crossbario/crossbar : on recree en donnant le nom et en changeant le port
