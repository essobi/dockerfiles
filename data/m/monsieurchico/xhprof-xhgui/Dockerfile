#  
# XhProf + XhGui Dockerfile  
# git@github.com:monsieurchico/docker-xhprof.git  
#  
FROM ubuntu:14.04  
MAINTAINER Romain Derocle "rderocle@gmail.com"  
# prevent debian errors  
ENV DEBIAN_FRONTEND noninteractive  
  
# users  
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb  
  
# prepare  
RUN \  
mkdir -p /var/www && \  
mkdir -p /data/xhprof && \  
mkdir -p /data/db && \  
mkdir -p /var/log/php5-fpm && \  
apt-get update && \  
apt-get -y install \  
software-properties-common \  
python-software-properties \  
python-setuptools && \  
add-apt-repository ppa:nginx/development && \  
add-apt-repository ppa:ondrej/php5-5.6 && \  
add-apt-repository ppa:git-core/ppa  
  
# install nginx  
RUN \  
apt-get install -y nginx && \  
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size
100m/" /etc/nginx/nginx.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
# install mongo  
RUN \  
apt-get install -y \  
ca-certificates curl \  
numactl \  
mongodb && \  
rm -rf /var/lib/mongodb && \  
chown -R mongodb:mongodb /data/db  
  
# install php  
RUN \  
apt-get -y install \  
php5-fpm \  
php5-cli \  
php5-mysql \  
php5-mcrypt \  
php5-mongo \  
php5-xhprof && \  
rm -f /etc/php5/fpm/conf.d/* && \  
rm -f /etc/php5/cli/conf.d/* && \  
ln -sfv /etc/php5/mods-available/*.ini /etc/php5/fpm/conf.d && \  
ln -sfv /etc/php5/mods-available/*.ini /etc/php5/cli/conf.d && \  
sed -i -e "s|;cgi.fix_pathinfo=1|cgi.fix_pathinfo=0|g" /etc/php5/fpm/php.ini
&& \  
sed -i -e "s|upload_max_filesize\s*=\s*2M|upload_max_filesize = 100M|g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s|post_max_size\s*=\s*8M|post_max_size = 100M|g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s|;daemonize\s*=\s*yes|daemonize = no|g" /etc/php5/fpm/php-fpm.conf
&& \  
sed -i -e "s|error_log.*|error_log = /var/log/php5-fpm.default.log|g"
/etc/php5/fpm/php-fpm.conf && \  
sed -i -e "s|;catch_workers_output\s*=\s*yes|catch_workers_output = yes|g"
/etc/php5/fpm/pool.d/www.conf && \  
find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
# install openssh  
RUN \  
apt-get install -y openssh-server  
  
# install supervisor  
RUN \  
apt-get install -y supervisor && \  
/usr/bin/easy_install supervisor && \  
/usr/bin/easy_install supervisor-stdout  
  
# install xhgui  
RUN \  
apt-get install -y git && \  
cd /var/www && \  
git clone https://github.com/perftools/xhgui.git && \  
cd xhgui && \  
php install.php && \  
php composer.phar --no-dev install && \  
cp config/config.default.php config/config.php  
  
# clean  
RUN \  
apt-get autoremove -y --purge \  
git \  
software-properties-common \  
python-software-properties \  
python-setuptools && \  
rm -rf /var/lib/apt/lists/*  
  
# conf  
COPY ./resources/nginx.conf /etc/nginx/sites-enabled/xhprof_vhost.conf  
COPY ./resources/phpfpm.conf /etc/php5/fpm/pool.d/xhprof_fpm.conf  
COPY ./resources/startup.sh /bin/startup.sh  
COPY ./resources/supervisord.conf /etc/supervisord.conf  
  
# ports  
EXPOSE 22 27017 33333  
# volumes  
VOLUME ["/var/log/supervisor", "/var/log/nginx", "/var/log/php5-fpm",
"/var/log/mongodb"]  
  
CMD ["/bin/bash", "/bin/startup.sh"]

