// const pg = require('pg');
// const pool = new pg.Pool({
// host: '127.0.0.1',
// database: 'postgres',
// port: '5432'});

// pool.query("SELECT NOW()", (err, res) => {
// console.log(err, res);
// pool.end();
// });

var express = require('express');
var pg = require("pg");
var app = express();

var connectionString = "postgres://localhost:5432/student";

// app.get('/', function (req, res, next) {
    pg.connect(connectionString,function(err,client,done) {
       if(err){
           console.log("not able to get connection "+ err);
           res.status(400).send(err);
       } 


        client.query('INSERT INTO Student (id ,name,rollnumber) values ($1,$2,$3)',[7,'ann iley',1005],function(err,result) {
           done(); // closing the connection;
           if(err){
               console.log(err);
               // res.status(400).send(err);
           }

           console.log(result.rows)
           // res.status(200).send(result.rows);
       });



       client.query('SELECT * FROM student',function(err,result) {
           done(); // closing the connection;
           if(err){
               console.log(err);
               // res.status(400).send(err);
           }

           console.log(result.rows)
           // res.status(200).send(result.rows);
       });




       //  client.query('CREATE TABLE items(id SERIAL PRIMARY KEY, text VARCHAR(40) not null, complete BOOLEAN)',function(err,result) {
       //     done(); // closing the connection;
       //     if(err){
       //         console.log(err);
       //         // res.status(400).send(err);
       //     }
       //      console.log(result)
       //     // res.status(200).send(result);
       // });


       // client.query('CREATE TABLE tab(id SERIAL PRIMARY KEY, text VARCHAR(40) not null, complete BOOLEAN)',function(err,result) {
       //     done(); // closing the connection;
       //     if(err){
       //         console.log(err);
       //         // res.status(400).send(err);
       //     }
       //      console.log(result)
       //     // res.status(200).send(result);
       // });









    });
// });

app.listen(4000, function () {
    console.log('Server is running.. on Port 4000');
});


