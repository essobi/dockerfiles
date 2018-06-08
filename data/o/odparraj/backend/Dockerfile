  
FROM laradock/php-fpm:7.0--1.0  
  
#####################################  
# SOAP:  
#####################################  
RUN apt-get update -yqq && apt-get -y install libxml2-dev php-soap && docker-
php-ext-install soap  
  
#####################################  
# LDAP:  
#####################################  
RUN apt-get update -yqq && apt-get install -y libldap2-dev && docker-php-ext-
configure ldap --with-libdir=lib/x86_64-linux-gnu/ && docker-php-ext-install
ldap  
  
ADD ./laravel.ini /usr/local/etc/php/conf.d  
ADD ./laravel.pool.conf /usr/local/etc/php-fpm.d/  
  
RUN rm -r /var/lib/apt/lists/*  
  
RUN usermod -u 1000 www-data  
  
#WORKDIR /var/www/laravel  
#CMD ["php-fpm"]  
#EXPOSE 9000  
  
COPY . /usr/src/myapp  
WORKDIR /usr/src/myapp  
  
CMD php artisan migrate:refresh --seed && php artisan serve --host=0.0.0.0
--port=80  

