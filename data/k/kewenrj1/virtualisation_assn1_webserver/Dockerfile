#Linux Distro  
FROM ubuntu:14.04  
#Dockerfile Maintainer  
MAINTAINER Rickie Kewene <kewenrj1@student.op.ac.nz>  
  
LABEL Last-modified="08/09/2015"  
  
#Update and Upgrade  
RUN apt-get -yqq update  
RUN apt-get -yqq upgrade  
  
#Install Apache  
RUN apt-get -yqq install apache2  
  
#Set Volume and Working Directory  
WORKDIR /var/www/html  
  
#Apache Commands  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
  
#Apache Specific Directories  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
  
#Expose the port  
EXPOSE 80  
#Run for Apache  
ENTRYPOINT ["/usr/sbin/apache2"]  
CMD ["-D", "FOREGROUND"]  
  
## Ref: https://docs.docker.com/articles/using_supervisord/ ##  

