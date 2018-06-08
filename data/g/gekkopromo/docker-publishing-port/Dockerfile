FROM ubuntu:latest  
MAINTAINER Herve Meftah <dockerlite@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y apache2 && \  
apt-get clean  
  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  

