FROM 1and1internet/ubuntu-16-nginx  
MAINTAINER brian.wojtczak@1and1.co.uk  
ARG DEBIAN_FRONTEND=noninteractive  
COPY files /  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository -y -u ppa:ondrej/php && \  
apt-get update && \  
apt-get install -y imagemagick graphicsmagick && \  
apt-get install -y php7.2-bcmath php7.2-bz2 php7.2-cli php7.2-common
php7.2-curl php7.2-dba php7.2-fpm php7.2-gd php7.2-gmp php7.2-imap php7.2-intl
php7.2-ldap php7.2-mbstring php7.2-mysql php7.2-odbc php7.2-pgsql
php7.2-recode php7.2-snmp php7.2-soap php7.2-sqlite php7.2-tidy php7.2-xml
php7.2-xmlrpc php7.2-xsl php7.2-zip && \  
apt-get install -y php-gnupg php-imagick php-mongodb php-streams php-fxsl && \  
mkdir /tmp/composer/ && \  
cd /tmp/composer && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
chmod a+x /usr/local/bin/composer && \  
cd / && \  
rm -rf /tmp/composer && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /etc/nginx/sites-enabled/default /etc/nginx/sites-available/* && \  
sed -i -e 's/^user = www-data$/;user = www-data/g'
/etc/php/7.2/fpm/pool.d/www.conf && \  
sed -i -e 's/^group = www-data$/;group = www-data/g'
/etc/php/7.2/fpm/pool.d/www.conf && \  
sed -i -e 's/^listen.owner = www-data$/;listen.owner = www-data/g'
/etc/php/7.2/fpm/pool.d/www.conf && \  
sed -i -e 's/^listen.group = www-data$/;listen.group = www-data/g'
/etc/php/7.2/fpm/pool.d/www.conf && \  
sed -i -e 's/max_execution_time = 30/max_execution_time = 300/g'
/etc/php/7.2/fpm/php.ini && \  
sed -i -e 's/upload_max_filesize = 2M/upload_max_filesize = 256M/g'
/etc/php/7.2/fpm/php.ini && \  
sed -i -e 's/post_max_size = 8M/post_max_size = 512M/g'
/etc/php/7.2/fpm/php.ini && \  
sed -i -e 's/memory_limit = 128M/memory_limit = 512M/g'
/etc/php/7.2/fpm/php.ini && \  
sed -i -e 's/fastcgi_param SERVER_PORT $server_port;/fastcgi_param SERVER_PORT
$http_x_forwarded_port;/g' /etc/nginx/fastcgi.conf && \  
sed -i -e 's/fastcgi_param SERVER_PORT $server_port;/fastcgi_param SERVER_PORT
$http_x_forwarded_port;/g' /etc/nginx/fastcgi_params && \  
sed -i -e '/sendfile on;/a\ fastcgi_read_timeout 300\;' /etc/nginx/nginx.conf
&& \  
mkdir -p /usr/src/tmp/ioncube && \  
curl -fSL
"http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz"
-o /usr/src/tmp/ioncube_loaders_lin_x86-64.tar.gz && \  
tar xfz /usr/src/tmp/ioncube_loaders_lin_x86-64.tar.gz -C /usr/src/tmp/ioncube
&& \  
cp /usr/src/tmp/ioncube/ioncube/ioncube_loader_lin_7.2.so
/usr/lib/php/20170718/ && \  
mkdir --mode 777 /var/run/php && \  
chmod 755 /hooks /var/www && \  
chmod -R 777 /var/www/html /var/log && \  
sed -i -e 's/index index.html/index index.php index.html/g' /etc/nginx/sites-
enabled/site.conf && \  
chmod 666 /etc/nginx/sites-enabled/site.conf && \  
nginx -t && \  
mkdir -p /run /var/lib/nginx /var/lib/php && \  
chmod -R 777 /run /var/lib/nginx /var/lib/php /etc/php/7.2/fpm/php.ini  

