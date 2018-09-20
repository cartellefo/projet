
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
    f = open("ready_data/company_animal.sql", "w")
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
        CREATE TABLE buyers (
            buyer_id integer,
            buyer_name  varchar,
            buyer_city varchar,
            date_of_birth timestamp,
            primary key (buyer_id)
        );  
        """,
        """
        CREATE TABLE animalComp (
            animal_id integer PRIMARY KEY,
            venue_id Integer REFERENCES venue(venue_id),
            owner_id INTEGER REFERENCES owners(owner_id),
            buyer_id integer references buyers(buyer_id),
            variety varchar,
            sex char(3),
            sales_event timestamptz,
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
    print('please give me the CPU time')
        
    # write in to csv data every tab
    #the bow for: to the table random values 
    
    g = open('ready_data/venues.csv', 'w')
    print("step1 ... ")
    g.write('venue_id,venue_name,city\n')


    f = open("ready_data/company_animal.sql", "a")    

    Vmax =max(10,min(200,int(Nmax*0.01)))
    print(Vmax)
    for i in range(0, Vmax):
        vid = str(i)
        vna = random.choice(place)
        vci = random.choice(city)
        stmt = "INSERT INTO venue (venue_id,venue_name,city) VALUES ('" + vid+"','"+vna+"','"+vci+"');"
     #   f = open("company_animal.sql", "a")
        f.write("\n" + stmt)
        g.write(vid+","+vna+","+vci + '\n')
        #f.close() 
    g.close()    
    print("step1 done ")

    g = open('ready_data/owners.csv', 'w')
    g.write('owner_id,owner_name,owner_city,date_of_birth\n')
    for i in range(0, 100*Nmax):
        if(i%10000==0) :
            print(i)
        oid = str(i)
        ownersIdListe.append(oid)
        ona = random.choice(person_name)
        oci = random.choice(city)
        od  = str(randomDate("1/1/1960 1:30 PM", "1/1/2009 4:50 AM"))

        stmt = "INSERT INTO owners(owner_id,owner_name,owner_city,date_of_birth) VALUES ('" + \
            oid+"','"+ona+"','"+oci+"','"+od+"');"
        
        g.write(oid+','+ona+','+ oci+','+od+'\n')
        
        f.write("\n" + stmt)
        #f.close() 
    g.close()

    print("step1 done ")

    #fieldnames = ['buyer_id', 'venue_id', 'buyer_name', 'buyer_city', 'date_of_birth']

    g = open('ready_data/buyers.csv', 'w')
    g.write('buyer_id,buyer_name,buyer_city,date_of_birth\n')
    for i in range(0, 90*Nmax):
        if(i%10000==0) :
            print(i)
        bid = str(i)
        bna = random.choice(person_name)
        bci = random.choice(city)
        bd  = str(randomDate("1/1/1980 1:30 PM", "1/1/2009 4:50 AM"))
        stmt = "INSERT INTO buyers(buyer_id, buyer_name, buyer_city, date_of_birth) VALUES ('" + \
            bid+"','"+bna+"','"+bci+"','"+bd+"');"
        g.write(bid+','+ bna+','+bci+','+bd+'\n')
      #  f = open("company_animal.sql", "a")
        f.write("\n" + stmt)
        #f.close() 
    g.close()



    print("step2 done ")
#        fieldnames = ['animal_id', 'venue_id', 'owner_id', 'variety', 'sex', 'date_of_birth', 'comments']

    g = open('ready_data/animal_sale.csv', 'w')  
    for i in range(0, 100*Nmax):
        if(i%10000==0) :
            print(i)
        aid = str(i)
        vid = str(random.randint(0,Vmax-1))
        oid = str(random.randint(0,100*Nmax-1))
        bid = str(random.randint(0,90*Nmax-1))
        v = random.choice(espece)
        s = random.choice(sex)
        d = str(randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM"))
        stmt = "INSERT INTO animalComp(animal_id, venue_id, owner_id,buyer_id, variety, sex, sales_event, comments) VALUES ('" + \
            aid+"','"+vid+"','"+oid+"','"+bid+"','"+v+"','"+s+"','"+d+"','none');"
        g.write(aid+','+vid+','+ oid+','+bid+','+v+','+s+','+d+','+'none'+ '\n')
    #    f = open("company_animal.sql", "a")
        f.write("\n" + stmt)
    g.close()
    print("step3 done ")
    f.close()   
    end = time.time()
    elapsed = end - start # cpu time     
    print (elapsed)

if __name__ == '__main__':
    create_tables()
    #insert_company_animal(10)
    insert_company_animal(int(sys.argv[1]))
