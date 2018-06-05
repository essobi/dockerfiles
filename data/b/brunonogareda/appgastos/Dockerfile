###################################################  
# DOCKERFILE PARA IMAXE DE APPGASTOS #  
###################################################  
FROM tomcat  
MAINTAINER bruno.nogareda <brunonogareda@gmail.com>  
  
ADD ./*.war /usr/local/tomcat/webapps/  
  
RUN echo "Europe/Madrid" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
# FROM, indicamos que imaxe utilizaremos de base,  
# en este caso unha máquina con un tomcat.  
# MAINTAINER, datos do autor da imaxe.  
# ADD, engadimos na imaxe a .war da aplicación directamente  
# na carpeta webapps do tomcat.  
# /path/ indicamos a ruta do ficheiro .war.  
# CMD, Comando por defecto para ser executado,  
# en este caso o propio tomcat.

