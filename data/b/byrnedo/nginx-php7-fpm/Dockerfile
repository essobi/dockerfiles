FROM ubuntu:16.04  
MAINTAINER Donal Byrne <byrnedo@tcd.ie>  
  
# Surpress Upstart errors/warning  
RUN dpkg-divert --local --rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update base image  
# Add sources for latest nginx  
# Install software requirements  
#  
ENV ERRORS=0  
ENV IMAGE_PHP_VERSION=7.1  
  
RUN apt-get update && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C && \  
apt-get install -y software-properties-common && \  
nginx=stable && \  
add-apt-repository ppa:nginx/$nginx && \  
LANG=C.UTF-8 add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get -y install supervisor \  
nginx-extras \  
php${IMAGE_PHP_VERSION}-fpm \  
git \  
php${IMAGE_PHP_VERSION}-mysql \  
php-apcu \  
php${IMAGE_PHP_VERSION}-curl \  
php${IMAGE_PHP_VERSION}-gd \  
php${IMAGE_PHP_VERSION}-intl \  
php${IMAGE_PHP_VERSION}-mcrypt \  
php${IMAGE_PHP_VERSION}-memcache \  
php${IMAGE_PHP_VERSION}-sqlite \  
php${IMAGE_PHP_VERSION}-tidy \  
php${IMAGE_PHP_VERSION}-xmlrpc \  
php${IMAGE_PHP_VERSION}-xsl \  
php${IMAGE_PHP_VERSION}-pgsql \  
php${IMAGE_PHP_VERSION}-mongo \  
php${IMAGE_PHP_VERSION}-ldap \  
pwgen \  
php${IMAGE_PHP_VERSION}-cli \  
curl && \  
apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
update-alternatives --set php /usr/bin/php${IMAGE_PHP_VERSION} && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN mkdir /opt/lua && \  
git clone https://github.com/knyar/nginx-lua-prometheus.git /tmp/lua-prom && \  
cp /tmp/lua-prom/prometheus.lua /opt/lua/ && \  
nginx -v  
  
# tweak nginx config  
RUN sed -i -e"s/worker_processes 1/worker_processes auto/"
/etc/nginx/nginx.conf && \  
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size
100m/" /etc/nginx/nginx.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# tweak php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php/${IMAGE_PHP_VERSION}/fpm/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/${IMAGE_PHP_VERSION}/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/${IMAGE_PHP_VERSION}/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g"
/etc/php/${IMAGE_PHP_VERSION}/fpm/php-fpm.conf && \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf  
  
# fix ownership of sock file for php-fpm  
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php/${IMAGE_PHP_VERSION}/fpm/pool.d/www.conf && \  
find /etc/php/${IMAGE_PHP_VERSION}/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \; && \  
mkdir /run/php  
  
  
COPY ./default.conf.tmpl /etc/nginx/sites-available/default.conf  
COPY ./metrics.conf /etc/nginx/sites-available/metrics.conf  
COPY ./supervisord.conf /etc/supervisord.conf  
COPY ./cmd.sh /  
COPY ./index.php /usr/share/nginx/html/index.php  
  
RUN phpenmod mcrypt && \  
rm -Rf /etc/nginx/conf.d/* && \  
mkdir -p /etc/nginx/ssl/ && \  
rm -f /etc/nginx/sites-enabled/default && \  
ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default
&& \  
ln -s /etc/nginx/sites-available/metrics.conf /etc/nginx/sites-enabled/metrics
&& \  
chmod 755 /cmd.sh && \  
chown -Rf www-data.www-data /usr/share/nginx/html/  
# Expose Ports  
EXPOSE 80 9000  
CMD ["/bin/bash", "/cmd.sh"]  

