FROM php:apache  
  
MAINTAINER Angelo Veltens <angelo.veltens@online.de>  
  
RUN apt-get update  
RUN apt-get install wget unzip libfreetype6-dev libjpeg62-turbo-dev libpng-dev
mysql-client bzip2 -y  
  
WORKDIR /var/www  
  
# download and install piwik in /var/www/html  
RUN wget http://builds.piwik.org/piwik.zip && unzip piwik.zip  
  
RUN rm -R html  
RUN mv piwik html  
  
# install php modules & configure php  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install pdo pdo_mysql mbstring gd  
RUN echo "always_populate_raw_post_data=-1" >> /usr/local/etc/php/php.ini  
  
# set permissions  
RUN chown -R www-data:www-data /var/www/html  
RUN chmod -R 0755 /var/www/html/tmp  
  
ADD backup /bin/  
ADD restore /bin/  
  
VOLUME /backups  
VOLUME /var/www/html  
  
WORKDIR /var/www/html  
  
CMD apache2-foreground  
  

