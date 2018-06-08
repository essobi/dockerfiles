FROM debian:jessie  
  
MAINTAINER Robin Schneider <ypid@riseup.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y php5-cli php5-gd php5-mysqlnd php5-curl php5-intl
php5-mcrypt php5-apcu php5-fpm nginx git  
# php5-pgsql php5-sqlite  
WORKDIR /var/www/program-o  
RUN git clone \--depth=1 https://github.com/Program-O/Program-O.git
/var/www/program-o && \  
chown --recursive www-data:www-data /var/www/program-o && \  
chmod --recursive 'u=rwX,g=,o=' /var/www/program-o  
  
ADD nginx_ssl.conf /root/  
ADD nginx.conf /root/  
ADD php.ini /etc/php5/fpm/  
ADD bootstrap.sh /usr/sbin/  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT ["bootstrap.sh"]  

