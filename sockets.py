import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/3.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:                     # Bucle infinito para recibir datos
    data = mysock.recv(512)     # Recibe hasta 512 bytes de datos
    if len(data) < 1:           # Si no hay más datos, 
        break                   # salir del bucle   
    print(data.decode(),end='') # Decodifica y muestra los datos recibidos

mysock.close()

# ¿qué es un socket?
# Un socket es un punto final en una comunicación entre dos máquinas. Es una abstracción que permite a los programas enviar y recibir datos a través de una red.
# En términos más técnicos, un socket es una combinación de una dirección IP y un número de puerto que identifica de manera única una conexión de red específica.
# Los sockets son utilizados en la programación de redes para establecer conexiones entre clientes y servidores, permitiendo la transferencia de datos a través de protocolos como TCP (Transmission Control Protocol) y UDP (User Datagram Protocol).

# ¿se usan mucho?
# Sí, los sockets son ampliamente utilizados en la programación de redes y en el desarrollo de aplicaciones
# que requieren comunicación a través de una red. Son fundamentales para la creación de aplicaciones web, servicios en la nube, juegos en línea, aplicaciones de mensajería y muchas otras aplicaciones que dependen de la comunicación entre dispositivos.
# Los sockets proporcionan una forma flexible y eficiente de manejar la comunicación en red, lo que los hace esenciales en el desarrollo de software moderno.

# ¿la librería requests usa sockets?
# Sí, la librería requests en Python utiliza sockets internamente para manejar las conexiones de red.
# La librería requests es una biblioteca de alto nivel que simplifica el proceso de hacer solicitudes HTTP en Python.
# Detrás de escena, requests utiliza sockets para establecer conexiones TCP con los servidores web, enviar solicitudes HTTP y recibir respuestas.

# ¿la libreria requests es mejor que usar sockets directamente? ¿o son cosas diferentes?
# La librería requests es generalmente considerada mejor para la mayoría de los casos de uso en comparación con el uso directo de sockets, especialmente para desarrolladores que buscan simplicidad y facilidad de uso.
# Requests proporciona una interfaz de alto nivel que abstrae muchos de los detalles complejos asociados con el manejo de sockets, lo que facilita la realización de solicitudes HTTP y la gestión de respuestas.
# Sin embargo, hay situaciones en las que el uso directo de sockets puede ser necesario o preferible, como en aplicaciones que requieren un control muy fino sobre la comunicación de red o en protocolos personalizados que no son compatibles con HTTP.
# En resumen, requests es una herramienta poderosa y conveniente para la mayoría de las aplicaciones web, mientras que el uso directo de sockets puede ser más adecuado para casos específicos que requieren un control detallado sobre la comunicación de red.# ¿puedes mostrarme ejemplos de código de ambos enfoques?

# Ambos enfoques logran el mismo objetivo de obtener el contenido del archivo romeo.txt desde el servidor data.pr4e.org.

# ¿y cómo se maneja la comunicación entre varios lenguajes de programación usando sockets o requests?
# La comunicación entre varios lenguajes de programación utilizando sockets o requests se maneja a través de protocolos de red estándar, como HTTP, TCP/IP, UDP, etc. Aquí hay una explicación de cómo funciona en ambos casos:
# Usando sockets:
# Los sockets permiten la comunicación directa entre aplicaciones escritas en diferentes lenguajes de programación. Cada lenguaje puede crear sockets y establecer conexiones utilizando las mismas direcciones IP y números de puerto.
# Por ejemplo, una aplicación escrita en Python puede crear un socket servidor que escuche en un puerto específico, mientras que una aplicación escrita en Java puede crear un socket cliente que se conecte a ese puerto. Una vez establecida la conexión, ambas aplicaciones pueden enviar y recibir datos en un formato acordado (por ejemplo, JSON, XML, texto plano, etc.).
# Usando requests:

# La librería requests se utiliza principalmente para hacer solicitudes HTTP, lo que facilita la comunicación entre aplicaciones web escritas en diferentes lenguajes de programación.
# Por ejemplo, una aplicación web escrita en Python puede exponer una API RESTful que acepte solicitudes HTTP. Una aplicación escrita en JavaScript (por ejemplo, en un navegador web) puede usar fetch o XMLHttpRequest para hacer solicitudes a esa API. La comunicación se realiza a través de mensajes HTTP, y los datos se pueden intercambiar en formatos comunes como JSON o XML.
# En ambos casos, la clave para la comunicación entre diferentes lenguajes de programación es el uso de protocolos estándar y formatos de datos comunes que ambos lados puedan entender.
# Aquí tienes un ejemplo simple de comunicación entre una aplicación Python y una aplicación JavaScript usando requests


# En este ejemplo, la aplicación Python actúa como un servidor API que responde a las solicitudes HTTP, mientras que la aplicación JavaScript actúa como un cliente que realiza solicitudes a esa API y procesa la respuesta.