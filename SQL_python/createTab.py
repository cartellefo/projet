import psycopg2
#from config import config
 
 
def create_tables():
   
    commands = (
        """
        CREATE TABLE vendeur (
            vendeur_id SERIAL PRIMARY KEY,
            vendeur_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_connecteur (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
       CREATE TABLE membres (
                age INTEGER ,
                nom  VARCHAR(5) NOT NULL,
                taile  numeric NOT NULL,
                
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendeur_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)

# def insert_tables():
#     commands = (
#         cur.execute("INSERT INTO membres(age,nom,taille) VALUES(21,'Dupont',1.83)")
#         cur.execute("INSERT INTO membres(age,nom,taille) VALUES(15,'Blumâr',1.57)")
#         cur.execute("INSERT Into membres(age,nom,taille) VALUES(18,'Özémir',1.69)")
#         )


    conn = None
    try:
        
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
        cur = conn.cursor()
      
        for command in commands:
            cur.execute(command)
     
        cur.close()
        
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()














