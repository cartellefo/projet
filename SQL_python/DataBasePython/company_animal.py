
import psycopg2
from random import randint
import random
import time
import random
import sys
import csv

espece = ['dog', 'puppy', 'cat', 'kitten', 'owl', 'owlet', 'bird', 'parrot', 'turtle', 'tortoise', 'mouse', 'lizard', 'horse', 'pork', 'hen', 'turkey cock'
              'flock', 'lamb', 'fly', 'elefant']
nouns = ['people', 'history', 'way', 'art', 'world', 'information', 'map', 'two', 'family', 'government', 'health',
             'system', 'computer', 'meat', 'year', 'thanks', 'music', 'person', 'reading', 'method', 'data', 'food', 'understanding']
sex = ['M', 'F']
city = ["Frankfurt", "Zürich", "Bern", "Stuttgart", "Freiburg", "Ulm", "Hamburg", "München", "Nürnberg", "Zürich", "Bregenz", "Salzburg", "Wien"]
place =["berliner_platz", "willy_brandt_platz", "hauptbahnhof"]
person_name = ["Marie", "Niklas", "Daniel ", "Felix ", "Mara" ,"Arda","Ali","Raphael","Theresa" ,"Carl","Jamal" ,"Titus","Lino","\
Selma", "Clemens", "Bo", "Dilan", "Alperen", "Janis", "Issa", "Noa", "Nikola", "Maris", "Anes", "Adel", "Boubacar", "Francis", "Minu"   
,"Mame", "Jing", "Nour", "Cinar", "Elyesa", "Anelia", "Sydney", "Bonny ", "Augustin", "Demir", "Elham", "Hani", "Fabien", "İsa"  
,"Anmol", "Kader", "Devrim" ,"Ramadan" ,"Lennie", "Nazar", "Hayden"     
,"Sabrin" ,"Hakim ","Dewin"  ,"Mohammed"]


def strTimeProp(start, end, format):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + random.random() * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end,):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p')


def create_tables():
    f = open("company_animal.sql", "w")
    commands = (
        """
        CREATE TABLE venue  (
            venue_id integer primary key,
            venue_name varchar,
            city  varchar
           
        );
        """,
        """ 
        CREATE TABLE owners (
            owner_id integer primary key,
            owner_name varchar,
            owner_city varchar,
            date_of_birth timestamp
            );
        """,
        """
        CREATE TABLE buyer (
            buyer_id integer,
            venue_id integer,
            buyer_name  varchar,
            buyer_city varchar,
            date_of_birth timestamp,
            primary key (buyer_id,venue_id),
            FOREIGN KEY (venue_id) REFERENCES venue(venue_id)
            --venue_id foreign key
        );  
        """,
        """
        CREATE TABLE animalComp (
            animal_id integer PRIMARY KEY,
            venue_id Integer REFERENCES venue(venue_id),
            owner_id INTEGER REFERENCES owners(owner_id),
            variety varchar,
            sex char(3),
            date_of_birth timestamptz,
            comments text
            
           );

        """)

    
    for command in commands:
        #print(command)
        f.write(command)

    f.close()


   
    



def insert_company_animal(Nmax):
    venueIdListe = []
    ownersIdListe =[]
    start = time.time()
    print(' please give me the CPU time')
        
    # write in to csv data every tab
    #the bow for: to the table random values 
    f = open("company_animal.sql", "a")
    with open('venues_animal.csv', 'w+', newline = '') as csvfile:
        fieldnames = ['venue_id','venue_name','city']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(0, Nmax):
            vid = str(randint(0000, 1000))
            venueIdListe.append(vid)
            vna = random.choice(place)
            vci = random.choice(city)
            stmt = "INSERT INTO venue (venue_id,venue_name,city) VALUES ('" + \
                vid+"','"+vna+"','"+vci+"');"
            
            f.write("\n" + stmt)
            writer.writerow({'venue_id': vid, 'venue_name':vna,'city':vci})
    csvfile.close()    
    print("step1 done ")
    with open('owners_animal.csv', 'w', newline = '') as csvfile:
        fieldnames = ['owner_id','owner_name','owner_city','date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(0, Nmax):
            oid = str(randint(0000, 1000))
            ownersIdListe.append(oid)
            ona = random.choice(person_name)
            oci = random.choice(city)
            od  = str(randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM"))

            stmt = "INSERT INTO owners(owner_id,owner_name,owner_city,date_of_birth timestamp) VALUES ('" + \
                oid+"','"+ona+"','"+oci+"','"+od+"');"
            
            writer.writerow({'owner_id': oid,'owner_name': ona,'owner_city': oci,'date_of_birth':od})
            f.write("\n" + stmt)
    csvfile.close()

    print("step1 done ")

    with open('buyer_animal.csv', 'w', newline='') as csvfile:
        fieldnames = ['buyer_id', 'venue_id', 'buyer_name', 'buyer_city', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        f = open("animal.sql", "a")
        for i in range(0, Nmax):
            bid = str(randint(0000, 1000))
            vid = random.choice(venueIdListe)
            bna = random.choice(person_name)
            bci = random.choice(city)
            bd  = str(randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM"))
            stmt = "INSERT INTO buyer(buyer_id,venue_id,buyer_name,buyer_city,date_of_birth timestamp) VALUES ('" + \
                bid+"','"+vid+"','"+bna+"','"+bci+"','"+bd+"');"
            
            writer.writerow({'buyer_id': bid, 'venue_id':vid,'buyer_name': bna,'buyer_city': bci,'date_of_birth':bd})
            f.write("\n" + stmt)
    csvfile.close()

    print("step2 done ")

    with open('buyer_animal.csv', 'w', newline='') as csvfile:
        fieldnames = ['animal_id', 'venue_id', 'owner_id', 'variety', 'sex', 'date_of_birth', 'comments']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()    
        for i in range(0, Nmax):
            aid = str(randint(0000, 1000))
            vid = random.choice(venueIdListe)
            oid = random.choice(ownersIdListe)
            v = random.choice(espece)
            s = random.choice(sex)
            d = str(randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM"))
            stmt = "INSERT INTO animalComp(animal_id, venue_id, owner_id, variety, sex, date_of_birth, comments) VALUES ('" + \
                aid+"','"+vid+"','"+oid+"','"+s+"',"+d+",'none');"
            writer.writerow({'animal_id': aid,'venue_id': vid,'owner_id': oid,'variety': v, 'sex': s,'date_of_birth':d,'comments': 'none'})
            f.write("\n" + stmt)
    csvfile.close()
    print("step3 done ")
    f.close()   
    end = time.time()
    elapsed = end - start # cpu time     
    print (elapsed)

if __name__ == '__main__':
  #  create_tables()
    #insert_company_animal(10)
    insert_company_animal(int(sys.argv[1]))
