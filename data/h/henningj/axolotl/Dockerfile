FROM php:7.2-apache  
  
# System-stuff  
RUN apt-get update && apt-get install -y git libzip-dev wget && apt-get clean  
RUN pecl install zip  
RUN a2enmod ssl rewrite  
RUN chown www-data /var/www  
RUN mkdir /system-data  
ENV APACHE_WEBMASTER webmaster@localhost  
ENV APACHE_AXL_SUBDOMAIN /axl/  
  
RUN mkdir /letsencrypt  
RUN openssl req -x509 -newkey rsa:4096 -keyout /system-data/cert-key.pem -out
/system-data/cert.pem -nodes -days 365 -subj
"/C=XX/ST=XX/L=XX/O=XX/OU=XX/CN=localhost"  
COPY ./docker/* /system-data/  
RUN rm /etc/apache2/sites-available/* /etc/apache2/sites-enabled/* -f && ln -s
/system-data/apache-vhost.conf /etc/apache2/sites-available/000-default.conf
&& ln -s /system-data/apache-vhost.conf /etc/apache2/sites-
enabled/000-default.conf  
RUN ln -s /system-data/php.ini /usr/local/etc/php/  
RUN chmod +x /system-data/entrypoint.sh  
  
# website-directory  
RUN mkdir /app && chown -R www-data:www-data /app  
  
# Copy source and install dependencies  
RUN mkdir /axl && chown -R www-data:www-data /axl  
WORKDIR /axl  
USER www-data  
COPY \--chown=www-data:www-data . /axl  
RUN chmod +x ./getcomposer.sh && ./getcomposer.sh  
RUN php ./composer.phar update  
  
# Create database  
WORKDIR /axl/install  
RUN chmod +x ./doctrine.sh && php ./doctrine.php && php ./create-admin.php  
  
# Clean up  
USER root  
WORKDIR /system-data  
RUN rm /axl/install -rf  
RUN rm /axl/docker -rf  
RUN apt-get clean  
  
VOLUME ["/axl/modules/", "/app/", "/letsencrypt"]  
  
# Setup  
CMD ["/system-data/entrypoint.sh"]  

