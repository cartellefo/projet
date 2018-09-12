import psycopg2
#from config import config

def create_tables():
    sql = """CREATE TABLE animal(
       espece varchar,
        sexe varchar,
        date_naissance varchar,
        nom varchar,
        code integer,
        commentaires varchar
    )
    """



try:
        
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
       
    cur = conn.cursor()
        
    cur.execute(sql)
        
    conn.commit()
        
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
    if conn is not None:
            conn.close()



def insert_animal_list(animal_list):
    
    sql = "INSERT INTO animal(espece, sexe, date_naissance, nom, code, commentaires) VALUES(%s)"
    conn = None
    try:
        
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
       
        cur = conn.cursor()
        
        cur.executemany(sql)
        
        conn.commit()
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



if __name__ == '__main__':
    create_tables()
   
    insert_animal_list([
        ('chien', 'F', '2008-02-20 15:45:00' , 'Canaille', 1150, None),
        ('chien', 'F','2009-05-26 08:54:00'  , 'Cali', 4422,'NULL'),
        ('chien', 'F','2007-04-24 12:54:00' , 'Rouquine',5611, 'NULL'),
        ('chien', 'F','2009-05-26 08:56:00' , 'Fila',1802, 'NULL'),
        ('chien', 'F','2008-02-20 15:47:00' , 'Anya', 1721,'NULL'),
        ('chien', 'F','2009-05-26 08:50:00' ,'Louya' ,3600, 'NULL'),
        ('chien', 'F', '2008-03-10 13:45:00','Welva' ,1140, 'NULL'),
        ('chien', 'F','2007-04-24 12:59:00' ,'Zira' ,3230, 'NULL'),
        ('chien', 'F', '2009-05-26 09:02:00','Java' , 3628,'NULL'),
        ('chien', 'M','2007-04-24 12:45:00' ,'Balou' , 4044,'NULL'),
        ('chien', 'M','2008-03-10 13:43:00' ,'Pataud' , 2013,'NULL'),
        ('chien', 'M','2007-04-24 12:42:00' , 'Bouli', 2018,'NULL'),
        ('chien', 'M', '2009-03-05 13:54:00','Zoulou' ,1456, 'NULL'),
        ('chien', 'M','2007-04-12 05:23:00' ,'Cartouche' ,1468, 'NULL'),
        ('chien', 'M', '2006-05-14 15:50:00', 'Zambo', 3462, 'NULL'),
        ('chien', 'M','2006-05-14 15:48:00' ,'Samba' ,1357, 'NULL'),
        ('chien', 'M', '2008-03-10 13:40:00','Moka' , 3431, 'NULL'),
        ('chien', 'M', '2006-05-14 15:40:00','Pilou' ,2784, 'NULL'),
        ('chat', 'M','2009-05-14 06:30:00' , 'Fiero', 3902, 'NULL'),
        ('chat', 'M','2007-03-12 12:05:00' ,'Zonko', 3819, 'NULL'),
        ('chat', 'M','2008-02-20 15:45:00' , 'Filou', 2109, 'NULL'),
        ('chat', 'M','2007-03-12 12:07:00' , 'Farceur',2078, 'NULL'),
        ('chat', 'M','2006-05-19 16:17:00' ,'Caribou' , 2904, 'NULL'),
        ('chat', 'M','2008-04-20 03:22:00' , 'Capou', 3018, 'NULL'),
        ('chat', 'F','2007-03-12 12:05:00' ,'Zolo', 3029, 'NULL'),
        ('chat', 'M','2008-02-20 15:45:00' , 'fota', 9032, 'NULL'),
        ('chat', 'F','2007-03-12 12:07:00' , 'Focer', 2018, 'NULL'),
        ('chat', 'M','2006-05-19 18:17:00' ,'ja' , 1834, 'NULL'),
        ('chat', 'M','2008-04-20 03:22:00' , 'Cipo', 1948, 'NULL'),
        ('chien', 'M', '2006-05-14 15:50:00', 'Zamo', 3402, 'NULL'),
        ('chien', 'M','2006-05-14 15:48:00' ,'Sama' ,1057, 'NULL'),
        ('chien', 'M', '2008-03-10 13:40:00','Mok' , 3931, 'NULL'),
        ('chien', 'M', '2006-05-14 15:40:00','Pilo' ,2284, 'NULL'),
        ('chat', 'M','2009-05-14 06:30:00' , 'Firo', 3502, 'NULL'),
        ('chat', 'M','2007-03-12 12:05:00' ,'Zonka', 3889, 'NULL'),
        ('chat', 'M','2008-02-20 15:45:00' , 'Fealou', 2119, 'NULL'),
        ('chat', 'M','2007-03-12 12:07:00' , 'Fca',2008, 'NULL'),
        ('chat', 'M','2006-05-19 16:17:00' ,'Car' , 2964, 'NULL'),
        ('chat', 'M','2008-04-20 03:22:00' , 'Caou', 3318, 'NULL'),
        ('singe', 'M', '2007-05-14 15:50:00', 'Zambo', 3062, 'NULL'),
        ('singe', 'M','2009-05-14 15:48:00' ,'Samba' ,3357, 'NULL'),
        ('singe', 'M', '2009-03-10 13:40:00','Moka' , 3431, 'NULL'),
        ('singe', 'M', '2009-05-14 15:40:00','Pilou' ,1784, 'NULL'),
        ('singe', 'M','2005-05-14 06:30:00' , 'Fiero', 1902, 'NULL'),
        ('signe', 'M','2009-03-12 12:05:00' ,'Zonko', 2819, 'NULL'),
        ('signe', 'M','2009-02-20 15:45:00' , 'Filou', 9109, 'NULL'),
        ('signe', 'M','2008-03-12 12:07:00' , 'Farceur',6078, 'NULL'),
        ('singe', 'M','2008-05-19 16:17:00' ,'Caribou' , 2304, 'NULL'),
        ('singe', 'M','2009-04-20 03:22:00' , 'Capou', 2018, 'NULL'),
        ('chat', 'M','2006-05-19 16:56:00' , 'Raccou', 'Pas de queue depuis la naissance')
    ])
         
         




