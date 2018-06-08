FROM quitoque/debian-jessie  
  
MAINTAINER Rémi Chomat <remi@quitoque.fr>  
  
# Update repositories  
RUN apt-get update  
  
RUN apt-get install -y php-http php-http-request php-net-socket php-net-url
php-pear php5-cli php5-common php5-curl php5-dev php5-gd php5-intl php5-ldap
php5-mcrypt php5-mysql php5-xsl php5-xdebug  
  
COPY files/xdebug.ini /tmp/xdebug.ini  
RUN cat /tmp/xdebug.ini > /etc/php5/mods-available/xdebug.ini  
CMD rm /tmp/xdebug.ini  

