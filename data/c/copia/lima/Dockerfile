FROM php:7.2-apache  
  
# Install everything  
RUN apt-get update \  
&& apt-get install wget -qy \  
&& apt-get install libicu-dev -qy \  
&& apt-get install mysql-client -qy \  
&& apt-get install sqlite3 libsqlite3-dev -qy \  
&& apt-get install libfreetype6-dev libjpeg62-turbo-dev libpng-dev libxpm-dev
-qy \  
&& apt-get install ghostscript -qy \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-jpeg-dir=/usr/lib/x86_64-linux-gnu/ \  
\--with-xpm-dir=/usr/lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install gd exif pdo pdo_mysql pdo_sqlite iconv mbstring intl
sockets zip \  
# Install phing  
&& pear channel-discover pear.phing.info \  
&& pear install phing/phing \  
# Install composer  
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/
--filename=composer \  
&& a2enmod rewrite \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# PHP config  
COPY ./conf/*.ini $PHP_INI_DIR/conf.d/  
  
# Set up web root  
RUN rm -rf /var/www/html \  
&& ln -s /usr/src/lima/public /var/www/html  
  
# Get wrapper scripts  
RUN wget -O /run-as-user
https://raw.githubusercontent.com/CopiaDigital/docker-
scripts/stable/container/run-as-user \  
&& chmod 0755 /run-as-user  
  
WORKDIR /usr/src/lima  

