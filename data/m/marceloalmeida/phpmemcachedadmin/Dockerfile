FROM debian:jessie-backports  
  
MAINTAINER Marcelo Almeida <marcelo.almeida@jumia.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Nginx and fix php5-fpm  
RUN apt-get update && \  
apt-get install -y nginx php5-fpm php5-memcached php5-memcache php5-igbinary
php5-dev php-pear wget pkg-config re2c libmemcached-dev libssl-dev make --no-
install-recommends  
  
# Config nginx and php  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx && \  
sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/fpm/php.ini
&& \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
&& \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf  
  
# Nginx site conf  
RUN rm -Rf /etc/nginx/conf.d/* && \  
mkdir -p /etc/nginx/sites-available/ && \  
mkdir -p /etc/nginx/sites-enabled/ && \  
mkdir -p /etc/nginx/ssl/  
ADD ./nginx-site.conf /etc/nginx/sites-available/default.conf  
RUN rm /etc/nginx/sites-enabled/default && \  
ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
  
# Install php5-memcached with igbinary support  
RUN pecl download memcached-2.2.0 && \  
tar xfz memcached-2.2.0.tgz && \  
cd memcached-2.2.0 && \  
phpize && \  
./configure --enable-memcached-igbinary && \  
make && \  
make install && \  
cd .. && \  
rm memcached-2.2.0* -rf  
  
# Install phpmemcacheadmin  
RUN wget -q
http://phpmemcacheadmin.googlecode.com/files/phpMemcachedAdmin-1.2.2-r262.tar.gz
&& \  
tar xfz phpMemcachedAdmin-1.2.2-r262.tar.gz -C /usr/share/nginx/html/ && \  
rm phpMemcachedAdmin-1.2.2-r262.tar.gz  
  
# Cleanup  
RUN apt-get purge wget pkg-config re2c libmemcached-dev libssl-dev make -y &&
\  
apt-get autoremove --purge -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Define mountable directories  
RUN chown -R www-data:www-data /usr/share/nginx/html  
  
# Define working directory and volumes  
WORKDIR /etc/nginx  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/usr/share/nginx/html", "/phpmemcachedadmin"]  
  
# Expose port  
EXPOSE 80  
ADD ./start.sh /start.sh  
CMD ["/bin/bash", "/start.sh"]  

