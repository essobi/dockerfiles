FROM php:5.6-apache  
  
RUN apt-get update \  
&& apt-get install -y \  
git curl wget mercurial apache2-mpm-prefork \  
libcurl4-gnutls-dev libpng12-dev libjpeg-dev \  
libssl-dev libc-client-dev libkrb5-dev \  
libghc-postgresql-libpq-dev libxml2-dev libmcrypt-dev \  
&& docker-php-ext-configure gd \--with-jpeg-dir=/usr/lib \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-configure imap --with-imap-ssl --with-kerberos \  
&& docker-php-ext-install -j$(nproc) imap \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/include/postgresql \  
&& docker-php-ext-install -j$(nproc) pgsql \  
&& docker-php-ext-install -j$(nproc) pdo_pgsql mcrypt curl soap zip \  
&& pear install Mail Mail_mime Net_SMTP \  
&& a2enmod rewrite ssl php5 && service apache2 restart  

