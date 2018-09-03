
import psycopg2
#from config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        #params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
        # create a cursor
        cur = conn.cursor()
        
 # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    connect()











# import psycopg2
# import time


# start = time.time()
# try:
#     conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
# except:
#     print("I am unable to connect to the database")
# #cur.execute("""SELECT datname from pg_database""")

# cur = conn.cursor()

# print('PostgreSQL database version:')
# cur.execute('SELECT version()')

# db_version = cur.fetchone()
# print(db_version)


#     connect()

