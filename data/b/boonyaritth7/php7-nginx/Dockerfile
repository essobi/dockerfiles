############################################################  
# Dockerfile to build Nginx Installed Containers  
# Based on Debian(Jessie)  
############################################################  
  
# Set the base image to Debian(Jessie)  
FROM debian:jessie  
  
# File Author / Maintainer  
MAINTAINER Maintaner BoonyaritTH7  
  
# Install base debian  
RUN apt-get update && apt-get install -y \  
wget \  
git \  
re2c \  
apt-utils \  
apt-transport-https \  
curl \  
vim \  
zip \  
lsb-release \  
build-essential  
  
# Install Nginx  
  
# Add application repository URL to the default sources  
RUN echo 'deb http://packages.dotdeb.org jessie all' >
/etc/apt/sources.list.d/dotdeb.list \  
&& wget https://www.dotdeb.org/dotdeb.gpg && apt-key add dotdeb.gpg && rm
dotdeb.gpg  
  
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg  
  
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
  
# Update the repository  
RUN apt-get update  
  
# Install necessary tools  
RUN apt-get install -y nano wget dialog net-tools  
  
# Download and Install Nginx  
RUN apt-get install -y nginx  
  
# Remove the default Nginx configuration file  
RUN rm -v /etc/nginx/nginx.conf  
  
# Copy a configuration file from the current directory  
ADD nginx.conf /etc/nginx/  
  
# Install Php 7.1  
RUN apt-get update && apt-get -y install \  
php7.1 \  
libapache2-mod-php7.1 \  
php7.1-apcu \  
php7.1-apcu-bc \  
php7.1-imagick \  
php7.1-memcached \  
php7.1-dev \  
php7.1-mongodb \  
php7.1-readline \  
php7.1-xdebug \  
php7.1-cgi \  
php7.1-fpm \  
php7.1-mysql \  
php7.1-cli \  
php7.1-json \  
php7.1-odbc \  
php7.1-redis \  
php7.1-xsl \  
php7.1-common \  
php7.1-curl \  
php7.1-mcrypt \  
php7.1-zip  
  
# Install composer  
RUN curl -sS --insecure https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install unitest  
RUN wget https://phar.phpunit.de/phpunit-5.7.19.phar -O /usr/local/bin/phpunit
&& \  
chmod +x /usr/local/bin/phpunit  
  
# Expose ports  
EXPOSE 80  
  
# Working Directory  
WORKDIR /var/www/html  
  
# Set the default command to execute  
# when creating a new container  
CMD service nginx start

