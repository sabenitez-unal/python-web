import xml.etree.ElementTree as et
import urllib.request

url = input("Give me the URL: ")
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_2370453.xml"

print(f"Retrieving {url}")

xml_document = urllib.request.urlopen(url).read()

with open("document.xml", "wb") as document:
    document.write(xml_document)

print(f"Retrieved {len(xml_document)} characters")

with open("document.xml", "r") as document:
    xml = et.parse(document)

counts = xml.findall(".//count")

suma = 0
for count in counts:
    suma += int(count.text) # type: ignore

print(f"Result: {suma}")


# Qué es DevOps?
# DevOps es un conjunto de prácticas que combina el desarrollo de software (Dev) y las
# operaciones de tecnología de la información (Ops). El objetivo de DevOps es acortar el ciclo de vida del desarrollo de software y proporcionar una entrega continua con alta calidad. DevOps se basa en la colaboración, la automatización y la integración entre los equipos de desarrollo y operaciones para mejorar la eficiencia y la confiabilidad en la entrega de software.
# Las prácticas de DevOps incluyen la integración continua, la entrega continua, la automatización de pruebas, la gestión de la configuración, el monitoreo y la retroalimentación continua. Al adoptar
# DevOps, las organizaciones pueden acelerar la entrega de software, mejorar la calidad del producto y aumentar la satisfacción del cliente.

# Como trabaja un equipo de desarrollo de software con un equipo de operaciones?
# Un equipo de desarrollo de software y un equipo de operaciones trabajan juntos en un entorno DevOps para lograr una entrega continua de software de alta calidad. La colaboración entre ambos equipos es fundamental para el éxito de DevOps. Aquí hay algunas formas en que estos equipos trabajan juntos:
# 1. Comunicación y colaboración: Los equipos de desarrollo y operaciones deben comunicarse de manera efectiva y colaborar estrechamente. Esto puede incluir reuniones regulares, herramientas de comunicación compartidas y la creación de un ambiente de trabajo colaborativo.
# 2. Integración continua: El equipo de desarrollo implementa prácticas de integración continua, donde el código se integra y prueba automáticamente en un entorno compartido. Esto permite detectar y resolver problemas de manera temprana, lo que mejora la calidad del software.
# 3. Entrega continua: El equipo de operaciones se encarga de la entrega continua, donde el software se despliega automáticamente en un entorno de producción después de pasar las pruebas. Esto permite una entrega rápida y confiable del software a los usuarios finales.
# 4. Automatización: Ambos equipos trabajan juntos para automatizar tareas repetitivas, como pruebas, despliegues y monitoreo. La automatización ayuda a reducir errores humanos, aumentar la eficiencia y acelerar el proceso de entrega de software.
# 5. Retroalimentación continua: Los equipos de desarrollo y operaciones deben proporcionar retroalimentación continua entre sí. Esto puede incluir la recopilación de métricas de rendimiento
# y la identificación de áreas de mejora en el proceso de desarrollo y operaciones. La retroalimentación continua ayuda a mejorar la calidad del software y a optimizar el proceso de entrega.

# ¿qué hace una persona que sólo está en el equipo de desarrollo?
# Una persona que solo está en el equipo de desarrollo se enfoca principalmente en la creación y el mantenimiento del software. Sus responsabilidades pueden incluir:
# 1. Escribir código: El desarrollador se encarga de escribir el código fuente del software, utilizando lenguajes de programación y herramientas de desarrollo.
# 2. Diseñar la arquitectura del software: El desarrollador puede participar en el diseño de la arquitectura del software, definiendo cómo se estructurará el código y cómo interactuarán los diferentes componentes del software.
# 3. Realizar pruebas: El desarrollador puede escribir pruebas unitarias y de integración para asegurarse de que el software funcione correctamente y cumpla con los requisitos establecidos.
# 4. Colaborar con otros desarrolladores: El desarrollador puede colaborar con otros miembros del equipo de desarrollo, compartiendo conocimientos, revisando el código y trabajando juntos para resolver problemas y mejorar el software.
# 5. Participar en la planificación del proyecto: El desarrollador puede participar en la planificación del proyecto, estimando el tiempo necesario para completar las tareas de desarrollo y contribuyendo a la definición de los objetivos del proyecto.
# En resumen, una persona que solo está en el equipo de desarrollo se enfoca en la creación y el mantenimiento del software, trabajando en estrecha colaboración con otros desarrolladores para garantizar la calidad y el éxito del proyecto de software.

