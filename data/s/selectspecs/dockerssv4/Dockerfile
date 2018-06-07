FROM debian:wheezy  
# Surpress Upstart errors/warning  
RUN dpkg-divert \--local \--rename \--add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update base image  
# Add sources for latest nginx  
# Install software requirements  
RUN apt-get update && \  
apt-get install -y wget && \  
echo "deb http://packages.dotdeb.org wheezy-php56 all" >>
/etc/apt/sources.list && \  
cd /tmp && wget \--no-check-certificate https://www.dotdeb.org/dotdeb.gpg &&
apt-key add dotdeb.gpg && \  
apt-get update && \  
apt-get upgrade -y  
  
RUN BUILD_PACKAGES="supervisor sendmail python-pip nginx-full php5-fpm git
php5-mysql php5-dev libcurl4-openssl-dev php5-curl php5-gd php5-intl
php5-mcrypt php5-memcache php5-sqlite php5-tidy php5-xmlrpc php5-xsl
php5-mysql php5-gd php5-imagick php5-imap php5-sqlite php5-xsl php5-pgsql
php5-mongo php-pear libgearman-dev libcurl4-openssl-dev libxml2-dev
libpcre3-dev libssh2-1 libssh2-1-dev" && \  
apt-get -y install $BUILD_PACKAGES && \  
pip install supervisor-stdout && \  
#install gearmand  
apt-get -y install libboost-all-dev gperf build-essential libevent-dev uuid-
dev && \  
cd /tmp && wget
https://launchpad.net/gearmand/1.2/1.1.12/+download/gearmand-1.1.12.tar.gz &&
tar xvzf gearmand-1.1.12.tar.gz && cd gearmand-1.1.12 && \  
./configure && make && make install && \  
echo "\n\n\n\n\n\n\n\n\n" | pecl install gearman && \  
echo "\n\n\n\n\n\n\n\n\n" | pecl install solr && \  
echo "\n\n\n\n\n\n\n\n\n" | pecl install -f ssh2 && \  
echo "extension=ssh2.so" > /etc/php5/mods-available/ssh2.ini && \  
echo "extension=gearman.so" > /etc/php5/mods-available/gearman.ini && \  
echo "extension=solr.so" > /etc/php5/mods-available/solr.ini && \  
php5enmod solr && \  
php5enmod gearman && \  
php5enmod ssh2 && \  
pear install Net_Gearman channel://pear.php.net/Net_Gearman-0.2.3 && \  
rm -rf /tmp/gearmand-1.1.12 && rm -rf /tmp/gearmand-1.1.12.tar.gz && rm -rf
dotdeb.gpg && \  
apt-get remove \--purge -y libboost-all-dev gperf build-essential libevent-dev
uuid-dev && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
#install phpunit  
RUN cd /tmp && wget https://phar.phpunit.de/phpunit.phar && chmod +x
phpunit.phar && mv phpunit.phar /usr/local/bin/phpunit  
# tweak nginx config  
RUN sed -i -e"s/worker_processes 1/worker_processes 5/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
&& \  
  
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size
100m/" /etc/nginx/nginx.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf  
#RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr
/var/log/nginx/error.log && ln -sf /dev/stdout /var/log/php5-fpm.log  
# tweak php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/memory_limit\s*=\s*128M/memory_limit = 512M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/max_execution_time\s*=\s*30/max_execution_time = 3600/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/sendfile\s*on/sendfile off/g" /etc/nginx/nginx.conf && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
&& \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 64/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/;access.log = log\/\$pool.access.log/access.log =
\/var\/log\/\$pool.access.log/g" /etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/;slowlog = log\/\$pool.log.slow/slowlog =
\/var\/log\/\$pool.slow.log/g" /etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/;request_slowlog_timeout = 0/request_slowlog_timeout = 5/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/;php_admin_value\\[error_log\\] = \/var\/log\/fpm-
php.www.log/php_admin_value\\[error_log\\] = \/var\/log\/\$pool.error.log/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/;php_admin_flag\\[log_errors\\] =
on/php_admin_flag\\[log_errors\\] = on/g" /etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/;pm.status_path = \/status/pm.status_path = \/status/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/;pm.max_requests = 500/pm.max_requests = 512/g"
/etc/php5/fpm/pool.d/www.conf  
  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/fpm/php.ini  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/cli/php.ini  
# fix ownership of sock file for php-fpm  
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php5/fpm/pool.d/www.conf && \  
find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
# nginx site conf  
RUN rm -Rf /etc/nginx/conf.d/* && \  
rm -Rf /etc/nginx/sites-available/default && \  
mkdir -p /etc/nginx/ssl/  
ADD ./nginx-site.conf /etc/nginx/sites-available/default.conf  
ADD ./common_server /etc/nginx/common_server  
ADD ./fastcgi_params /etc/nginx/fastcgi_params  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
# Supervisor Config  
ADD ./supervisord.conf /etc/supervisord.conf  
# Start Supervisord  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
# Setup Volume  
VOLUME ["/var/www"]  
  
# add test PHP file  
ADD ./index.php /var/www/index.php  
RUN chown -Rf www-data.www-data /var/www/  
# Expose Ports  
#EXPOSE 443  
EXPOSE 80  
  
CMD ["/bin/bash", "/start.sh"]  

