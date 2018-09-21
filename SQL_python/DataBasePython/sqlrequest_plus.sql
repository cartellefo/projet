drop table venue;
drop table buyer;
drop table OWNERS;
drop table animalComp;




        CREATE TABLE venue  (
            venue_id integer primary key,
            venue_name varchar,
            city  varchar
           
        );
         
        CREATE TABLE owners (
            owner_id integer primary key,
            owner_name varchar,
            owner_city varchar,
            date_of_birth timestamp
            );
        
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
        
        CREATE TABLE animalComp (
            animal_id integer PRIMARY KEY,
            venue_id Integer REFERENCES venue(venue_id),
            owner_id INTEGER REFERENCES owners(owner_id),
            variety varchar,
            sex char(3),
            date_of_birth timestamptz,
            comments text
            
           );
           
           

select owner_name,owner_id
 from owners
 where owner_id = (select max(owner_id) from owners);





 select owner_name,owner_id
 from owners,animalcomp
 where owners.owner_id =animalcomp.owner_id;


SELECT *
FROM owners
INNER JOIN animalcomp ON owners.owner_id= animalcomp.owner_id 
INNER JOIN venue ON venue.venue_id = animalcomp.venue_id;


select from animalcomp
where variety = 'dog'
inner join buyers on buyers;

-- welche owner hat die meiste tiere verkaufen?
select count(*),a.owner_id, b.owner_name 
from animalcomp a left join owners b on a.owner_id=b.owner_id 
where a.owner
group by a.owner_id, b.owner_name order by count(*) desc ;

--# Anzahl an verkaufte Hund pro monat
SELECT
    date_trunc('month', sales_event) m,
    COUNT (animal_id)
FROM
    animalcomp 
    where variety = 'dog'
GROUP BY
    m
ORDER BY
    m;
--alle  Tiere pro Wochen, die in der gleiche Stadt verkauft würden, pro Tiere art
select round(anzahl/sum(anzahl) over (partition by 1),3) as rel_part,variety from 
(
Select count(*) anzahl ,a.variety 
From animalcomp a
inner join owners o on o.owner_id= a.owner_id 
inner join buyers b on b.buyer_id = a.buyer_id
group by variety
)name_table

;


-- anzahl an buyer mit alter, Jahrgang


SELECT
    EXTRACT(YEAR FROM age( date_of_birth)) age ,left(date_trunc('year', date_of_birth)::text,4) as _year,
    COUNT (buyer_id)
FROM
  	buyers 
 group by age, buyer_name,_year
 order by buyer_name

;



select date_trunc('year', '08/01/1981 04:25 PM'::timestamptz) ,age('08/01/1981 04:25 PM'::timestamptz), EXTRACT(YEAR FROM age('08/01/1981 04:25 PM'::timestamptz)); 
----

select date_trunc('year', '08/01/1981 04:25 PM'::timestamptz) ,age('08/01/1981 04:25 PM'::timestamptz), EXTRACT(YEAR FROM age('08/01/1981 04:25 PM'::timestamptz)); 

SELECT md5(animalcomp::text) FROM animalcomp limit 10; 

----
select 'hash' as checksum_record, * from animalcomp limit 10;

SELECT md5 (animalcomp::text) FROM animalcomp limit 10;

select 'hash' as checksum_record(animalcomp::text), * from animalcomp limit 10;

SELECT md5(animalcomp::text) FROM animalcomp limit 10;        