# ¿qué hace una persona que sólo está en el equipo de operaciones?
# Una persona que solo está en el equipo de operaciones se enfoca principalmente en la gestión y el mantenimiento de la infraestructura tecnológica necesaria para el funcionamiento del software. Sus responsabilidades pueden incluir:
# 1. Configuración y administración de servidores: El profesional de operaciones se encarga de configurar y administrar los servidores donde se ejecuta el software, asegurándose de que estén disponibles, seguros y optimizados para el rendimiento.
# 2. Despliegue de software: El profesional de operaciones se encarga de desplegar el software en los entornos de producción, asegurándose de que el proceso de despliegue sea eficiente, confiable y sin interrupciones para los usuarios finales.
# 3. Monitoreo y mantenimiento: El profesional de operaciones monitorea el rendimiento del software en producción, identificando y resolviendo problemas de rendimiento, disponibilidad y seguridad. También se encarga del mantenimiento de la infraestructura tecnológica, aplicando actualizaciones y parches según sea necesario.
# 4. Gestión de la configuración: El profesional de operaciones se encarga de gestionar la configuración de los sistemas y aplicaciones, asegurándose de que estén correctamente configurados y documentados para facilitar la gestión y el mantenimiento.
# 5. Colaboración con el equipo de desarrollo: El profesional de operaciones colabora con el equipo de desarrollo para garantizar que el software se despliegue y funcione correctamente en los entornos de producción, proporcionando retroalimentación sobre el rendimiento y la estabilidad del software y trabajando juntos para resolver problemas y mejorar la calidad del software.
# En resumen, una persona que solo está en el equipo de operaciones se enfoca en la gestión y el mantenimiento de la infraestructura tecnológica, asegurándose de que el software se despliegue y funcione correctamente en los entornos de producción, trabajando en estrecha colaboración con el equipo de desarrollo para garantizar la calidad y el éxito del proyecto de software.

# ¿qué hace una persona que está en ambos equipos?
# Una persona que está en ambos equipos, es decir, en el equipo de desarrollo y en el equipo de operaciones, se conoce comúnmente como un ingeniero DevOps. Este profesional tiene responsabilidades tanto en el desarrollo de software como en la gestión de la infraestructura tecnológica. Sus responsabilidades pueden incluir:
# 1. Escribir código: El ingeniero DevOps puede escribir código para desarrollar nuevas funcionalidades, corregir errores y mejorar el software, al igual que un desarrollador tradicional.
# 2. Configuración y administración de servidores: El ingeniero DevOps también se encarga de configurar y administrar los servidores donde se ejecuta el software, asegurándose de que estén disponibles, seguros y optimizados para el rendimiento, al igual que un profesional de operaciones tradicional.
# 3. Automatización: El ingeniero DevOps se enfoca en la automatización de tareas repetitivas, como pruebas, despliegues y monitoreo, para mejorar la eficiencia y reducir los errores humanos en el proceso de entrega de software.
# 4. Colaboración y comunicación: El ingeniero DevOps colabora estrechamente con ambos equipos, facilitando la comunicación y la colaboración entre el equipo de desarrollo y el equipo de operaciones para garantizar una entrega continua de software de alta calidad.
# 5. Monitoreo y retroalimentación: El ingeniero DevOps monitorea el rendimiento del software en producción, identificando y resolviendo problemas de rendimiento, disponibilidad y seguridad, y proporciona retroalimentación continua al equipo de desarrollo para mejorar la calidad del software.
# En resumen, una persona que está en ambos equipos, como un ingeniero DevOps, tiene responsabilidades tanto en el desarrollo de software como en la gestión de la infraestructura tecnológica, trabajando en estrecha colaboración con ambos equipos para garantizar la calidad y el éxito del proyecto de software.

# ¿en cuál de los 3 roles es más fácil encontrar trabajo?
# La facilidad para encontrar trabajo en los roles de desarrollo, operaciones o DevOps puede variar según la demanda del mercado laboral, las habilidades requeridas y la experiencia del candidato. Sin embargo, en general, el rol de DevOps ha experimentado un crecimiento significativo en los últimos años debido a la creciente adopción de prácticas DevOps en las organizaciones. Esto ha llevado a una alta demanda de ingen
# ieros DevOps que puedan combinar habilidades de desarrollo y operaciones para mejorar la eficiencia y la calidad en la entrega de software. Por lo tanto, es posible que sea más fácil encontrar trabajo en el rol de DevOps en comparación con los roles de desarrollo o operaciones tradicionales, aunque esto puede variar según la ubicación geográfica y el mercado laboral específico. Es importante destacar que cada rol tiene su propia demanda y oportunidades laborales, por lo que es recomendable investigar el mercado laboral local y desarrollar las habilidades necesarias para el rol deseado.

