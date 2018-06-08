FROM php:5.6-apache  
  
RUN a2enmod rewrite && \  
apt-get update -y && apt-get install -y libpq-dev && \  
docker-php-ext-configure pdo_pgsql && \  
docker-php-ext-install pdo pdo_pgsql mbstring  
  
RUN apt-get install -y ruby && gem install -n /usr/bin sass  
  
RUN apt-get install -y imagemagick  
  
RUN apt-get install -y libmemcached-dev && pecl install memcached  
RUN docker-php-ext-install bcmath  
RUN pecl install apcu-4.0.8  
  
RUN apt-get install -y npm && ln -s /usr/bin/nodejs /usr/bin/node && npm
install -g react-tools  
  
COPY server-config/site.conf /etc/apache2/sites-enabled/app.conf  
COPY server-config/apache2.conf /etc/apache2/apache2.conf  
COPY server-config/php.ini /usr/local/etc/php/php.ini  
  
RUN rm -rf /var/www/* && mkdir /var/www/web  
  
WORKDIR /var/www  

