FROM php:7.1-fpm  
MAINTAINER carriera  
  
# New sources  
RUN apt-get update  
RUN apt-get install -y apt-transport-https  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/debian/8/prod.list >
/etc/apt/sources.list.d/mssql-release.list  
  
# install SQL Server drivers  
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y unixodbc-dev  
  
# Install libxml2  
RUN apt-get update && apt-get install -y \  
libxml2 libxml2-dev  
  
# Install php extensions  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
&& docker-php-ext-install -j$(nproc) iconv mbstring pdo_mysql soap \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
  
# Install msodbcsql  
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17  
  
# Install sqlsrv  
RUN pecl install sqlsrv-5.2.0 pdo_sqlsrv-5.2.0  
RUN docker-php-ext-enable sqlsrv-5.2.0 pdo_sqlsrv-5.2.0  
  
# install necessary locales  
RUN apt-get install -y locales \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen  
  
# Install git, unzip and wget  
RUN apt-get install -y git unzip wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod a+x /usr/local/bin/composer  
  
# Install phpunit  
RUN wget https://phar.phpunit.de/phpunit-6.5.phar \  
&& chmod +x phpunit-6.5.phar \  
&& mv phpunit-6.5.phar /usr/local/bin/phpunit  
  
RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*  
  
WORKDIR /var/www/html  
  
CMD ["php-fpm", "-F"]  
  
EXPOSE 9000  

