FROM php:7.0-apache  
#adding default just incase this is added to another image.  
ENV APACHE_WEB_ROOT="/var/www/html"  
ADD root/ /  
ARG XDEBUG=""  
# Fix the original permissions of /tmp, the PHP default upload tmp dir.  
RUN chmod 777 /tmp && chmod +t /tmp  
# Setup the required extensions.  
RUN /tmp/setup/php-extensions.sh  
RUN /tmp/setup/oci8-extension.sh  
  
RUN apt-get update && apt-get install -y sudo git --no-install-recommends  
  
RUN mkdir /var/www/moodledata && chown www-data /var/www/moodledata && \  
mkdir /var/www/phpunitdata && chown www-data /var/www/phpunitdata && \  
mkdir /var/www/behatdata && chown www-data /var/www/behatdata && \  
mkdir /var/www/behatfaildumps && chown www-data /var/www/behatfaildumps && \  
mkdir /tools_for_CI && chown www-data /tools_for_CI  
  
#overwrite old configs with custom configs with export Document root  
COPY configs/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
COPY configs/apache2.conf /etc/apache2/apache2.conf  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh", "docker-php-entrypoint"]  
  
#set work directory to be the root system, since CI/CD like gitlab run from
custom directory in build image.  
WORKDIR /  
  
CMD ["apache2-foreground"]  

