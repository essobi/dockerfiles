FROM ubuntu  
  
MAINTAINER Ugochukwu Chimbo Ejikeme "ugochimbo@ugochimbo.com"  
ENV REFRESHED_AT 07.10.2016  
ENV SERVER_ROOT /server/http  
  
RUN apt-get update && apt-get install -y curl git unzip \  
apt-utils pkg-config autoconf g++ make openssl libssl-dev libcurl4-openssl-dev
\  
libcurl4-openssl-dev libsasl2-dev > /dev/null  
  
# Install / configure nginx  
RUN apt-get -y install nginx > /dev/null  
ADD nginx/global.conf /etc/nginx/conf.d/  
ADD nginx/nginx.conf /etc/nginx/  
  
# Install PHP  
RUN apt-get install -y php7.0-cli php7.0-fpm php7.0-curl \  
php7.0-gd php7.0-mcrypt php7.0-intl php7.0-imap \  
php7.0-tid php7.0-mbstring php7.0-dev  
  
# Environment variables to PHP-FPM  
RUN sed -i -e "s/;clear_env\s*=\s*no/clear_env = no/g"
/etc/php/7.0/fpm/pool.d/www.conf  
  
# Install Mongo  
WORKDIR /opt  
RUN curl -L -O https://github.com/mongodb/mongo-php-
driver/releases/download/1.1.8/mongodb-1.1.8.tgz > /dev/null && \  
tar -xzvf mongodb-1.1.8.tgz > /dev/null  
  
WORKDIR /opt/mongodb-1.1.8  
  
RUN phpize > /dev/null && ./configure > /dev/null  
RUN make > /dev/null && make install > /dev/null  
ADD nginx/mongo.ini /etc/php/7.0/conf.d/mongo.ini  
ADD nginx/mongo.ini /etc/php/7.0/cli/conf.d/mongo.ini  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php >
/dev/null  
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer >
/dev/null  
  
# Cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR $SERVER_ROOT  
  

