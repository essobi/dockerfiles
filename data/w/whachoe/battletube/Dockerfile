FROM luis/laravel-nginx:latest  
MAINTAINER Jo Giraerts <jo.giraerts@gmail.com>  
  
# Make sure PHP has pecl and intl  
RUN apt-get update && apt-get install -y php5-dev php5-intl  
  
# Install php mongo extension  
RUN pecl install mongo  
RUN echo "extension=mongo.so" > /etc/php5/mods-available/mongo.ini  
RUN ln -s /etc/php5/mods-available/mongo.ini /etc/php5/fpm/conf.d/20-mongo.ini  
RUN ln -s /etc/php5/mods-available/mongo.ini /etc/php5/cli/conf.d/20-mongo.ini  
  
# Install our app  
ADD . /var/www  
RUN chown -R www-data:www-data /var/www  
  
# Make sure our queue-service gets started too  
ADD ./sysconfig/supervisord-battletube.conf /etc/supervisor/conf.d/battletube-
queue.conf  

