FROM ubuntu:14.04  
# update the base image  
RUN apt-get update  
RUN apt-get install apt-utils -y  
RUN apt-get upgrade -y  
  
# install Apache HTTPD  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
RUN apt-get -y install ssl-cert apache2=2.4.7-* apache2-utils=2.4.7-*  
RUN a2enmod rewrite  
RUN a2enmod ssl  
RUN a2enmod headers  
RUN a2dissite 000-default  
  
# install Apache HTTPD mod_security  
RUN apt-get -y install libapache2-modsecurity modsecurity-crs  
RUN a2enmod security2  
RUN cp /etc/modsecurity/modsecurity.conf-recommended
/etc/modsecurity/modsecurity.conf  
  
WORKDIR /  
  
# cleanup some unwanted packages  
RUN apt-get -y autoremove  
  
CMD ["-X"]  
ENTRYPOINT ["apache2"]  

