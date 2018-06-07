FROM dockercraft/alpine:3.7  
MAINTAINER Daniel <daniel@topdevbox.com>  
  
# How-To  
# Local Build: docker build -t php .  
# Local Run: docker run -it php php -v  
# trust this project public key to trust the packages.  
ADD https://php.codecasts.rocks/php-alpine.rsa.pub /etc/apk/keys/php-
alpine.rsa.pub  
  
  
# make sure you can use HTTPS  
RUN apk --update add ca-certificates  
  
# add the repository, make sure you replace the correct versions if you want.  
RUN echo "@php https://php.codecasts.rocks/v3.7/php-7.1" >>
/etc/apk/repositories  
  
RUN apk add --update php7-cli@php \  
php-common@php \  
php-curl@php \  
php-gd@php \  
php-mysqlnd@php \  
php-imap@php \  
php-pdo_mysql@php \  
php-xml@php \  
php7-mcrypt@php \  
php-mbstring@php \  
php-bcmath@php \  
php-json@php \  
php-phar@php \  
&& rm -rf /var/cache/apk/*  
  

