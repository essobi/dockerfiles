FROM ubuntu:14.04  
MAINTAINER Raphael Bottino <raphabot@gmail.com>  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install git mysql-client mysql-server apache2 libapache2-mod-php5
pwgen python-setuptools vim-tiny php5-mysql php-apc php5-gd php5-curl
php5-memcache memcached drush mc && \  
apt-get autoclean  
  
ADD start.sh /start.sh  
RUN chmod 775 /start.sh  
  
ENTRYPOINT ["/start.sh"]  

