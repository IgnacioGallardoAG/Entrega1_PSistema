# Entrega1_PSistema

Indicaciones para ejecutar el código
1.- Abrir Pycharm
2.- Revisar que las librerías estén, en caso de no estar instaladas, hacer lo siguiente:
- Entrar a settings
- En la parte del nombre del proyecto clickear y elegir la opción "Python Interpreter"
- Luego verificar que está usando la versión de Python 3.12 (para evitar conflictos)
- Instalar las siguientes librerías:
-   grpcio (protobuf debería instalarse en conjunto, en caso de no hacerlo instalarlo)
-   grpcio-tools
-   geopy (geographiclib	2.0	2.0 debería instalarse en conjunto, en caso de no hacerlo instalarlo)
-   setuptools

3.- Se debe trabajar con 2 terminales:
- La primera terminal destinada a levantar el servicio mediante el comando "python distance_grpc_service.py"
- La segunda terminal se deberá ejecutar el archivo "pruebas.py" mediante el comando "python -m unittest pruebas_prototipo.pruebas"

y ya con eso debería funcionar todo correctamente
