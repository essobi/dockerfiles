FROM library/ubuntu:14.04  
FROM python:2.7  
  
COPY /. /.  
COPY /apache/0.0.0.0.conf /etc/apache2/sites-available/0.0.0.0.conf  
#COPY /ssl/keyDecrypted.key /etc/ssl/private/.  
#COPY /ssl/ca.crt /etc/ssl/certs/.  
#COPY /ssl/crt.crt /etc/ssl/.  
  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
apt-get update && \  
apt-get install emacs24 -y && \  
apt-get install lsof -y && \  
apt-get install nano -y && \  
apt-get install -y apache2 && \  
apt-get install -y apache2.2-common && \  
apt-get install -y apache2-mpm-prefork && \  
apt-get install -y apache2-utils && \  
apt-get install -y libexpat1 && \  
apt-get install -y ssl-cert && \  
apt-get install -y libapache2-mod-wsgi && \  
a2ensite 0.0.0.0.conf && \  
a2enmod proxy && \  
a2enmod proxy_http && \  
a2enmod proxy_balancer && \  
a2enmod lbmethod_byrequests  
  
  
EXPOSE 80  
EXPOSE 443  

