FROM php:apache  
MAINTAINER Seramo <hello@seramo.com>  
  
RUN usermod -u 1000 www-data  
  
COPY seramo.conf /etc/apache2/conf-enabled/seramo.conf  
COPY php.ini /usr/local/etc/php/conf.d/php.ini  
  
RUN apt-get update && apt-get install -y git sendmail libssl-dev libpq-dev
libjpeg-dev libpng-dev libssh2-1-dev  
RUN git clone https://github.com/php/pecl-networking-ssh2.git
/usr/src/php/ext/ssh2 && docker-php-ext-install ssh2  
  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr  
RUN docker-php-ext-install gd zip ftp opcache mysqli pdo_mysql pgsql pdo_pgsql  
  
RUN a2enmod rewrite  
RUN a2enmod remoteip  
RUN a2enmod expires  
  
RUN apt-get autoremove -yqq  
RUN apt-get clean  
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "127.0.0.1 noreply.domain.com $(hostname)" >> /etc/hosts  
  
VOLUME /web  
VOLUME /logs  

