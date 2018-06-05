FROM borales/ubuntu  
  
MAINTAINER Alexandr Bordun  
  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && apt-get update  
  
# Installing PHP packages  
RUN apt-get install -y mysql-client-5.7 \  
php7.2-cli php7.2-common php7.2-readline \  
php-apcu php7.2-curl php7.2-fpm php7.2-gd php-imagick php7.2-json \  
php7.2-intl php-memcached php7.2-mysql php-mongodb \  
php-redis php7.2-xsl php7.2-mbstring php7.2-zip php7.2-xml php7.2-opcache  
  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/"
/etc/php/7.2/cli/php.ini  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/"
/etc/php/7.2/fpm/php.ini  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/"
/etc/php/7.2/fpm/php.ini  
RUN echo "www-data ALL=(ALL) NOPASSWD:/usr/sbin/service php7.2-fpm restart" >
/etc/sudoers.d/www-data-phpfpm  
  
ADD ./run-server.sh /run-server.sh  
CMD bash -x /run-server.sh

