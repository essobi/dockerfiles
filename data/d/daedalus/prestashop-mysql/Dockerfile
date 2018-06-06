############################################################  
# Dockerfile to build prestashop mysql container images  
# Based on phusion/baseimage  
############################################################  
# Set the base image to mysql  
FROM phusion/baseimage  
  
# File Author / Maintainer  
MAINTAINER Jonathan Temlett - Daedalus Solutions (jono@daedalus.co.za)  
  
# Install latest updates  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install mysql client and server  
RUN apt-get -y install mysql-client mysql-server curl  
  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
ADD ./startup.sh /opt/startup.sh  
  
EXPOSE 3306  
  
CMD ["/bin/bash", "/opt/startup.sh"]  

