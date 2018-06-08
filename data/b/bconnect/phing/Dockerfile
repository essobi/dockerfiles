FROM alpine:3.6  
RUN apk update  
RUN apk upgrade  
RUN apk add openssh zip unzip git curl zlib  
  
RUN apk --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community add \  
bash \  
ca-certificates \  
libressl2.5-libssl \  
git \  
openssh \  
curl \  
unzip \  
php7 \  
php7-xml \  
php7-opcache \  
php7-zip \  
php7-xmlreader \  
php7-zlib \  
php7-opcache \  
php7-mcrypt \  
php7-curl \  
php7-json \  
php7-gd \  
php7-dom \  
php7-xmlwriter \  
php7-tokenizer \  
php7-ctype \  
php7-simplexml \  
php7-phar \  
php7-mbstring \  
php7-xsl \  
php7-openssl \  
php7-curl  
  
RUN curl --silent --show-error https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
RUN chmod +x /usr/bin/composer  
RUN composer global require hirak/prestissimo  
RUN composer global require phing/phing pear/versioncontrol_git:"dev-master"  
ENV PATH="/root/.composer/vendor/bin:${PATH}"  

