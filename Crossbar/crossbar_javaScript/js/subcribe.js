
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
      var msg = args[0];
      console.log("event for 'onhello' received: " + msg);
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


