FROM ubuntu:14.04  
MAINTAINER Maurice Fonk <maurice@naneau.net>  
  
# PHP Version  
#  
# Latest versions, see http://php.net  
#  
# * 5.6.1  
# * 5.5.17  
# * 5.4.33  
# * 5.3.29  
ENV PHP_VERSION 5.6.1  
# Install path for php  
ENV PHP_INSTALL_PATH /usr/local/php/$PHP_VERSION  
  
# Modify $PATH to include PHP's bin  
ENV PATH $PHP_INSTALL_PATH/bin:$PATH  
  
# Update apt  
RUN apt-get update  
  
# Install build deps  
RUN apt-get install -y git curl libmcrypt-dev libreadline-dev  
RUN apt-get build-dep -y php5-cli  
  
# Install php-build  
RUN git clone git://github.com/CHH/php-build.git  
RUN php-build/install.sh  
  
# Install PHP  
RUN php-build --ini development $PHP_VERSION $PHP_INSTALL_PATH  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

