Link del Repositorio
https://github.com/hartor8019/DPIAS1

****** Paso # 1:  Creacion del proyecto ******
- Una vez creado el proyecto se debe de crear una subcarpeta llamada src
- En la subcarpeta src se deben de copiar los archivos (main_students.py) y (IMDB top 1000.csv) este ultimo es el dataset

****** Paso # 2: Este proyecto se ejecuto en un entorno virtual con Virtualenv por lo que es necesario instalarlo ******

* Primero se debe revisar si la version de Python instalada cuenta con virtualenv el comando es pip list (Buscar virtualenv)
* Si no se visualiza en la lista, es posible instalarla con el siguiente comando " virtualenv -p python3 env "
* Lo anterior creara un nuevo directorio en el proyecto llamado env (este contiene una gran cantidad de utilidades)
* El paso siguiente es activar nuestro entorno virtual con el siguiente comando : .\env\Scripts\activate
* Una vez el entorno este activado veremos al inicio del prompt algo asi (env) PS C:\Users\USUARIO\proyectosem1> donde (env) indica que ya estamos dentro de nuestro entorno.
* El siguiente paso es instalar las librerias de pandas y sentence-transformers con los siguientes comandos (pip install sentence-transformers) - (pip install pandas ).
  
***** Ejecucion del Proyecto *****

Una ves se hayan realizado los puntos anteriores podemos proceder con la ejecucion del proyecto, para ello debemos ejecutar el siguiente comando python .\src\main_students.py
debemos asegurarnos que nos encontramos con el entorno inicializado. 

#Comando para la ejecucion del proyecto
python .\src\main_students.py



