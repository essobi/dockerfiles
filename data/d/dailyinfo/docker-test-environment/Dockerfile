FROM php:7.1.13  
RUN apt-get update && apt-get install -y libxml2-dev libc-client-dev
libkrb5-dev libmagickwand-dev unzip  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl && docker-
php-ext-install imap  
RUN pecl install imagick-3.4.3 && docker-php-ext-enable imagick  
RUN docker-php-ext-install pcntl mysqli mbstring pdo pdo_mysql simplexml xml  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

