También hay un atajo de línea de comandos para ejecutar testmod(). Puedes instruir al intérprete de Python para ejecutar el módulo doctest directamente de la biblioteca estándar y pasar los nombres del módulo en la línea de comandos:

python -m doctest -v example.py
Esto importará example.py como un módulo independiente y ejecutará a testmod(). Note que esto puede no funcionar correctamente si el archivo es parte de un paquete e importa otros submódulos de ese paquete.