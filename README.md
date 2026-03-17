# Manejo de Arrays - Seminario

Este proyecto contiene dos implementaciones del mismo programa: una en JavaScript (Node.js) y otra en Python.

## Requisitos Previos

### Para ejecutar la versión en JavaScript

- **Node.js** instalado en tu sistema (versión 12 o superior)
  - Descárgalo desde: [nodejs.org](https://nodejs.org)

### Para ejecutar la versión en Python

- **Python** instalado en tu sistema (versión 3.6 o superior)
  - Descárgalo desde: [python.org](https://www.python.org)

## Instalación

### Paso 1: Clonar o descargar el proyecto

Descarga el repositorio en tu computadora.

### Paso 2: Instalar las dependencias de Node.js

Si deseas ejecutar la versión en JavaScript, necesitas instalar el paquete `prompt-sync`:

```bash
npm install
```

Este comando instalará automáticamente el paquete `prompt-sync` especificado en el archivo `package.json`.

**Nota:** Si no tienes npm instalado, asegúrate de tener Node.js instalado correctamente en tu sistema.

## Uso

### Ejecutar la versión en JavaScript

```bash
node main.js
```

El programa te pedirá:

1. La cantidad de personas que vas a ingresar
2. Para cada persona:
   - Nombre
   - Edad
   - Nota

Luego mostrará:

- Lista de personas en el orden ingresado
- El nombre de la primera persona
- Personas ordenadas por nota (de mayor a menor)
- Suma total de notas
- Promedio de notas

### Ejecutar la versión en Python

```bash
python main.py
```

O si tienes Python 3:

```bash
python3 main.py
```

El programa solicitará los mismos datos que la versión JavaScript y mostrará los mismos resultados.

## Estructura del Proyecto

- `main.js` - Implementación en JavaScript
- `main.py` - Implementación en Python
- `package.json` - Configuración de dependencias de Node.js
- `README.md` - Este archivo de instrucciones

## Dependencias

- **prompt-sync** - Librería para capturar entrada del usuario en Node.js
