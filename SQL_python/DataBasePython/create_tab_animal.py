import psycopg2
from random import randint
import random
import time
import random
import sys
# from config import config


# random date
def strTimeProp(start, end, format):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + random.random() * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end,):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p')


# print(randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM"))


f = open("animal.txt", "w")


def create_tables():

    sql = """DROP TABLE animal"""
    sql2 = """CREATE TABLE IF NOT EXISTS animal(
        animal_key serial,
       variety varchar,
        sex char(3),
        date_of_birth timestamptz,
        name varchar,
        code integer,
        comments text
    );
    """
    f.write(sql2)

    try:

        conn = psycopg2.connect(
            "dbname='postgres' user='postgres' host='localhost' password='dbpass'")

        cur = conn.cursor()
   #     cur.execute(sql)
        cur.execute(sql2)

        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_animal_list_db(Nmax):
    print(Nmax)
    espece = ['dog', 'puppy', 'cat', 'kitten', 'owl', 'owlet', 'bird', 'parrot', 'turtle', 'tortoise', 'mouse', 'lizard', 'horse', 'pork', 'hen', 'turkey cock'
              'flock', 'lamb', 'fly', 'elefant']
    nouns = ['people', 'history', 'way', 'art', 'world', 'information', 'map', 'two', 'family', 'government', 'health',
             'system', 'computer', 'meat', 'year', 'thanks', 'music', 'person', 'reading', 'method', 'data', 'food', 'understanding']

    sex = ['M', 'F']

    conn = None
    try:

        conn = psycopg2.connect(
            "dbname='postgres' user='postgres' host='localhost' password='dbpass'")

        cur = conn.cursor()
        for i in range(0, Nmax):
            if i % 100 == 0:
                print(i)
            v = random.choice(espece)
            s = random.choice(sex)
            d = randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM")
            n = random.choice(nouns)
            c = randint(0000, 10000)
            sql = """INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES (%s,%s,%s,%s,%s,%s)"""
            cur.execute(sql, (v, s, d, n, c, 'comment'))
            conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    # Notice that we don't need the `csv` module.
    # next(f)  # Skip the header row.


# conn.commit()


def insert_animal_list_file(Nmax):

    #f = StringIO("42\tfoo\n74\tbar\n")
    # with open('animal.csv', 'r') as f:
        # print(Nmax)

    espece = ['dog', 'puppy', 'cat', 'kitten', 'owl', 'owlet', 'bird', 'parrot', 'turtle', 'tortoise', 'mouse', 'lizard', 'horse', 'pork', 'hen', 'turkey cock'
              'flock', 'lamb', 'fly', 'elefant']
    nouns = ['people', 'history', 'way', 'art', 'world', 'information', 'map', 'two', 'family', 'government', 'health',
             'system', 'computer', 'meat', 'year', 'thanks', 'music', 'person', 'reading', 'method', 'data', 'food', 'understanding']

    sex = ['M', 'F']

    for i in range(0, Nmax):
        if i % 100 == 0:
            print(i)
        v = random.choice(espece)
        s = random.choice(sex)
        d = str(randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM"))
        n = random.choice(nouns)
        c = str(randint(0000, 10000))
        stmt = "INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('" + \
            v+"','"+s+"','"+d+"','"+n+"',"+c+",'none');"
        #f = open("animal.txt", "a")
        f.write("\n" + stmt)

      # print(stmt)
# f.close()


# pg_dump  -f postgres > sql_file
# pg_dump [connection-option...] [option...] [dbname]


if __name__ == '__main__':

    create_tables()
    insert_animal_list_file(15)

   # insert_animal_list_db(int(sys.argv[1]))

    # insert_animal_list_file(int(sys.argv[1]))

#
