# 📘 PokeApi – Consumo de API Externa

## 📌 Descripción del proyecto
Este proyecto corresponde a la **entrega final del Taller de Consumo de APIs Externas**, donde se consume la **PokeAPI**, una API pública que provee información sobre Pokémon.

La aplicación está desarrollada en **Python** y utiliza una **estructura modular**, separando responsabilidades en carpetas como controladores, servicios y cliente, siguiendo buenas prácticas de programación.

---

## 🎯 Objetivo
- Consumir una API pública real (PokeAPI).
- Aplicar la estructura base vista en clase.
- Separar la lógica del consumo de datos.
- Documentar correctamente el proyecto.

---

## 🧱 Estructura del proyecto
PokeApi/
│
├── clientela/ # Gestión del cliente de conexión a la API
├── controladores/ # Controladores de la aplicación
├── servicios/ # Lógica de negocio y consumo de la API
├── pycache/ # Archivos temporales generados por Python
│
├── ajustes de la aplicación.py # Configuración general del proyecto
├── principal.py # Archivo principal de ejecución
├── requisitos.txt # Dependencias del proyecto
├── .gitignore # Archivos ignorados por Git

---

## 5. API utilizada
- **Nombre:** PokeAPI  
- **Tipo:** API pública  
- **URL base:** https://pokeapi.co/  
- **Descripción:** Proporciona información sobre Pokémon, incluyendo estadísticas, tipos, habilidades y otros datos relevantes.

---

## 6. Requisitos del sistema
- Python 3.8 o superior
- Librerías indicadas en el archivo `requisitos.txt`

---

## 7. Instalación y ejecución
1. Clonar el repositorio:
```bash
git clone https://github.com/Marialeja20/PokeApi.git
Acceder al directorio del proyecto:

cd PokeApi


Crear y activar el entorno virtual:

python -m venv venv
.\venv\Scripts\activate


Instalar dependencias:

pip install -r requisitos.txt
Ejecutar la aplicación:

python principal.py

8. Funcionalidad del sistema

La aplicación permite realizar consultas a la PokeAPI, procesar la información obtenida y gestionarla mediante una estructura modular que facilita el mantenimiento y la escalabilidad del proyecto.

9. Autor

María Alejandra Pérez Banquez
Técnico Profesional en Programación de Computadoras
