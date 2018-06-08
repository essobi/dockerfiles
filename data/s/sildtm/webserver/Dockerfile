FROM ubuntu:14.04  
MAINTAINER Sild <failsild@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y software-properties-common curl && \  
add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get install -y --force-yes php7.0 php7.0-mysql \  
php7.0-json php7.0-curl php7.0-mbstring \  
apache2 libapache2-mod-php7.0 && \  
a2enmod rewrite  
  
RUN curl -o /etc/apache2/sites-available/000-default.conf
https://raw.githubusercontent.com/sild/docker_builds/webserver-
php7/000-default.conf  
  
EXPOSE 80  
WORKDIR /var/www/html  
  
ENTRYPOINT ["apachectl", "-DFOREGROUND" ]  

