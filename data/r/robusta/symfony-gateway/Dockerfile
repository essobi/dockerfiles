FROM tutum/lamp  
MAINTAINER Nicolas Zozol <nz@robusta.io>  
  
# Classic LAMP with Symfony and Node JS 4  
  
# Add some php5 extension  
RUN apt-get update && apt-get install -y vim curl php5-common php5-cli
php5-fpm php5-mcrypt php5-mysql php5-apcu php5-gd php5-imagick php5-curl
php5-intl  
  
#ADD symfony.ini /etc/php5/fpm/conf.d/  
#ADD symfony.ini /etc/php5/cli/conf.d/  
  
#ADD symfony.pool.conf /etc/php5/fpm/pool.d/  
  
# Docker user has id 1000  
RUN usermod -u 1000 www-data  
  
# Composer SHOULD be run inside the host, with the code  
#ENV COMPOSER_VERSION 1.0.0-alpha11  
  
# Install Composer  
#RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer #--version=${COMPOSER_VERSION}  
  
#RUN unlink /var/www/html && rm -rf /app  
  
  
  
#RUN ./mysql-script.sh  
  
COPY composer.phar /bin/composer  
RUN chmod +x /bin/composer  
#RUN mv /bin/composer.phar /bin/composer  
  
  
  
WORKDIR /app  
  
## This script must be run AFTER the code is uploaded  
COPY install.sh ./install.sh  
RUN chmod +x ./install.sh  
  
  
VOLUME /app  
  
#RUN composer install --no-scripts  
# then use git clone, then composer install  
#VOLUME /app  
  
# Command to run :  
#docker run -d --name symfony -v /app:/app robusta/symfony-gateway  
#/Users/nicorama/code/clients/store-gateway/path  
  
#Mac :  
#docker run -d --name symfony -v /Users/nicorama/code/clients/store-
gateway/path:/app -p 80:80 robusta/symfony-gateway  
#docker-machine ls  
#docker-machine ip default # that's why 80 needs to be forwarded...  
  
#php app/console cache:clear  
# php app/console doctrine:schema:update --force  
# php app/console doctrine:fixtures:load  
  
#docker run -d --name symfony -v /Users/nicorama/code/clients/store-
gateway/path:/app -p 80:80 robusta/symfony-gateway  
#docker exec symfony git clone https://nicorama@bitbucket.org/robusta-
code/store-gateway.git  
  
#docker exec symfony /bin/sh -c 'cd store-gateway/path/;composer install'  
#docker exec symfony /mysql-script.sh  
#docker exec symfony chmod -R 777 /app/app/logs  
#docker exec symfony chmod -R 777 /app/app/cache  
  
#docker run -d --name symfony -v /Users/nicorama/code/clients/store-
gateway/path:/app -p 80:80 robusta/symfony-gateway

