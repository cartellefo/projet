import psycopg2
import time


start = time.time()
try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
except:
    print("I am unable to connect to the database")
#cur.execute("""SELECT datname from pg_database""")

cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute('SELECT version()')

db_version = cur.fetchone()
print(db_version)

end = time.time()
elapsed = end -start
print(elapsed)
#connect()
