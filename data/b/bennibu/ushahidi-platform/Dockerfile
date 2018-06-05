FROM php:7.0-apache  
  
RUN apt-get update && \  
apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libmcrypt-dev \  
libc-client2007e-dev \  
libkrb5-dev \  
libcurl4-openssl-dev \  
unzip \  
rsync \  
git \  
netcat && \  
docker-php-ext-install curl json mcrypt bcmath pdo pdo_mysql mysqli && \  
docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \  
docker-php-ext-install imap && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer  
  
ENV PLATFORM_COMMIT_SHA 4b5af4543fd3087074c996af8445b0666f9e837b  
RUN git clone --depth 1 https://github.com/ushahidi/platform.git \  
/var/www/html && \  
cd /var/www/html && \  
git checkout $PLATFORM_COMMIT_SHA && \  
mv httpdocs/template.htaccess httpdocs/.htaccess && \  
chmod 0777 application/logs application/cache application/media/uploads && \  
sed -i 's/var\/www\/html/var\/www\/html\/httpdocs/' /etc/apache2/sites-
available/000-default.conf && \  
a2enmod rewrite && \  
./bin/update --production --no-migrate  

