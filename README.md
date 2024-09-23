## instalacio 
    1- clona el repositorio
        git clone <https://github.com/chaloS67/blog.git>

    2- Crea y activa un entorno virtual
        python -m venv env
        source env/bin/activate  
        # En Windows: env\Scripts\activate

    3- Instala las dependencias
        pip install -r requirements.txt

    4- Realiza las migraciones de la base de datos:
        python manage.py migrate

    5- Ejecuta el servidor
        python manage.py runserver

    6- Abre tu navegador y navega http://localhost:8000 o al puerto que le asignes

## Uso

    - En la pantalla principal ir hasta iniciar sesion
    - Registrarte con nombre de usuario y contraseña - (las comprobaciones de la contraseña estan desabilitadas)
    - Una vez que tu nombre salga en la pantalla azul ya estas habilitado para usar la aplicacion
    - Dirigirse hacia crear
    - Escribe un post
    - Para listar nos dirigimos a "listar" esto nos va a dar un listado de los mensajes en este listado se encuentran las opcion de "editar" , "eliminar","detalle" elige cual desees.



    