# carranza-TuPrimeraPagina
1- El primer paso de este proyecto fue clonar el repositorio de GitHub en vscode.
2- Luego genere el .gitignore.
3- Cree la carpeta .venv y la active.
4- Cree la carpeta carranza_tuprimerapagina y levanté el entorno.
5- Separo las funcionalidades creando una aplicación (appcasa).
6- Por defecto el proyecto no la va a reconocer 100% a la aplicación, entonces voy a INSTALLED_APP y agregue mi aplicación a la lista.
7- Despues configuro la URL, que es por donde el usuario ingresa.
8- Hay que agregar el templates, dentro se puede crear un archivo con el nombre de la vista + .html.
9- Si tenemos varias aplicaciones en la carpeta de templates puede ser tedioso. Lo que hay que hacer es detntro de la aplicación crear una carpeta que se llame templates y ahí pasas los que necesitas.
10- Para poder poner el html se puede hacer poniendo, html:5 o ! + enter.
11- Dentro de la aplicación, vamos a models.py. Axá es donde se trabajan losc´digos.
12- En models.py se crea el modelo de datos.
13- Para que exista: Migración que indique que creamos un modelo (usando: python manage.py makamigrations) y luego, ya con la migración, plasme lo que tiene esta migración en la base (usando: python manage.py migrate)
14- Luego se crea una etiqueta form, donde creamos el html de nuestro proyecto.
15- Trabajando con los input desde html, tenemos poca seguridad. Cuando usamos POST por defecto Django necesita un token de seugridad ({% csrf_token %}).
16- Dentro de la aplicación creamos un archivos que se llame form.py. 
17- Para pasar la info a un template, lo hago a traves de un contexto.
18- Para que detecte que es algo que se pasa por contexto se usa {{formulario}}.
19- Para que el listado no pase todo y nos pasen lo que hay, hay que pedirle a la base de datos todos los que tenga.
