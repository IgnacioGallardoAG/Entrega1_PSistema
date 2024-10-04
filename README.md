# Entrega1_PSistema

## Indicaciones para ejecutar el código

1. Abrir Pycharm.
2. Revisar que las librerías estén instaladas:
   - Si no están instaladas, hacer lo siguiente:
     1. Entrar a `Settings`.
     2. En la parte del nombre del proyecto, clickear y elegir la opción "Python Interpreter".
     3. Luego, verificar que está usando la versión de **Python 3.12**.
     4. Instalar las siguientes librerías:
        - `grpcio` (protobuf debería instalarse en conjunto, en caso de no ser así instalarlo).
        - `grpcio-tools`.
        - `geopy` (`geographiclib` debería instalarse en conjunto, en caso de no ser así instalarlo).
        - `setuptools`.

3.- Se debe trabajar con 2 terminales:
- La primera terminal destinada a levantar el servicio mediante el comando "python distance_grpc_service.py"
- La segunda terminal se deberá ejecutar el archivo "pruebas.py" mediante el comando "python -m unittest pruebas_prototipo.pruebas"

## Notas adicionales

- Verificar las configuraciones antes de ejecutar las pruebas.
- Asegurarse de que el servicio gRPC esté corriendo antes de lanzar las pruebas.
