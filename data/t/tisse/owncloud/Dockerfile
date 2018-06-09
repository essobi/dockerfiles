FROM ubuntu:14.04  
MAINTAINER Chris Pettersson  
  
RUN apt-get update && \  
apt-get install -y php5-cli php5-gd php5-pgsql php5-curl php5-intl php5-mcrypt
\  
php5-ldap php5-gmp php5-apcu php5-imagick php5-sqlite php5-fpm smbclient nginx
wget  
  
RUN wget http://de.archive.ubuntu.com/ubuntu/pool/universe/p/php-
apcu/php5-apcu_4.0.6-1_amd64.deb  
RUN apt-get -y purge php5-apcu  
RUN dpkg -i php5-apcu_4.0.6-1_amd64.deb  
  
ADD bootstrap.sh /usr/bin/  
ADD nginx_ssl.conf /root/  
ADD nginx.conf /root/  
ADD owncloud-8.1.3.tar.bz2 /var/www/  
  
RUN chown -R www-data:www-data /var/www &&\  
chmod +x /usr/bin/bootstrap.sh  
  
ADD php.ini /etc/php5/fpm/  
  
EXPOSE 443  
VOLUME /var/www/owncloud/data  
VOLUME /var/www/owncloud/config  
VOLUME /root/ssl  
  
ENTRYPOINT ["bootstrap.sh"]  
  

