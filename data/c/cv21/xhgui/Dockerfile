FROM php:5-fpm  
  
MAINTAINER Vitaly Bolychev <vitaly.bolychev@gmail.com>  
  
# install mongodb according official docs  
# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.2 main"
| tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
RUN apt-get update  
RUN apt-get install -y mongodb-org  
  
# install and configure mcrypt  
RUN apt-get update && apt-get install -y libmcrypt-dev && docker-php-ext-
install -j$(nproc) mcrypt  
  
# install libssl for pecl  
RUN apt-get install -y libssl-dev  
  
# install mongodb driver and zip extension via pecl  
RUN pecl install mongodb && docker-php-ext-enable mongodb  
RUN pecl install zip && docker-php-ext-enable zip  
  
# install nginx  
RUN apt-get install -y nginx  
  
# set up config files  
COPY ./nginx/default.conf /etc/nginx/sites-enabled/default  
COPY ./php-fpm/timezone.ini /usr/local/etc/php/conf.d  
  
ADD ./xhgui/ /var/www/xhgui/  
  
WORKDIR /var/www/xhgui  
  
RUN mkdir -p /data/db && chmod -R 777 /data/db  
  
RUN php install.php  
RUN chown -R www-data:www-data /var/www/xhgui  
  
CMD service nginx start && php-fpm -D && mongod  
  
# expose nginx and mongodb ports  
EXPOSE 80 27017

