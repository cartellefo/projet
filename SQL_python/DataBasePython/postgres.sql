

INSERT INTO animal (espece, sexe, date_naissance, nom,code, commentaires) VALUES 
        ('chien', 'F', '2008-02-20 15:45:00' , 'Canaille', 1150, ''),
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
        ('chat', 'M','2006-05-19 16:56:00' , 'Raccou',3012, 'Pas de queue depuis la naissance');
        
        
        
------------------------------------------------------------------------------
--import the the excel file to sql 
LOAD DATA LOCAL INFILE 'animal.csv'
INTO TABLE Animal
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(espece, sexe, date_naissance, nom, commentaires);

        

----------------------------------------------------------------------------
-- sum_n_product_with_animal
-- intput x : number to add
--        y : limit
--        z : OFFSET
-- out sum(values + x), product(values * x)
  
CREATE OR REPLACE FUNCTION sum_n_product_with_animal(x int,y int,z int, OUT sum int, OUT product int)
RETURNS SETOF record
AS $$
    SELECT $1 + animal.code, $1 * animal.code
     FROM animal
     limit $2 OFFSET $3;
$$ LANGUAGE SQL;

SELECT * FROM sum_n_product_with_animal(4,2,6); 



CREATE OR REPLACE FUNCTION type_animal(x varchar,OUT animal_type varchar) 
returns setof record
AS $$
SELECT animal.nom
from animal
where animal.espece = 'x';
$$ language SQL;  
select type_animal('chien')
------------------------------------------------------------------------------

CREATE FUNCTION avgCode(VARIADIC arr numeric[]) RETURNS numeric AS $$
    SELECT avg($1[i]) FROM animal($1, 1) g(i);
$$ LANGUAGE SQL;
SELECT avgCode(10, -1, 5, 4.4);










----------------------------------------------------------------------------
select * from part_drawings;

select * from vendor_parts;


CREATE OR REPLACE FUNCTION players_young2(x INTEGER)
 RETURNS  NUMERIC AS $total$
 declare
	total integer;
  BEGIN
     SELECT 
     SUM(CASE WHEN p_alter<x then 1 ELSE 0 END) into total
      FROM t_players
 ;
  RETURN total;
      
END;
$total$ LANGUAGE plpgsql;



DO $$
DECLARE
    counter integer := 1;
    tsp VARCHAR(50) := 'a';
	ElpExt VARCHAR(50) := 'b';
	
BEGIN
		RAISE NOTICE ' % % %',counter,tsp,ElpExt;
END $$;
 LANGUAGE plpgsql;
	


	


-- the number of age less thant x : x is the intput parameter
CREATE OR REPLACE FUNCTION players_young(x INTEGER)
 RETURNS  NUMERIC AS $total$
 declare
	total integer;
  BEGIN
     SELECT 
     count(*) into total
      FROM t_players
  where p_alter < x;
  RETURN total;
      
END;
$total$ LANGUAGE plpgsql;

select players_young(15);


-- the function count vendors
CREATE OR REPLACE FUNCTION vendors_number()
 RETURNS  NUMERIC AS $total$
 declare
	total integer;
  BEGIN
     SELECT 
     count (vendors) into total
      FROM vendors;
      RETURN total;
      
END;$total$ LANGUAGE plpgsql;

select vendors_number();








-- function giving the list of persons with id<x  
   CREATE OR REPLACE FUNCTION getlist(x int) RETURNS SETOF vendors AS $$
    SELECT * FROM vendors WHERE vendor_id < x;
$$ LANGUAGE SQL;

SELECT * FROM getlist(10) AS t1;


-- function return p_alter greater than x

CREATE OR REPLACE FUNCTION players_number(x INTEGER)
 RETURNS  NUMERIC AS $t_numb$
 declare 
 	t_numb numeric;
	BEGIN
         select p_alter into t_numb
          from t_players
          where p_alter > x;
          return t_numb;
          
END;$t_numb$ LANGUAGE plpgsql;
select players_number(2);








DO $$
DECLARE
    counter integer := 1;
    tsp VARCHAR(50) := 'a';
	ElpExt VARCHAR(50) := 'b';
	
BEGIN
		RAISE NOTICE ' % % %',counter,tsp,ElpExt;
END $$;
 LANGUAGE plpgsql;









 	
 	
 select f_metadata('bdv','bn');   
 select f_metadata(12,5);   
      
      
CREATE OR REPLACE FUNCTION totalRecords ()
RETURNS integer AS $total$
declare
	total integer;
BEGIN
   SELECT count(*) into total FROM COMPANY;
   RETURN total;
END;
$total$ LANGUAGE plpgsql;  
select count(*) from vendors;
  
------------------------------- 
 CREATE OR REPLACE FUNCTION sum_n_product_with_animal(x int,y int,z int, OUT sum int, OUT product int)
RETURNS SETOF record
AS $$
    SELECT $1 + animal.code, $1 * animal.code
     FROM animal
     limit $2 OFFSET $3;
$$ LANGUAGE SQL;

SELECT * FROM sum_n_product_with_animal(4,2,6); 
            


CREATE OR REPLACE FUNCTION f_metadata(a text, b text)
RETURNS VARCHAR AS $info$

	DECLARE
    	info text;
    		
	BEGIN
	  INSERT INTO animal(nom, date_naissance)
	   VALUES (a, b);
	   
	 
	END; 
 	$info$ LANGUAGE plpgsql; 

select * from f_metadata('kenufh','2534');



            INSERT INTO stadt(nachname, vorname)
            SELECT code, nom
            FROM animal
            WHERE animal.code = 1721;
            