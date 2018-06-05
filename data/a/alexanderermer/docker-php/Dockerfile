FROM debian:jessie  
  
RUN apt-get update -y  
RUN apt-get install apache2 make build-essential debconf-utils -y  
RUN printf 'mysql-server mysql-server/root_password password ""' | debconf-
set-selections  
RUN printf 'mysql-server mysql-server/root_password_again password ""' |
debconf-set-selections  
RUN apt-get install mysql-server -y  
RUN apt-get install php5-mysql curl wget git zlib1g-dev libbz2-dev -y  
RUN apt-get install php5 libapache2-mod-php5 php5-mcrypt php5-mysql php5-curl
php5-gd php5-intl php-pear php5-imagick php5-imap php5-mcrypt php5-memcache
php5-recode php5-sqlite php5-tidy php5-xmlrpc php5-xsl -y  
  
RUN export DEBIAN_FRONTEND=noninteractive  
RUN curl -sS https://getcomposer.org/installer | php  
  
EXPOSE 22 80  
CMD ["/usr/sbin/apache2ctl -D FOREGROUND"]  

