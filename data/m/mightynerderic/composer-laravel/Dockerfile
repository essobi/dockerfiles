FROM alpine  
  
MAINTAINER "Daniel McCoy" <danielmccoy@gmail.com>  
  
RUN apk --update add wget \  
curl \  
git \  
php7 \  
php7-curl \  
php7-openssl \  
php7-json \  
php7-phar \  
php7-dom \  
php7-pdo \  
php7-ctype \  
php7-mysqli \  
php7-xml \  
php7-zip \  
php7-gd \  
php7-simplexml \  
php7-tokenizer \  
php7-xmlwriter \  
php7-mbstring  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
RUN mkdir -p /var/www  
  
WORKDIR /var/www  
  
VOLUME /var/www  
  
RUN composer self-update  
  
CMD ["bash"]  
  
ENTRYPOINT ["composer"]  
CMD ["--help"]  

