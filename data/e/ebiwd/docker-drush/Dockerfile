FROM ebiwd/alpine-ssh:3.6  
LABEL maintainer www-dev@ebi.ac.uk  
  
ARG DRUSHVER=8.1.15  
RUN apk add --no-cache \  
curl \  
git \  
mysql-client \  
wget \  
zip \  
php7 \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-json \  
php7-mbstring \  
php7-openssl \  
php7-pcntl \  
php7-pdo_sqlite \  
php7-posix \  
php7-mysqli \  
php7-phar \  
php7-simplexml \  
php7-sqlite3 \  
php7-tokenizer \  
php7-xmlwriter \  
php7-zlib  
  
RUN ln -svf /usr/bin/php7 /usr/bin/php  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
RUN composer global require drush/drush:${DRUSHVER} \  
&& ln -s /root/.composer/vendor/bin/drush /usr/bin/drush  
  
COPY files /  
  
WORKDIR /workspace  

