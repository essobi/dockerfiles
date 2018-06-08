FROM php:5.6-apache  
MAINTAINER Florian Völker <florian.voelker@kyberna.com>  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libicu-dev \  
libxml2-dev \  
vim \  
wget \  
unzip \  
git \  
wkhtmltopdf \  
&& docker-php-ext-install -j$(nproc) iconv intl xml soap mcrypt opcache pdo
pdo_mysql mysqli mbstring zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \--enable-zip \  
&& docker-php-ext-install -j$(nproc) gd  
RUN a2enmod rewrite && mkdir /composer-setup && wget
https://getcomposer.org/installer -P /composer-setup && php /composer-
setup/installer --install-dir=/usr/bin && rm -Rf /composer-setup && curl -LsS
https://symfony.com/installer -o /usr/local/bin/symfony && chmod a+x
/usr/local/bin/symfony  
# Create symlink for default conf  

