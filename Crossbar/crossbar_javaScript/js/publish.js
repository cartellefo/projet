

console.log('check publish');

var wsuri = "ws://localhost:8080/ws";

try {
   // for Node.js

   var autobahn = require('autobahn');
} catch (e) {
   // for browsers (where AutobahnJS is available globally)

}

//var autobahn = require('autobahn');

var connection = new autobahn.Connection({
   url: wsuri,
   realm: 'realm1'}
);

var counter ='publisher published to the tpoic';
connection.onopen = function (session) {

   // SUBSCRIBE to a topic and receive events
  data = [9,'adbi', 1268]
  // setInterval(function(){
	session.publish('repi.data.simple.gaussian', data);
    console.log("published to 'oncounter' with counter " + data);
    console.log("published to 'oncounter' with counter number");
    // counter = counter +1;
      


  // }, 3000) 
   
}



connection.open();

     