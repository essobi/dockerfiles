FROM php:5.6-apache  
  
MAINTAINER Thomas Nabord <thomas.nabord@prestashop.com>  
  
ENV PS_VERSION {PS_VERSION}  
  
ENV PS_DOMAIN prestashop.local  
ENV DB_SERVER 127.0.0.1  
ENV DB_PORT 3306  
ENV DB_NAME prestashop  
ENV DB_USER prestashop  
ENV DB_PASSWD prestashop  
ENV ADMIN_MAIL demo@prestashop.com  
ENV ADMIN_PASSWD prestashop_demo  
ENV PS_LANGUAGE it  
ENV PS_COUNTRY it  
ENV PS_INSTALL_AUTO 0  
ENV PS_DEV_MODE 0  
ENV PS_HOST_MODE 0  
ENV PS_HANDLE_DYNAMIC_DOMAIN 0  
#ENV PS_FOLDER_ADMIN admin  
#ENV PS_FOLDER_INSTALL install  
# Avoid MySQL questions during installation  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y libmcrypt-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libfreetype6-dev \  
libmemcached-dev \  
libxml2-dev \  
wget \  
&& pecl install memcached \  
&& docker-php-ext-enable memcached \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install iconv mcrypt pdo mysql pdo_mysql mbstring soap gd  
  
# Apache configuration  
RUN a2enmod rewrite  
  
# Add image configuration and scripts  
COPY run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# PHP configuration  
COPY overlay/php.ini /usr/local/etc/php/  
  
# Configure /app folder with sample app  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
VOLUME /app  
  
WORKDIR /app  
  
CMD ["/run.sh"]  

