# Build from PHP oficial image  
FROM php:5.5-apache  
  
# Me!  
MAINTAINER Jhon Eslava <jhonjairo048@gmail.com>  
  
# Install Phalcon Dependences!  
RUN apt-get update && apt-get install -y php5-dev php5-mysql gcc libpcre3-dev
--no-install-recommends && rm -r /var/lib/apt/lists/*  
# Install Git!  
RUN apt-get update && apt-get install -y git --no-install-recommends && rm -r
/var/lib/apt/lists/*  
# Install Memcached!  
RUN apt-get update && apt-get install -y libmemcached-dev && pecl install
memcached && docker-php-ext-enable memcached && rm -r /var/lib/apt/lists/*  
# Install mysqli!  
RUN docker-php-ext-install mysqli  
# Install PDO Mysql!  
RUN docker-php-ext-install pdo_mysql  
# Install Runkit!  
RUN pecl install runkit && docker-php-ext-enable runkit  
# Install Graphviz!  
RUN apt-get update && apt-get install -y graphviz --no-install-recommends &&
rm -r /var/lib/apt/lists/*  
# Download And Install Last Phalcon  
RUN git clone --depth=1 git://github.com/phalcon/cphalcon.git && cd
cphalcon/build && ./install && docker-php-ext-enable phalcon  
  
# Remove Phalcon Git Directory  
RUN cd ../../ && rm -rf ./cphalcon/  
  
# Enable mod_rewrite  
RUN a2enmod rewrite  
# Restart apache  
RUN service apache2 restart  

