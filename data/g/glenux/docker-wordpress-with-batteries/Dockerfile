FROM wordpress:4.8.0-php7.1-apache  
MAINTAINER Glenn Y. Rolland <glenn.rolland@datatransition.net>  
  
RUN curl -L \  
https://github.com/vrana/adminer/releases/download/v4.3.1/adminer-4.3.1-mysql-
en.php \  
-o adminer.php  
  
RUN curl -L \  
https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \  
-o /usr/local/bin/wp && \  
chmod +x /usr/local/bin/wp  
  
RUN apt-get update && \  
apt-get install less && \  
apt-get autoremove  
  
ADD wp-config.php /var/www/html/wp-config.php  
  