# ¿en cuál de los 3 roles se valora más un ingeniero de sistemas titulado?
# La valoración de un ingeniero de sistemas titulado puede variar según la empresa, la industria y el mercado laboral específico. Sin embargo, en general, un ingeniero de sistemas titulado puede ser valorado en los roles de desarrollo, operaciones y DevOps, dependiendo de las habilidades y experiencias del individuo. En el rol de desarrollo, un ingeniero de sistemas titulado puede ser valor
# ado por su conocimiento en diseño de software, arquitectura y habilidades de programación. En el rol de operaciones, un ingeniero de sistemas titulado puede ser valorado por su conocimiento en administración de sistemas, redes y seguridad. En el rol de DevOps, un ingeniero de sistemas titulado puede ser valorado por su capacidad para combinar habilidades de desarrollo y operaciones, así como por su conocimiento en automatización y gestión de la infraestructura tecnológica. En última instancia, la valoración de un ingeniero de sistemas titulado dependerá de las necesidades específicas de la empresa y del mercado laboral en el que se encuentre.

# ¿en cuál de los 3 roles se valora más un ingeniero de sistemas sin título?
# La valoración de un ingeniero de sistemas sin título puede variar según la empresa, la industria y el mercado laboral específico. En general, aunque un título puede ser un factor importante para algunas empresas
#, muchas organizaciones también valoran la experiencia práctica, las habilidades técnicas y la capacidad de resolver problemas en los roles de desarrollo, operaciones y DevOps. En el rol de desarrollo, 
# un ingeniero de sistemas sin título puede ser valorado por su habilidad para escribir código, diseñar software y colaborar con otros desarrolladores. En el rol de operaciones, un ingeniero de sistemas sin título puede ser valorado por su experiencia en administración de sistemas, redes y seguridad. En el rol de DevOps, un ingeniero de sistemas sin título puede ser valorado por su capacidad para combinar habilidades de desarrollo y operaciones, así como por su experiencia en automatización y gestión de la infraestructura tecnológica. En última instancia, la valoración de un ingeniero de sistemas sin título dependerá de las necesidades específicas de la empresa y del mercado laboral en el que se encuentre.7

# ¿en cuál de los 3 roles se gana más dinero?
# La remuneración en los roles de desarrollo, operaciones y DevOps puede variar significativamente según la ubicación geográfica, la industria, el nivel de experiencia y las habilidades específicas del individuo. Sin embargo
#, en general, los roles de DevOps tienden a tener una remuneración más alta en comparación con los roles de desarrollo y operaciones tradicionales debido a la creciente demanda de profesionales con habilidades combinadas en desarrollo y operaciones. Los ingenieros DevOps suelen ser valorados por su capacidad para mejorar la eficiencia y la calidad en la entrega de software, lo que puede llevar a una mayor remuneración. Sin embargo, es importante destacar que la remuneración puede variar ampliamente según el mercado laboral específico y las circunstancias individuales, por lo que es recomendable investigar el mercado laboral local para obtener información más precisa sobre los salarios en cada rol.

# ¿es positivo que desde la mitad de la carrera de ingeniería de sistemas, me empiece a preparar para el rol de DevOps?
# Sí, es positivo que desde la mitad de la carrera de ingeniería de sistemas te empieces a preparar para el rol de DevOps. El rol de DevOps es cada vez más demandado en la industria tecnológica, y tener habilidades y conocimientos en esta área puede abrir muchas oportunidades laborales. Al prepararte para el rol de DevOps desde temprano en tu carrera, puedes adquirir habilidades técnicas en desarrollo, operaciones y automatización, lo que te hará un candidato más competitivo en el mercado laboral. Además, el rol de DevOps te permitirá trabajar en proyectos emocionantes y desafiantes, colaborando con equipos multidisciplinarios para mejorar la eficiencia y la calidad en la entrega de software. En resumen, prepararte para el rol de DevOps desde la mitad de tu carrera de ingeniería de sistemas es una excelente decisión que puede beneficiarte a largo plazo en tu desarrollo profesional.

