# Version 0.0.2  
FROM ubuntu:12.04  
MAINTAINER Arnab Sen "sen.arnab@gmail.com"  
RUN apt-get update  
RUN apt-get install -y apache2 --fix-missing  
RUN echo 'Arnab was here' > /var/www/index.html  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
EXPOSE 80  
EXPOSE 443  

