FROM ubuntu:14.04.2  
MAINTAINER Adnan Issadeen <adnan.issadeen@live.com>  
  
RUN apt-get update && apt-get install wget curl sqlite3 nginx vim -y --force-
yes  
RUN apt-get install mysql-server php5 php5-cli php5-fpm php5-curl php5-common
php5-gd php5-mysql -y --force-yes  
ADD nginxfile /etc/nginx/sites-available/phpapp  
RUN rm /etc/nginx/sites-enabled/default && ln -s /etc/nginx/sites-
available/phpapp /etc/nginx/sites-enabled/phpapp  
RUN mkdir /usr/src/phppackages  
WORKDIR /usr/src/phppackages  
RUN wget https://phar.phpunit.de/phpunit.phar && chmod a+x phpunit.phar && mv
phpunit.phar /usr/local/bin/phpunit  
RUN curl -LsS http://symfony.com/installer > symfony.phar && mv symfony.phar
/usr/local/bin/symfony && chmod a+x /usr/local/bin/symfony  
WORKDIR /  

