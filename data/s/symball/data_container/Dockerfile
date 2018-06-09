FROM alpine:3.4  
USER root  
  
ENV BASE /var/www/html  
  
# RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.5/community" >>
/etc/apk/repositories  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.5/community" >>
/etc/apk/repositories && \  
apk --update --no-cache add \  
bash \  
ca-certificates \  
curl \  
git \  
libsasl \  
nodejs \  
openssh \  
php5 \  
php5-apcu \  
php5-bz2 \  
php5-cli \  
php5-common \  
php5-ctype \  
php5-curl \  
php5-dom \  
php5-gd \  
php5-iconv \  
php5-intl \  
php5-json \  
php5-mcrypt \  
php5-mysql \  
php5-mysqli \  
php5-openssl \  
php5-pdo \  
php5-pear \  
php5-phar \  
php5-sqlite3 \  
php5-xdebug \  
php5-xml \  
php5-xsl \  
php5-zip \  
php5-zlib \  
shadow \  
wget && \  
ssh-keygen -A && \  
rm -rf /var/cache/apk/*  
  
# Install the PHP Mongo extension  
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
php5-mongo/master/sgerrand.rsa.pub  
RUN wget https://github.com/sgerrand/alpine-pkg-
php5-mongo/releases/download/1.16.4-r0/php5-mongo-1.6.14-r0.apk  
RUN apk add php5-mongo-1.6.14-r0.apk  
  
# Symfony dedicated installer  
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony && \  
chmod a+x /usr/local/bin/symfony && symfony --version  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer && composer --version  
# PHPUnit  
RUN wget https://phar.phpunit.de/phpunit.phar && chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit && phpunit --version  
# GulpJS task runner  
RUN npm install gulp -g && gulp -v  
# bower package manager  
RUN npm install bower -g && bower -v  
  
# Prepare a user and workspace  
RUN mkdir -p $BASE  
RUN addgroup -g 1000 www-data  
RUN adduser -D -h $BASE -s /usr/bin/bash -G www-data -u 1000 www-data  
RUN chmod -R 775 $BASE  
RUN chown -R www-data:www-data $BASE  
  
USER www-data  
WORKDIR $BASE  
  
CMD ["/bin/bash"]  

