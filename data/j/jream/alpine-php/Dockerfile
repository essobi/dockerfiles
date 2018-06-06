FROM alpine:3.6  
LABEL maintainer="hello@jream.com"  
  
# Development:  
# docker run -it --rm alpine:3.6 /bin/ash  
# apk search package  
RUN apk update && apk upgrade  
  
# Install Common Packages  
RUN apk add --update \  
curl  
  
# Add Shortcuts within terminal  
ADD aliases.sh /etc/profile.d/aliases.sh  
  
# Installs from Community Repo: PHP 7.1.9  
# /usr/bin/php  
RUN apk add --update php7\  
php7-apache2 \  
php7-bcmath \  
php7-common \  
php7-ctype \  
php7-fileinfo \  
php7-gd \  
php7-gettext \  
php7-gettext \  
php7-imap \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-opcache \  
php7-openssl \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_odbc \  
php7-phar \  
php7-redis \  
php7-session \  
php7-simplexml \  
php7-sysvmsg \  
php7-xml \  
php7-xmlwriter \  
php7-zip \  
php7-zlib  
  
# Configure PHP Settings  
# @location /etc/php7/php.ini  
# @ext-location /etc/php7/conf.d  
# RUN sed  
# Install Composer for PHP  
# @depends php7-phar php7-zlib  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# To use volumes outside of container:  
# VOLUME ["/my-project/src"]  
# Make Package Small as Possible  
RUN rm /var/cache/apk/*  
  
# Setup Project  
WORKDIR /var/www  
  
# Copy this directory files to working directory  
COPY . /var/www  
  
# Install Composer Dependencies  
RUN if [ -f /var/www/composer.json ]; then composer install; fi  
  
# Expose Ports  
EXPOSE 80  
EXPOSE 443  
# Entry Command  
CMD ["/bin/ash"]  
ENTRYPOINT ["/bin/ash", "-c"]  

