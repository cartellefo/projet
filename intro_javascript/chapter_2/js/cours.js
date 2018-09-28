
/*var a;
a = 3.14;
console.log(a);
var f = 100;
console.log("La variable f contient la valeur " + f);*/

/*console.log("Début du programme");
var nombre = 1;
while (nombre <= 5) {
    console.log(nombre);
    nombre++;
}
console.log("Fin du programme");*/


function direbonjour(){
	console.log("Bonjour !");
}

console.log("debut");
direbonjour()

function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

/**
 * Returns a random integer between min (inclusive) and max (inclusive)
 * Using Math.round() will give you a non-uniform distribution!
 */
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log(getRandomArbitrary(10,30))
console.log(getRandomInt(10,30))