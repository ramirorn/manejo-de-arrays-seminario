const prompt = require('prompt-sync')();

let cantidad_personas = parseInt(prompt("Ingrese la cantidad de personas: "));
let contador = 0;
let personas = [];
let suma = 0;

while (contador < cantidad_personas) {

    let persona = [];

    persona.push(prompt("Ingrese el nombre de la persona: "))
    persona.push(parseInt(prompt("Ingrese la edad de la persona: ")))
    persona.push(parseInt(prompt("Ingrese la nota de la persona: ")))

    personas.push(persona)

    contador++;
}

console.log("Lista de personas (en el orden que se ingresaron): ");

for (let persona of personas) {
    console.log(persona)
}

console.log("Lista de personas en la fila 0, columna 0 (nombre):");
console.log(personas[0][0]);

console.log("Personas ordenadas por nota de mayor a menor:");

let ordenados = [...personas].sort((a, b) => b[2] - a[2]);

for (let persona of ordenados) {
    console.log(persona);
}

for (let persona of personas) {
    suma = suma + persona[2];
}

console.log("La suma de las notas de las personas es:", suma);

let promedio = suma / cantidad_personas;

console.log("El promedio de las notas de las personas es:", promedio);