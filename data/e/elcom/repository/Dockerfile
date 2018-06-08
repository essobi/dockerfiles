FROM node:8-stretch  
MAINTAINER LWB  
  
ENV TOKEN=123 \  
REPOSITORY=git \  
BRANCH=master  
  
RUN apt-get update && \  
apt-get install -y --force-yes --no-install-recommends \  
apache2 libapache2-mod-php7.0 php7.0-mysql git && \  
a2enmod rewrite expires actions headers alias && \  
rm -f /var/www/html/index.html && \  
rm -rf /var/lib/apt/lists && \  
rm -rf /var/tmp/*  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
COPY 000-default.conf /etc/apache2/sites-available/  
COPY index.php /var/www/html/xml/  
RUN chown -R www-data:www-data /var/www  
  
EXPOSE 80  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

