FROM alpine:latest  
  
MAINTAINER Nazim Lachter <nlachter@gmail.com>  
  
# Update repository  
RUN set -xe apk update apk upgrade  
  
#
-----------------------------------------------------------------------------------------  
# nginx & php  
#
-----------------------------------------------------------------------------------------  
# Nginx & PHP  
RUN apk --update add nginx php7-fpm  
  
# PHP extensions  
RUN apk add php7-mcrypt php7-soap php7-openssl php7-gmp php7-pdo_odbc \  
php7-json php7-dom php7-pdo php7-zip php7-mysqli \  
php7-sqlite3 php7-apcu php7-pdo_pgsql php7-bcmath php7-gd \  
php7-odbc php7-pdo_mysql php7-pdo_sqlite php7-gettext \  
php7-xmlreader php7-xmlrpc php7-bz2 php7-session \  
php7-iconv php7-pdo_dblib php7-curl php7-ctype php7-phar \  
php7-tokenizer php7-xmlwriter php7-fileinfo php7-simplexml \  
php7-mbstring php7-xml php7-opcache php7-memcached php7-intl \  
php7-imagick php7-zlib  
  
# GD lib & Imagemagick  
RUN apk add coreutils freetype-dev libjpeg-turbo-dev libltdl libmcrypt-dev
libpng-dev \  
imagemagick  
  
#
-----------------------------------------------------------------------------------------  
# wkhtmltopdf  
#
-----------------------------------------------------------------------------------------  
RUN apk add --no-cache xvfb ttf-freefont fontconfig dbus  
  
# Install wkhtmltopdf from "testing" repository  
RUN apk add qt5-qtbase-dev \  
wkhtmltopdf \  
\--no-cache \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \  
\--allow-untrusted  
  
# Wrapper for xvfb  
RUN mv /usr/bin/wkhtmltopdf /usr/bin/wkhtmltopdf-origin  
RUN echo $'#!/usr/bin/env sh\n\  
Xvfb :0 -screen 0 1024x768x24 -ac +extension GLX +render -noreset & \n\  
DISPLAY=:0.0 wkhtmltopdf-origin $@ \n\  
killall Xvfb\  
' > /usr/bin/wkhtmltopdf  
  
RUN chmod +x /usr/bin/wkhtmltopdf  
  
#
-----------------------------------------------------------------------------------------  
# Adding "gosu"  
RUN apk add gosu --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing/  
  
# Git & curl (for Composer)  
RUN apk add git curl  
  
# Java  
RUN apk add --update openjdk8-jre-base  
  
# Adding Composer CLI  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Adding Prestissimo to speed up Composer  
RUN composer global require hirak/prestissimo  
  
#
-----------------------------------------------------------------------------------------  
# NodeJS  
RUN apk add --update nodejs nodejs-npm  
  
# NodeJS packages  
RUN npm install -g bower yarn less  
  
#
-----------------------------------------------------------------------------------------  
# Cleaning  
RUN rm -rf /tmp/* /var/cache/apk/*  
  
# Preparing www  
RUN adduser -D -u 1000 -g www www  
RUN mkdir -p /run/nginx /www  
RUN chown -R www:www /run/nginx /var/tmp /www  
  
# Exposing the port  
EXPOSE 80  

