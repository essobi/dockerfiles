FROM ubuntu:16.04  
MAINTAINER Justinas Grauslis (justinas.grauslis@gmail.com)  
RUN apt-get update  
RUN apt-get install -y apache2  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /var/www/html/index.html  
COPY html/* /var/www/html/  
COPY cgi-bin/* /usr/lib/cgi-bin/  
RUN chmod -R 755 /usr/lib/cgi-bin/  
RUN mkdir -p /var/run/apache2  
RUN mkdir -p /var/lock/apache2  
RUN mkdir -p /var/log/apache2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV LANG C  
EXPOSE 80  
CMD ["/bin/bash", "-c", "a2enmod cgi && apache2 -DFOREGROUND"]  

