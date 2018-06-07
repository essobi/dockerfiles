#Origin: Ubuntu 14.04 LTS  
FROM ubuntu:14.04  
  
#Actualizar el repositorio Ubuntu, luego descarga e instala paquetes que  
#requieren actualizacion.  
RUN apt-get -qq update && apt-get -qqy upgrade  
  
#Instalar algunos paquetes bases, utiles para mi y algunas dependencias.  
RUN apt-get -qqy install \  
wget \  
git \  
curl \  
python \  
lamp-server^  
  
  
RUN mkdir /var/www/html/logs  
RUN chmod o+w /var/www/html/logs  
RUN mkdir /var/www/html/data  
RUN mkdir /var/www/html/config  
RUN a2enmod rewrite  
  
# Set AllowOverride  
RUN cp /etc/apache2/apache2.conf /etc/apache2/apache2.conf.orig  
RUN /bin/bash -c "sed -i '166s/None/All/' /etc/apache2/apache2.conf"  
# Exposing ports  
EXPOSE 80 22 3306  
  
# CMD /bin/bash  

