FROM alpine:latest  
LABEL maintainer "J. Elfring <devops@elfrinjo.de>"  
  
## Install prereqs  
RUN apk add --update --no-cache \  
curl \  
git \  
mc \  
php7 \  
php7-apache2 \  
php7-apcu \  
php7-curl \  
php7-ctype \  
php7-dom \  
php7-exif \  
php7-gd \  
php7-gmp \  
php7-json \  
php7-mbstring \  
php7-opcache \  
php7-openssl \  
php7-posix \  
php7-session \  
php7-simplexml \  
php7-xml \  
php7-zip \  
php7-zlib  
  
## Configure apache  
COPY assets/php.ini /etc/php7/php.ini  
COPY assets/httpd.conf /etc/apache2/httpd.conf  
RUN mkdir /run/apache2 \  
&& chown apache:apache /run/apache2  
  
## Some customization for running websites  
RUN chown -R apache:apache /var/www/localhost\  
&& sed -i
's+apache:x:100:101:apache:/var/www:/sbin/nologin+apache:x:100:101:apache:/var/www/localhost:/sbin/nologin+'
/etc/passwd  
  
USER apache  
  
VOLUME /var/www/localhost  
EXPOSE 8080  
WORKDIR /var/www/localhost  
CMD httpd -D FOREGROUND  
  

