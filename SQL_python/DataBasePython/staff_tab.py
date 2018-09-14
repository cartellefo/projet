import psycopg2




sql = """CREATE TABLE employee(
   empl_id integer,
   empl_name varchar,
   empl_tsp varchar,
   empl_sexe varchar,
   date_of_birth date,
   commentaires varchar
)
"""


try:

    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' host='localhost' password='dbpass'")

    cur = conn.cursor()

    cur.execute(sql)

    conn.commit()

    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()


# if __name__ == '__main__':
#     create_tables()