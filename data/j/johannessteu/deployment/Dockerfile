# DOCKER-VERSION 1.2.0  
FROM jenkins  
MAINTAINER Johannes Steu <js@johannessteu.de>  
USER root  
  
RUN apt-get update && apt-get -y install git apache2 php5 curl expect && apt-
get clean  
RUN echo 'date.timezone = "Europe/Berlin"' >> /etc/php5/cli/php.ini  
RUN mkdir -p /root/.ssh  
RUN chmod 700 /root/.ssh  
RUN curl -s https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
RUN cd /var/www && git clone
http://johannessteu.de:10080/essentials/deployment.git  
RUN cd /var/www/deployment && composer install

