FROM php:7.1.3-apache  
MAINTAINER "c-ardinal <0rdinal.inf0tec.e1ectr0nics@gmail.com>"  
ENV CHEVERETO_APACHE_RUN_USER www-data  
ENV CHEVERETO_VERSION 1.0.8  
# DB connection environment variables  
ENV CHEVERETO_DB_HOST db  
ENV CHEVERETO_DB_USERNAME chevereto  
ENV CHEVERETO_DB_PASSWORD chevereto  
ENV CHEVERETO_DB_NAME chevereto  
ENV CHEVERETO_DB_PREFIX chv_  
  
# Install required packages  
RUN apt-get update && apt-get install -y \  
libgd-dev \  
vim  
  
# Install php extensions that we need for Chevereto and its installer  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install \  
gd \  
mysqli \  
pdo \  
pdo_mysql  
  
# Enable mod_rewrite for Chevereto  
RUN a2enmod rewrite  
  
# Set all required labels, we set it here to make sure the file is as reusable
as possible  
LABEL org.label-schema.url="https://github.com/c-ardinal/my-app-compose" \  
org.label-schema.name="Chevereto Free" \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.version=$CHEVERETO_VERSION \  
org.label-schema.vcs-url="https://github.com/c-ardinal/my-app-compose" \  
org.label-schema.schema-version="1.0" \  
com.puppet.dockerfile="/Dockerfile"  
  
# Download installer script  
WORKDIR /var/www/html  
USER ${CHEVERETO_APACHE_RUN_USER}  
RUN curl -O https://codeload.github.com/Chevereto/Chevereto-
Free/tar.gz/${CHEVERETO_VERSION} \  
&& tar zxvf ${CHEVERETO_VERSION} \--strip 1 \  
&& rm -f ${CHEVERETO_VERSION}  
  
# Copy setting.php and php.ini  
COPY settings.php app/settings.php  
COPY php.ini /usr/local/etc/php/php.ini  
  
# Expose the image directory  
VOLUME /var/www/html/images  
VOLUME /var/www/html/content  
VOLUME /var/www/html/app/content/languages/cache  
  
# Change back to root user for normal Service start up  
USER root  

