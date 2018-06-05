FROM apollo13/ubuntu:16.04  
MAINTAINER Bohdan Kolecek <kolecek@apollo13.cz>  
  
ENV SERVER_NAME=realitor-frontend \  
LC_CTYPE=C.UTF-8  
RUN \  
  
# Register 3rd-party package repositories  
  
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 00A6F0A3C300EE8C && \  
echo 'deb http://ppa.launchpad.net/nginx/stable/ubuntu xenial main' >
/etc/apt/sources.list.d/nginx-stable-trusty.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C && \  
echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >
/etc/apt/sources.list.d/ondrej-php-xenial.list && \  
apt-get update && \  
  
# Install nginx  
  
apt-get update && \  
apt-get install -y nginx && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx && \  
  
# Install PHP 7  
  
apt-get -y install \  
php-imagick php-msgpack php-redis \  
php7.0-bcmath php7.0-cli php7.0-pgsql php7.0-gd php7.0-curl php7.0-mbstring
php7.0-sqlite3 php7.0-xml php7.0-zip php7.0-fpm && \  
  
service php7.0-fpm restart && \  
  
# Install Composer  
  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
  
# Install supervisord  
  
dpkg-divert --local --rename --add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl && \  
apt-get install -y supervisor && \  
  
# Setup directories  
  
mkdir /run/php && \  
mkdir /var/www/realitor-frontend && \  
  
# Clean up  
  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
  
# Fix permissions for VirtualBox Docker host  
  
usermod -u 1000 www-data  
  
COPY config/php/custom.ini /etc/php/7.0/fpm/conf.d/  
COPY config/php/custom.conf config/php/www.conf /etc/php/7.0/fpm/pool.d/  
COPY config/supervisor /etc/supervisor/conf.d  
COPY config/nginx/sites-available/default /etc/nginx/sites-available/  
COPY bin/run.sh /  
COPY bin/build.sh /usr/local/bin/  
  
VOLUME /var/www/realitor-frontend  
  
EXPOSE 80  
ENV EC2_ENVIRONMENT=false  
  
CMD [ "/run.sh" ]  

