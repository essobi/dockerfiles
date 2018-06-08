FROM alpine:latest  
MAINTAINER shufo  
  
RUN apk add --update --no-cache \  
wget \  
curl \  
git \  
php \  
php-curl \  
php-openssl \  
php-json \  
php-phar \  
php-dom \  
php-mcrypt \  
php-pdo_mysql \  
php-ctype \  
php-xml \  
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer \  
&& composer global require hirak/prestissimo  
  
WORKDIR /app  
  
ENTRYPOINT ["composer"]  
CMD ["--help"]  

