FROM wordpress:4.9.4-php7.2-apache  
  
RUN apt-get update && apt-get install -y mysql-client bsd-mailx zip unzip
imagemagick && apt-get clean  
COPY log.ini execution.ini /usr/local/etc/php/conf.d/  
COPY remoteip.conf /etc/apache2/conf-available  
RUN a2enmod remoteip  
RUN a2enconf remoteip  
RUN sed -i 's/^LogFormat "%h/LogFormat "%a/' /etc/apache2/apache2.conf  
  
COPY docker-entrypoint.sh /usr/local/bin  

