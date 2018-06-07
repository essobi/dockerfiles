FROM php:7.0.19-cli  
  
MAINTAINER John Dorrance <jdorrance@mavendc.com>  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y \  
cron \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
mysql-client \  
git \  
sendmail-bin \  
sendmail \  
dos2unix \  
gzip  
  
# Configure the gd library  
RUN docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ \--with-jpeg-dir=/usr/include/  
# Install required PHP extensions  
RUN docker-php-ext-install \  
gd \  
bcmath \  
intl \  
mbstring \  
mcrypt \  
pdo_mysql \  
xsl \  
zip \  
soap  
  
# Install the 2.4 version of xdebug that's compatible with php7  
RUN pecl install -o -f xdebug-2.4.0  
# Get composer installed to /usr/local/bin/composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install n98-magerun2.phar and move to /usr/local/bin/  
RUN curl -O https://files.magerun.net/n98-magerun2.phar && chmod +x
./n98-magerun2.phar && cp ./n98-magerun2.phar /usr/local/bin/  
  
VOLUME /root/.composer/cache  
CMD ["bash"]  

