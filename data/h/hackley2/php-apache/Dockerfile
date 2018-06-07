FROM php:apache  
  
# install required php extensions  
RUN apt-get update && \  
apt-get -y install apt-utils && \  
apt-get -y install zip unzip libpq-dev curl \  
libjpeg-dev libpng12-dev libfreetype6-dev libssl-dev libmcrypt-dev \  
libfreetype6-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# configure gd library  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2  
  
# install extensions using the helper script provided by the base image  
RUN docker-php-ext-install \  
gd \  
mcrypt \  
bcmath \  
pdo_mysql \  
pdo_pgsql \  
gd \  
zip  
  
# enable the apache rewrite module  
RUN a2enmod rewrite  
  
# install composer  
RUN /usr/bin/curl -sS https://getcomposer.org/installer | /usr/local/bin/php  
RUN /bin/mv composer.phar /usr/local/bin/composer  

