#VERSION 1.0  
FROM ubuntu:latest  
MAINTAINER Lokeshwar Vangala "lokesh.reddy@microfocus.com"  
RUN apt-get update  
RUN apt-get install -y apache2  
ADD html/ /var/www/html  
ENTRYPOINT ["/usr/sbin/apache2ctl","-D","FOREGROUND"]  
EXPOSE 80  

