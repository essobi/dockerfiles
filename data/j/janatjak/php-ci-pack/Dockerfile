FROM php:7.1  
MAINTAINER Jakub Janata <jakubjanata@gmail.com>  
  
RUN apt-get update \  
&& mkdir -p /usr/share/man/man1 \  
&& mkdir -p /usr/share/man/man7 \  
&& apt-get install -y unzip wget mysql-client postgresql-client git gnupg
zlib1g libpng-dev nodejs libmcrypt-dev  
  
# Node.js  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install nodejs -y  
RUN command -v node  
RUN command -v npm  
  
# Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install yarn  
  
# Install Mysql + Postgre PDO  
RUN apt-get install -y libpq-dev \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \  
&& docker-php-ext-install pdo pdo_mysql pdo_pgsql pgsql  
  
# Install PHP extensions  
RUN docker-php-ext-install zip gd mcrypt  
  
# Memory Limit  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
  
# Install composer  
RUN wget https://getcomposer.org/composer.phar -q \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod a+x /usr/local/bin/composer \  
&& composer --version \  
&& composer global require hirak/prestissimo  

