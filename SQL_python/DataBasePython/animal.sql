CREATE TABLE IF NOT EXISTS animal(
        animal_key serial,
       variety varchar,
        sex char(3),
        date_of_birth timestamptz,
        name varchar,
        code integer,
        comments text
    );
    
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('owlet','F','08/06/2008 08:26 PM','system',5022,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('mouse','M','03/16/2008 01:38 PM','history',5706,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('pork','M','03/08/2008 10:31 PM','world',845,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('bird','F','05/16/2008 05:08 AM','method',568,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('lamb','F','03/10/2008 06:38 AM','health',1534,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('pork','M','07/06/2008 01:16 AM','art',740,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('elefant','F','09/15/2008 06:19 AM','system',6648,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('cat','M','11/02/2008 11:05 AM','world',1931,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('lamb','F','09/15/2008 06:28 PM','way',9184,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('lamb','M','11/12/2008 05:09 PM','health',5814,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('owlet','M','10/03/2008 05:12 AM','year',8494,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('parrot','M','07/09/2008 04:18 PM','method',7851,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('turtle','F','09/16/2008 02:27 AM','two',4964,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('lizard','F','08/11/2008 06:39 PM','history',8904,'none');
INSERT INTO animal (variety, sex, date_of_birth, name, code, comments) VALUES ('elefant','M','11/02/2008 12:19 PM','data',1053,'none');