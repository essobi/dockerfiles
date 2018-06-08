FROM debian:wheezy  
MAINTAINER Vasiliev Ruslan dbooom.com@gmail.com  
  
# Install basic packages and build tools  
RUN apt-get update && apt-get install -y \  
wget \  
build-essential \  
libssl-dev \  
libpcre3 \  
libpcre3-dev  
  
# Get sources  
WORKDIR /tmp  
RUN wget http://nginx.org/download/nginx-1.7.6.tar.gz
http://labs.frickle.com/files/ngx_cache_purge-2.1.tar.gz  
RUN tar -zxvf nginx-1.7.6.tar.gz && mv nginx-1.7.6 nginx && rm
nginx-1.7.6.tar.gz  
RUN tar -zxvf ngx_cache_purge-2.1.tar.gz && mv ngx_cache_purge-2.1
ngx_cache_purge && rm ngx_cache_purge-2.1.tar.gz  
  
# Configure and build software  
WORKDIR /tmp/nginx  
RUN ./configure \  
\--sbin-path=/usr/local/sbin \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--user=www-data \  
\--group=www-data \  
\--with-http_gzip_static_module \  
\--with-http_ssl_module \  
\--without-mail_pop3_module \  
\--without-mail_imap_module \  
\--without-mail_smtp_module \  
\--add-module=/tmp/ngx_cache_purge  
RUN make && make install  
  
# Copy configuration files into /etc/nginx  
RUN mv /usr/local/nginx/html /var/www && \  
chown -R www-data:www-data /var/www  
  
# Fix html root directive  
RUN sed -i 's/root\s*html;.*$/root \/var\/www;/' /etc/nginx/nginx.conf  
  
# Cleaning steps  
WORKDIR /  
RUN rm -rf /tmp/nginx /tmp/ngx_cache_purge  
RUN apt-get remove -y wget build-essential libssl-dev libpcre3-dev  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN apt-get update && \  
BUILD_PACKAGES="supervisor php5-fpm php5-mysql php5-curl php5-gd php5-intl
php5-mcrypt php5-memcache php5-sqlite php5-tidy php5-xmlrpc php5-xsl
php5-pgsql pwgen" && \  
apt-get -y install $BUILD_PACKAGES && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean;  
  
# tweak php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
&& \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php5/fpm/pool.d/www.conf;  
  
# fix ownership of sock file for php-fpm  
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php5/fpm/pool.d/www.conf && \  
find /etc/php5/conf.d/ -name "*.ini" -exec sed -i -re 's/^(\s*)#(.*)/\1;\2/g'
{} \;  
  
# Supervisor Config  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Expose nginx ports  
EXPOSE 80 443  
# Run nginx in forefront  
# CMD ["nginx", "-g", "daemon off;"]  
CMD ["/usr/bin/supervisord"]  

