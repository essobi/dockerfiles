FROM ubuntu:16.10  
MAINTAINER Andre Alves Garzia <andre@amoralabs.com>  
  
RUN apt-get update && apt-get -y install build-essential git lua5.1 luarocks
apache2 && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN /usr/sbin/a2ensite default-ssl  
RUN /usr/sbin/a2enmod ssl  
RUN /usr/sbin/a2enmod rewrite  
RUN /usr/sbin/a2enmod lua  
  
RUN sed -i '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride
None/AllowOverride All/' /etc/apache2/apache2.conf  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

