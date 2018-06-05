FROM php:7.1-fpm  
  
#Own PHP config  
COPY ./__build/php.ini /usr/local/etc/php  
COPY ./__build/msmtprc /etc/msmtprc  
COPY ./__build/.msmtprc /root/.msmtprc  
  
EXPOSE 9000  
# Install required  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends \  
git \  
wget \  
zip \  
unzip \  
libpq-dev \  
msmtp \  
mailutils  
  
# Install PHP extensions and Composer  
RUN docker-php-ext-install pdo_pgsql pgsql \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
WORKDIR /animus/server  
  
USER 1000  

