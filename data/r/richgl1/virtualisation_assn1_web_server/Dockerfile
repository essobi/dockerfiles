#Web_Server#  
#Ubuntu Distro and Version 14.04  
FROM ubuntu:14.04  
#Maintainer  
MAINTAINER Glenn Richardz "richgl1@student.op.ac.nz"  
# Update and Upgrade  
RUN apt-get -yqq update  
RUN apt-get -yqq upgrade  
  
# Installs Apache2 and Supervisor  
RUN apt-get -yqq install apache2  
RUN apt-get -yqq install supervisor  
  
#Configure the www Directory  
WORKDIR /var/www/html  
  
#Apache Specific Commands  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
  
#Apache Specific Directories & OpensPort 80  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
EXPOSE 80  
#Entrypoint  
ENTRYPOINT [ "/bin/sh", "-c", "/usr/sbin/apache2 -D FOREGROUND" ]  

