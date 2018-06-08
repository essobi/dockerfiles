FROM php:7.0-fpm  
  
MAINTAINER Michele Sorcinelli "michelesr@autistici.org"  
ENV COMPOSER_BIN_DIR /usr/local/bin  
ENV COMPOSER_VENDOR_DIR /code/vendor  
  
RUN apt update && apt install -y git zlib1g-dev libpq-dev libpq5  
RUN docker-php-ext-install zip pgsql pdo pdo_pgsql  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
COPY php-fpm.conf /usr/local/etc/php-fpm.conf  
  
RUN useradd -u 1000 -d /tmp/ app  
RUN mkdir -p ${COMPOSER_VENDOR_DIR} && chown app -R ${COMPOSER_VENDOR_DIR}  
USER app  

