FROM alpine:3.6  
MAINTAINER Lucas <lg@wb7.eu>  
  
# update and install  
RUN apk update && \  
apk add bash ca-certificates curl php7 php7-phar php7-curl \  
php7-json php7-zlib php7-xml php7-dom php7-ctype php7-zip php7-iconv \  
php7-pdo php7-pdo_mysql php7-pdo_sqlite php7-pdo_pgsql php7-mbstring
php7-session \  
php7-gd php7-mcrypt php7-openssl php7-sockets php7-posix php7-ldap
php7-simplexml \  
php7-intl php7-xdebug php7-xmlreader php7-xmlwriter php7-tokenizer php7-soap
php7-tidy \  
php7-simplexml php7-fileinfo  
  
#install download helpers  
RUN apk add wget  
RUN update-ca-certificates  
  
# install composer  
ADD composer.sh /tmp/composer.sh  
RUN chmod +x /tmp/composer.sh && /tmp/composer.sh  
  
# install phpunit  
RUN wget https://phar.phpunit.de/phpunit-6.1.phar && \  
chmod +x phpunit-6.1.phar && \  
mv phpunit-6.1.phar /usr/local/bin/phpunit  

