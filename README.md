# Web-de-Gestion-Disciplinaria

## Pagina web destinada a brindar solucion al proyecto final conjunto de las asignaturas ISW-2 y P5.

# Tecnologias:

- Django 3.2.9  
- Bulma 0.9.3  
- Font-Awesome 5.15.4  
- Widget tweaks 
- Alpine.js
- Iodine.js

## Pasos

# Paso 1 :

Correr migraciones:
`
python manage.py migrate
`

# Paso 2 :

Crear super usuario para acceder a la pagina.

`
python manage.py createsuperuser
`

Dadas las restricciones del negocio el superusuario debia ser credo programaticamente y seria el encargado de introducir los datos en el sistema.


# Paso 3 :

Correr el servidor

`
python manage.py runserver
`

# Paso 4 :

Agregar datos desde el panel de admin.
Viajamos al localhost:port/admin y creamos un perfil para el superusuario dado que el superusuario no necesariamente debe tener un perfil.