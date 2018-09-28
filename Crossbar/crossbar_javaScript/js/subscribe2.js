
var pg = require("pg");
var connectionString = "postgres://localhost:5432/student";


var wsuri = "ws://localhost:8080/ws";
console.log('subcribe call')
try {
   // for Node.js

   var autobahn = require('autobahn');
} catch (e) {
   // for browsers (where AutobahnJS is available globally)

}

//var autobahn = require('autobahn');


//var autobahn = require('autobahn');

var connection = new autobahn.Connection({
   url: wsuri,
   realm: 'realm1'}
); 

connection.onopen = function (session) {

   
   function onhello (args) {
      var data = args;
      console.log(data);




      pg.connect(connectionString,function(err,client,done) {
       if(err){
           console.log("not able to get connection "+ err);
           res.status(400).send(err);
       } 
       
       for (var i = 0; i == 100; i++) {

           client.query('INSERT INTO Student (id ,name,rollnumber) values ($1,$2,$3)', data, function(err,result) {
             done(); // closing the connection;
             if(err){
                 console.log(err);
                 // res.status(400).send(err);
             }

             console.log(result.rows)
             // res.status(200).send(result.rows);
          });

         
       }

        





         client.query('SELECT * FROM student',function(err,result) {
           done(); // closing the connection;
           if(err){
               console.log(err);
               // res.status(400).send(err);
           }

           console.log(result.rows)
           // res.status(200).send(result.rows);
       });



   
});
    }


   session.subscribe('repi.data.simple.gaussian', onhello).then(
      function (sub) {
         console.log("subscribed to topic 'onhello'");
      },
      function (err) {
         console.log("failed to subscribed: " + err);
      }
   );


}
connection.open();


