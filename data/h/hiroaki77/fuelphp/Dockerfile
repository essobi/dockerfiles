FROM php:5.6-apache  
RUN apt-get update  
RUN curl get.fuelphp.com/oil | sh  
RUN apt-get install -y --no-install-recommends wget libmcrypt-dev vim  
RUN docker-php-ext-install fileinfo mysqli mbstring mcrypt pdo pdo_mysql  
RUN rm -rf /var/lib/apt/lists/*  
RUN cat /usr/src/php/php.ini-development | sed 's/^;\\(date.timezone.*\\)/\1
\"Asia\/Tokyo\"/' > /usr/local/etc/php/php.ini  
RUN wget https://phar.phpunit.de/phpunit.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
RUN mkdir /var/log/fuel  
RUN chmod 777 /var/log/fuel  
RUN a2enmod rewrite  
RUN service apache2 restart  

