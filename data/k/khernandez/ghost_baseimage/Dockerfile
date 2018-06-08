#  
# Para usar phusion/baseimage como imagen base y construir nuestras imágenes  
# de forma que podamos reproducirla con seguridad, nos debemos asegurar que  
# utilizamos una versión específica de phusion/baseimage: NO USAR `latest`  
#  
# Para ver las versiones dispobnibles, puedes acceder a la siguiente URL  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
#  
FROM phusion/baseimage:0.9.15  
MAINTAINER Koldo Hernández <info@koldohernandez.com>  
  
  
# Inicializar las variables de entorno necesarias  
ENV HOME /root  
  
  
#  
# Si queremos acceder al container via SSH, debemos regenerar las claves SSH.  
# Por defecto, baseimage-docker no contiene ninguna por lo que debemos hacerlo
nosotros mismos.  
# Si comentamos esta instrucción, se generará una automáticamente al
inicializar el sistema (imagen).  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
#  
# Si queremos deshabilitar el acceso SSH comentamos esta linea  
#RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
# Utilizar el sistema de inicio de baseimage-docker (my_init)  
CMD ["/sbin/my_init"]  
  
# Instalo NodeJS y librerías del sistema utiles: cURL, zip, unzip  
RUN apt-get update && \  
apt-get install -y nodejs npm && \  
apt-get install -y curl && \  
apt-get install zip unzip  
  
# ... y creo el enlace simbólico para que funcione el comando "node" (esto
sucede por instalar NodeJS desde el gestor de paquetes)  
RUN ln -s /usr/bin/nodejs /usr/local/bin/node  
  
# Instalo Ghost. Para ello,  
# ... creo la carpeta donde va a ir el cms  
RUN cd /home && mkdir ghost  
WORKDIR /home/ghost  
  
# ... descargo Ghost  
RUN curl -L https://ghost.org/zip/ghost-latest.zip -o ghost.zip  
RUN unzip -uo ghost.zip -d ./  
RUN rm -f ghost.zip  
  
# ... creo el fichero config.js reemplazando 127.0.0.1 por 0.0.0.0  
RUN sed 's/127.0.0.1/0.0.0.0/' config.example.js > config.js  
  
# ... instalo las dependendias del proyecto  
RUN npm install --production  
  
# Pongo las variables de entorno que necesito  
ENV NODE_ENV production  
  
  
# Añado el script que arranca el servidor node  
ADD 01_start_ghost_server.sh /etc/my_init.d/01_start_ghost_server.sh  
RUN chmod +x /etc/my_init.d/01_start_ghost_server.sh  
  
# Expongo el puerto donde escucha Ghost  
EXPOSE 2368  
# Limpiar todos los archivos y temporales utilizados durante la instalación  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

