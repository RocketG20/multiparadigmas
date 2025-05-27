# Sistema de Recomendación de Películas 🎬

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Data Ready](https://img.shields.io/badge/Data-Ready-brightgreen)

## Características principales ✨

- 📊 **Carga automática** de `peliculas.csv` incluido en el repositorio
- 🔍 Filtrado por género con funciones puras
- 🏆 Sistema de ranking por calificación
- � Recomendaciones aleatorias
- ⚡ Operaciones asíncronas

## Instalación express ⚡ (3 pasos)

1. **Clonar y entrar al directorio**:
   ```bash
   git clone https://github.com/tu-usuario/recomendador-peliculas.git
   cd recomendador-peliculas
Ejecutar directamente (el sistema detectará automáticamente el archivo CSV):

bash
python recomendador.py
✅ El repositorio ya incluye peliculas.csv con datos de ejemplo 📌 NUEVO

Opcional: Para entorno virtual:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
pip install asyncio
Estructura actualizada del repositorio
recomendador-peliculas/
├── data/
│   └── peliculas.csv       # 📌 Datos incluidos (200+ películas de ejemplo)
├── recomendador.py         # Código principal
├── README.md               # Este archivo
└── .gitignore              # Archivos excluidos de Git
Personalización de datos ✏️
Si quieres usar tus propias películas:

Edita data/peliculas.csv manteniendo el formato:

csv
id,title,genre,year,rating
1,El Padrino,Crime,1972,9.2
2,Pulp Fiction,Crime,1994,8.9
El sistema detectará automáticamente los cambios al reiniciar

FAQ ❓ 📌 NUEVA SECCIÓN
P: ¿Qué hago si veo errores al cargar el CSV?
R: Verifica que:

El archivo esté en data/peliculas.csv

No tenga líneas vacías al final

Use codificación UTF-8

P: ¿Cómo añado más géneros?
R: Solo agrega nuevas películas con el género deseado en el CSV

Hecho por Guillermo Del Bosque G.
