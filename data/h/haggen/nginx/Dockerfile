FROM debian:jessie  
  
MAINTAINER Arthur <arthur@corenzan.com>  
  
RUN groupadd -r www && useradd -r -g www www  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y ca-certificates nginx=1.9.3-1~jessie
php5-fpm php5-cli php5-mcrypt php5-mysql php5-gd php5-pgsql php5-xcache &&
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /var/log/php /var/log/php-fpm && ln -sf /dev/stdout
/var/log/nginx/static.log && ln -sf /dev/stdout /var/log/nginx/access.log &&
ln -sf /dev/stderr /var/log/nginx/error.log && ln -sf /dev/stderr
/var/log/php/error.log && ln -sf /dev/stderr /var/log/php-fpm/error.log && ln
-sf /dev/stdout /var/log/php-fpm/slow.log && ln -sf /dev/stdout /var/log/php-
fpm/access.log  
  
COPY nginx /etc/nginx  
COPY php5 /etc/php5  
COPY www /var/www  
  
VOLUME ["/var/www", "/var/log/nginx", "/etc/nginx", "/etc/php5/fpm",
"/etc/php5/fpm/pool.d", "/var/log/php", "/var/log/php-fpm"]  
  
EXPOSE 80 443  
COPY www.sh /usr/bin/www.sh  
  
CMD ["/usr/bin/www.sh"]  

