# projet

Das ist mein eigenes Spielprojekt

jetzt versuche ich SQL mit Posgres python und crossbar

 crossbar - python - postgres
 nous suposons ici que notre base de données se touve ailleurs que dans notre machine ie nous pouvons pas faire d'acces direct. Nous avons donc besoin d'un crossbar.

a) le travail ici consiste  a recuperer le temps de CPU lors de l'exercutio d'un programme avec publisher de crossbar et inserer dans une base  de donner avec subscriber.

1 - créer la base de données et y charger des données (cf create.py, insert.py)
2 - programmer le publisher en lui indiquant le message a publier (cf puconn.py) 
3 - programmer le subscriber en le connecter aavec la base de données

s'assurer que publisher et subscriber sont connecter au meme localhost ici le 8080 ie celui du crossbar
la fonction qui calcule le cpu time se trouve dans publisher.

b) le travail ici consiste a recuperer les données dans une base de données. nous avons besoin de recuperer les données dans une base pour ensuite l'etudier

1- programmer la fonction read_write  qui lire et ecrire dans la base de données (cf read_write.py)
2- programmer la fonction call_select qui appel la fonction read_write pour executer

call_select effectue un appel. cependant elle doit avoir le meme topic que la fonction read_write ici "u'repi.data.select'" 
dans le code read_write, nous avons deux fonctions precise read et write. Write ecris dans notre base de données et read y lit. Cependant il est preferable que read read aient des topic differents. on sous entend ici le faire qu'ils peuvent avoir le meme topic.
La fonction read sera appeler par une autre fonction pour etre executer ici call_select et sur quoi ils doivent avoir le meme topic.








