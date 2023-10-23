# Cloudwatch
  
Módulo para conectarse a AWS Cloudwatch  

*Read this in other languages: [English](Manual_Cloudwatch.md), [Português](Manual_Cloudwatch.pr.md), [Español](Manual_Cloudwatch.es.md)*
  
![banner](imgs/Banner_Cloudwatch.png o jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectarse a AWS
  
Este comando permite conectarse a tu cuenta de AWS, para ello necesitas tu Access Key Id y tu Secret Access Key, estos datos los puedes obtener en la consola de AWS, en la seccion de Security Credentials.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Access Key ID|Identificador de la cuenta de AWS|IKAMLSURT6HYUHRY48EF|
|Secret Access Key|Clave secreta de la cuenta de AWS|JYFifnrufd2pGHJ2illrZMVnhwxQnHSY5JK6JdhCtu|
|Region|Region de AWS|us-east-1|
|Asignar resultado a Variable|Variable donde se almacenara el estado de la conexion, devuelve True si es exitosa o False en el caso contrario|Variable|

### Crear Grupo de Log
  
Este comando permite crear un grupo de log en Cloudwatch. Debes contar con el permiso de IAM: "logs:CreateLogGroup"
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del grupo de log|Nombre del grupo de log a crear|new_log_group|
|Asignar resultado a Variable|Variable donde se almacenara el resultado, retorna True si es exitoso o False en caso contrario|Variable|

### Eliminar Grupo de Log
  
Este comando permite eliminar un grupo de log en Cloudwatch. Debes contar con el permiso de IAM: "logs:DescribeLogGroups"
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del grupo de log|Nombre del grupo de log a eliminar|log_group_name|
|Asignar resultado a Variable|Variable donde se almacenara el resultado, retorna True si es exitoso o False en caso contrario|Variable|

### Crear Flujo de Log
  
Este comando permite crear un flujo de log en Cloudwatch. Debes contar con el permiso de IAM: "logs:CreateLogStream"
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del grupo de log|Nombre del grupo de log donde se creara el flujo. Debe existir previamente.|log_group_name|
|Nombre del flujo de log|Nombre del flujo de log que se creara.|log_stream_name|
|Asignar resultado a Variable|Variable donde se almacenara el resultado, retorna True si es exitoso o False en caso contrario|Variable|

### Eliminar Flujo de Log
  
Este comando permite eliminar un flujo de log en Cloudwatch. Debes contar con el permiso de IAM: "logs:DescribeLogStreams".
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del grupo de log|Nombre del grupo de log donde se encuentra el flujo a eliminar. Debe existir previamente.|log_group_name|
|Nombre del flujo de log|Nombre del flujo de log que se desea eliminar.|log_stream_name|
|Asignar resultado a Variable|Variable donde se almacenara el resultado, retorna True si es exitoso o False en caso contrario|Variable|

### Cargar Eventos de Log
  
Este comando permite cargar eventos de log en un flujo de log en Cloudwatch. Debe tener permiso de IAM: "logs:PutLogEvents".
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del grupo de log|Nombre del grupo de log donde se encuentra el flujo.|log_group_name|
|Nombre del flujo de log|Nombre del flujo de log donde se desea colocar los eventos.|log_stream_name|
|Eventos de log|Eventos de log que se desea poner en el flujo.|[{
  "timestamp": 123456789,
  "message": "This is a test message"
}, {
  "timestamp": 123456789,
  "message": "This is another test message"
}]|
|Archivo de log de Rocketbot|Nombre del flujo de log que se desea obtener el token.|C:/Rocketbot/logs/log.txt|
|Asignar resultado a Variable|Variable donde se almacenara el resultado, retorna el token del flujo de log en caso de ejecutar correctamente o False en caso contrario.|Variable|

### Obtener Eventos de Log
  
Este comando permite obtener eventos de un flujo de log en Cloudwatch. Debe tener permiso IAM: "logs:GetLogEvents".
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del grupo de log|Nombre del grupo de log donde se encuentra el flujo.|log_group_name|
|Nombre del flujo de log|Nombre del flujo de log que se desea obtener los eventos.|log_stream_name|
|Asignar resultado a Variable|Variable donde se almacenara el resultado, retorna un diccionario con los eventos del flujo de log si se ejecuta correctamente o False caso contrario.|Variable|
