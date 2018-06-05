FROM debian:latest  
MAINTAINER Alberto Gonzalez <alberto@oforte.net>  
# Instalar apache2 y configurar locales  
RUN apt-get update && apt-get install -y locales locales-all apache2 curl  
RUN locale-gen es_ES.UTF-8  
EXPOSE 80  
VOLUME /var/www  
# Variables para Apache 2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
# Contenido web  
VOLUME /var/www/html/  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

