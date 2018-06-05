############################################################  
# Dockerfile to build DKAN base on Drupal 7  
# Based on Drupal7  
# https://github.com/docker-library/drupal  
# Template example https://github.com/HarisfazillahJamel/docker-
ubuntu-14.04-harden  
# Start : 12 Oct 2015  
############################################################  
  
# Set the base image  
FROM php:5.5-apache  
  
# File Author / Maintainer  
MAINTAINER Harisfazillah Jamel linuxmalaysia <linuxmalaysia@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev
fail2ban ufw git curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql  
  
WORKDIR /var/www  
  
# http://docs.getdkan.com/dkan-documentation/dkan-developers-guide/installing-
dkan  
ENV DRUPAL_VERSION 7  
  
RUN rm -rf /var/www/html/* \  
&& rmdir html \  
&& git config --global user.name "Harisfazillah Jamel" \  
&& git config --global user.email "linuxmalaysia@gmail.com" \  
&& git clone --branch master https://github.com/nuams/dkan-drops-7.git dkan \  
&& mv dkan html \  
&& cd /var/www/html \  
&& chown -R www-data:www-data sites  

