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

select count(*),a.owner_id, b.owner_name 
from animalcomp a left join owners b on a.owner_id=b.owner_id 
where a.own
group by a.owner_id, b.owner_name order by count(*) desc ;

# Anzahl an verkaufte Hund pro monat
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
#alle  Tiere , die von einem owner verkauft wurden, der aus der gleichen stadt kommt wie der buyerdie in der gleiche Stadt verkauft würden, pro Tiere art
Select * 
From animalcomp
inner join owners on owners.owner_id= animalcomp.owner_id 
inner join buyer on buyer.buyer_id = animalcomp.buyer_id






inner join owners on owners.city= buyer.city
inner join buyer on buyer.buyer_id = animalcomp.buyer_id

select *  animal_id
from owners


SELECT count (*)
FROM animalcomp
INNER JOIN owners
ON animalcomp.owner_id=owners.owner_id
WHERE 
item.rate>=10;
group by
	m
order by
   variety






