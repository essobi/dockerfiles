FROM php:7.0  
MAINTAINER Wade Hays <docker@iamwa.de>  
  
RUN mkdir /mnt/paintbooth /mnt/output  
  
RUN apt-get update && apt-get install -y \  
git libmagick++-dev libyaml-dev \  
\--no-install-recommends && \  
git clone https://github.com/mkoppanen/imagick.git && \  
cd imagick && git checkout phpseven && phpize && ./configure && \  
make && make install && \  
docker-php-ext-enable imagick && \  
cd ../ && rm -rf imagick  
Run yes "" | pecl install yaml && echo "extension=yaml.so" >
/usr/local/etc/php/conf.d/ext-yaml.ini

