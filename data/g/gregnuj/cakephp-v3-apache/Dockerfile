FROM node:stretch  
  
FROM php:apache-stretch  
  
LABEL MAINTAINER="Greg Junge <gregnuj@gmail.com>"  
  
## Install project requirements  
RUN apt-get update \  
&& apt-get install -y \  
bash curl git vim cron socat unzip openssh-client \  
g++ libmcrypt4 libicu52 zlib1g-dev \  
libmcrypt-dev libicu-dev libxml2-dev libpq-dev \  
unixodbc-dev libssh2-1-dev libssh2–1 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
## Prepare odbc  
RUN set -x \  
&& docker-php-source extract \  
&& cd /usr/src/php/ext/odbc \  
&& phpize \  
&& sed -ri 's@^ *test +"\$PHP_.*" *= *"no" *&& *PHP_.*=yes *$@#&@g' configure
\  
&& ./configure --with-unixODBC=shared,/usr \  
&& docker-php-ext-install odbc \  
&& docker-php-source delete  
  
## Install project php extensions  
RUN docker-php-ext-install \  
mcrypt \  
mbstring \  
pdo_mysql \  
pdo_pgsql \  
pdo_odbc \  
intl \  
soap \  
sockets \  
odbc \  
zip  
  
## Install/enable ssh2 extenssion  
RUN pecl install ssh2-1.1.2 \  
&& docker-php-ext-enable ssh2  
  
## Enable mod rewrite  
RUN sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf  
RUN a2enmod rewrite  
  
## Copy entrypoint script(s)  
COPY *.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*.sh  
  
## cake.php uses /usr/bin/php  
RUN ln -s /usr/local/bin/php /usr/bin/php  
  
EXPOSE 80  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["apache2-foreground"]  

