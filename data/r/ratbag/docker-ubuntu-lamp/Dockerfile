FROM ubuntu:16.04  
MAINTAINER Ben Robey <benrobey@toyourdevices.com>  
LABEL Description="Lamp stack using PHP7" \  
Version="1.0"  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y \  
php7.0 \  
php7.0-common \  
php7.0-cli \  
php7.0-fpm \  
php7.0-mcrypt \  
php7.0-pgsql \  
php7.0-mbstring \  
php-mysql \  
php7.0-dom \  
php7.0-gd \  
zip unzip php7.0-zip  
  
RUN apt-get install apache2 libapache2-mod-php7.0 -y  
RUN apt-get install mariadb-common mariadb-server mariadb-client -y  
RUN apt-get install git nodejs npm composer nano tree vim curl ftp -y  
RUN npm install -g bower grunt-cli gulp  
  
COPY run.sh /usr/sbin/  
  
RUN a2enmod rewrite  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN chmod +x /usr/sbin/run.sh  
RUN chown -R www-data:www-data /var/www/html  
  
VOLUME /var/www/html  
VOLUME /var/log/httpd  
VOLUME /var/lib/mysql  
VOLUME /var/log/mysql  
  
EXPOSE 80  
EXPOSE 3306  
CMD ["/usr/sbin/run.sh"]  

