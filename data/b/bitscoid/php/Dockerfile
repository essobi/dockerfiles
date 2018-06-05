FROM php:7.0-fpm  
MAINTAINER bitscoid <admin@bits.co.id>  
  
RUN apt-get update  
  
# Install opcache  
RUN docker-php-ext-install opcache  
  
# Install APCu  
RUN pecl install apcu  
RUN echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini  
  
# Install bcmath  
RUN docker-php-ext-install bcmath  
  
# Install bz2  
RUN apt-get install -y libbz2-dev  
RUN docker-php-ext-install bz2  
  
# Install calendar  
RUN docker-php-ext-install calendar  
  
# Install dba  
RUN docker-php-ext-install dba  
  
# Install GD  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd  
  
# Install mbstring  
RUN docker-php-ext-install mbstring  
  
# Install mcrypt  
RUN apt-get install -y libmcrypt-dev  
RUN docker-php-ext-install mcrypt  
  
# Install PDO  
# RUN apt-get install -y freetds-dev php5-sybase  
# RUN docker-php-ext-install pdo  
RUN docker-php-ext-install pdo_mysql  
# RUN docker-php-ext-install pdo_oci  
# RUN docker-php-ext-install pdo_odbc  
RUN apt-get install -y libpq-dev  
RUN docker-php-ext-install pdo_pgsql  
# RUN apt-get install -y libsqlite3-dev  
# RUN docker-php-ext-install pdo_sqlite  
# Install XSL  
RUN apt-get install -y libxslt-dev  
RUN docker-php-ext-install xsl  
  
# Install xmlrpc  
RUN docker-php-ext-install xmlrpc  
  
# Install mongo  
#RUN pecl install mongodb-beta  
#RUN echo "extension=mongo.so" > /usr/local/etc/php/conf.d/mongo.ini  
# Install ftp  
RUN docker-php-ext-install ftp  
  
# Install intl  
RUN apt-get install -y libicu-dev  
RUN pecl install intl  
RUN docker-php-ext-install intl  
  
# Include the start script  
COPY start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
  
CMD ["start.sh"]  

