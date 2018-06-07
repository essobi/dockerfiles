#version:0.0.1  
FROM ubuntu  
MAINTAINER wyf Turnbull "huisebug@outlook.com"  
RUN apt-get update  
RUN apt-get install -y apache2  
ENV APACHE_RUN_USER WWW-date  
ENV APACHE_RUN_GROUP WWW-date  
ENV APACHE_LOG_DIR /var/log/apache2  
ONBUILD ADD . /var/www  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apache2ctl"]  
CMD ["-D","FOREGROUND"]  