# ¿qué persona dentro de qué equipo es quien sabe manejar contenedores y orquestadores?
# La persona que sabe manejar contenedores y orquestadores generalmente se encuentra en el equipo de DevOps. Los contenedores, como Docker, y los orquestadores, como Kubernetes,
# son herramientas clave en el rol de DevOps para facilitar la automatización, el despliegue y la gestión de aplicaciones en entornos de producción. Un ingeniero DevOps con experiencia en contenedores y orquestadores puede diseñar, implementar y mantener infraestructuras basadas en contenedores, así como configurar y administrar orquestadores para garantizar la escalabilidad, la disponibilidad y la eficiencia de las aplicaciones. Aunque algunos miembros del equipo de desarrollo o operaciones también pueden tener conocimientos en contenedores y orquestadores, es más común que esta experiencia se encuentre en el equipo de DevOps debido a su enfoque en la integración de desarrollo y operaciones.

# ¿enlista los roles de cada uno de los 3 equipos?
# Claro, aquí tienes una lista de roles comunes en cada uno de los tres equipos:
# Equipo de Desarrollo:
# 1. Desarrollador de Software
# 2. Ingeniero de Software
# 3. Arquitecto de Software
# 4. Analista de Requisitos
# 5. Tester de Software
# Equipo de Operaciones:
# 1. Administrador de Sistemas
# 2. Ingeniero de Operaciones
# 3. Especialista en Redes
# 4. Ingeniero de Seguridad
# 5. Administrador de Base de Datos
# Equipo de DevOps:
# 1. Ingeniero DevOps
# 2. Especialista en Automatización
# 3. Ingeniero de Infraestructura
# 4. Ingeniero de Contenedores
# 5. Ingeniero de Orquestación

# ¿qué habilidades técnicas se necesitan para cada uno de los 3 roles?
# Aquí tienes una lista de habilidades técnicas comunes para cada uno de los tres roles:
# Habilidades técnicas para el rol de Desarrollo:
# 1. Lenguajes de programación (por ejemplo, Python, Java, C++)
# 2. Frameworks de desarrollo (por ejemplo, Django, Spring)
# 3. Control de versiones (por ejemplo, Git)
# 4. Diseño de software y arquitectura
# 5. Pruebas unitarias y de integración
# Habilidades técnicas para el rol de Operaciones:
# 1. Administración de sistemas operativos (por ejemplo, Linux, Windows)
# 2. Redes y protocolos de comunicación
# 3. Seguridad informática
# 4. Automatización de tareas (por ejemplo, Ansible, Puppet)
# 5. Monitoreo y gestión de infraestructura (por ejemplo, Nagios, Prometheus)
# Habilidades técnicas para el rol de DevOps:
# 1. Conocimientos en desarrollo de software y operaciones
# 2. Automatización de procesos (por ejemplo, Jenkins, Travis CI)
# 3. Contenedores (por ejemplo, Docker)
# 4. Orquestadores (por ejemplo, Kubernetes)
# 5. Infraestructura como código (por ejemplo, Terraform)

# Es decir, el DevOps debe saber un poco de los otros dos roles, pero no necesariamente ser un experto en ninguno de los dos, 
# sino tener un conocimiento general de ambos para poder integrar y automatizar los procesos de desarrollo y operaciones de manera efectiva. 
# El rol de DevOps se enfoca en la colaboración y la integración entre los equipos de desarrollo y operaciones, por lo que es importante tener 
# habilidades técnicas en ambas áreas para poder facilitar la entrega continua de software de alta calidad.

# ¿qué habilidades técnicas NO se necesitan para cada uno de los 3 roles?
# Aquí tienes una lista de habilidades técnicas que generalmente no se necesitan para cada uno de los tres roles:
# Habilidades técnicas que NO se necesitan para el rol de Desarrollo:
# 1. Administración de sistemas operativos
# 2. Redes y protocolos de comunicación
# 3. Seguridad informática
# 4. Automatización de tareas de operaciones
# 5. Monitoreo y gestión de infraestructura
# Habilidades técnicas que NO se necesitan para el rol de Operaciones:
# 1. Lenguajes de programación avanzados
# 2. Frameworks de desarrollo
# 3. Diseño de software y arquitectura
# 4. Pruebas unitarias y de integración
# 5. Control de versiones
# Habilidades técnicas que NO se necesitan para el rol de DevOps:
# 1. Conocimientos profundos en lenguajes de programación específicos
# 2. Diseño de software y arquitectura avanzada
# 3. Administración de sistemas operativos a nivel experto
# 4. Redes y protocolos de comunicación avanzados
# 5. Seguridad informática a nivel experto
# Es importante destacar que estas listas son generales y pueden variar según la empresa, la industria y el mercado laboral específico. En algunos casos, puede haber roles híbridos o específicos que requieran habilidades

# En pocas palabras... ¿el devops hace que el equipo de desarrollo y el de TI y operaciones dejen de pelear?
