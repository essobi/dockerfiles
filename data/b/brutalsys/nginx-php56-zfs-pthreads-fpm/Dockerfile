FROM ubuntu:14.04.2  
MAINTAINER Elliot Morales <elliot@brutalsys.com >  
  
# Enviroment Variable  
ENV NEWRELIC_LICENSE false  
ENV NEWRELIC_APP false  
ENV PHP_CHILDREN false  
ENV PHP_VERSION 5.6.18  
# Surpress Upstart errors/warning  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update base image  
# Add sources for latest nginx  
# Install software requirements  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
nginx=stable && \  
add-apt-repository ppa:nginx/$nginx && \  
apt-get update && \  
apt-get upgrade -y && \  
BUILD_PACKAGES="supervisor nginx pwgen wget autoconf build-essential libfcgi-
dev libfcgi0ldbl libjpeg62-dbg libmcrypt-dev libssl-dev libc-client2007e libc-
client2007e-dev libxml2-dev" && \  
apt-get -y install $BUILD_PACKAGES && \  
ln -s /usr/lib/libc-client.a /usr/lib/x86_64-linux-gnu/libc-client.a && \  
apt-get -y build-dep php5 && \  
mkdir -p /opt/php-$PHP_VERSION && \  
mkdir -p mkdir /usr/local/src/php5-build && \  
cd /usr/local/src/php5-build && \  
wget http://de.php.net/get/php-$PHP_VERSION.tar.bz2/from/this/mirror -O
php-$PHP_VERSION.tar.bz2 && \  
tar jxf php-$PHP_VERSION.tar.bz2 && \  
cd php-$PHP_VERSION && \  
./configure \  
\--prefix=/opt/php-$PHP_VERSION \  
\--enable-maintainer-zts \  
\--with-pdo-pgsql \  
\--with-zlib-dir \  
\--with-freetype-dir \  
\--enable-mbstring \  
\--with-libxml-dir=/usr \  
\--enable-soap \  
\--enable-calendar \  
\--with-curl \  
\--with-mcrypt \  
\--with-zlib \  
\--with-gd \  
\--with-pgsql \  
\--disable-rpath \  
\--enable-inline-optimization \  
\--with-bz2 \  
\--with-zlib \  
\--enable-sockets \  
\--enable-sysvsem \  
\--enable-sysvshm \  
\--enable-pcntl \  
\--enable-mbregex \  
\--enable-exif \  
\--enable-bcmath \  
\--with-mhash \  
\--enable-zip \  
\--with-pcre-regex \  
\--with-mysql \  
\--with-pdo-mysql \  
\--with-mysqli \  
\--with-jpeg-dir=/usr \  
\--with-png-dir=/usr \  
\--enable-gd-native-ttf \  
\--with-openssl \  
\--with-fpm-user=www-data \  
\--with-fpm-group=www-data \  
\--with-libdir=/lib/x86_64-linux-gnu \  
\--enable-ftp \  
\--with-imap \  
\--with-imap-ssl \  
\--with-kerberos \  
\--with-gettext \  
\--with-xmlrpc \  
\--with-xsl \  
\--enable-opcache \  
\--enable-fpm && \  
make && make install && \  
cp /usr/local/src/php5-build/php-$PHP_VERSION/php.ini-production
/opt/php-$PHP_VERSION/lib/php.ini && \  
cp /opt/php-$PHP_VERSION/etc/php-fpm.conf.default
/opt/php-$PHP_VERSION/etc/php-fpm.conf && \  
/opt/php-$PHP_VERSION/bin/pecl install pthreads-1.0.0 && \  
echo "extension=pthreads.so" >> /opt/php-$PHP_VERSION/lib/php.ini  
  
RUN apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
# tweak nginx config  
RUN sed -i -e"s/worker_processes 1/worker_processes 5/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size
100m/" /etc/nginx/nginx.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# tweak php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/opt/php-$PHP_VERSION/lib/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/opt/php-$PHP_VERSION/lib/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/opt/php-$PHP_VERSION/lib/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/opt/php-$PHP_VERSION/lib/php.ini && \  
sed -i -e "s/short_open_tag = Off/short_open_tag = On/g"
/opt/php-$PHP_VERSION/lib/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g"
/opt/php-$PHP_VERSION/etc/php-fpm.conf && \  
sed -i -e "s/log_errors = On/log_errors = Off/g"
/opt/php-$PHP_VERSION/lib/php.ini  
  
# nginx site conf  
RUN rm -Rf /etc/nginx/conf.d/* && \  
rm -Rf /etc/nginx/sites-available/default && \  
mkdir -p /etc/nginx/ssl/  
ADD ./nginx-site.conf /etc/nginx/sites-available/default.conf  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
RUN echo -e "[global]\nerror_log = /dev/null\ndaemonize =
no\ninclude=etc/pool.d/*.conf" > /opt/php-$PHP_VERSION/etc/php-fpm.conf  
# Install and Configure Newrelic  
RUN sed -i 's/^# \\(.*-backports\s\\)/\1/g' /etc/apt/sources.list && \  
wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list && \  
apt-get update -qqy  
RUN apt-get install newrelic-php5 -y  
  
# Add static PHP-FPM Config  
ADD ./www.conf /opt/php-$PHP_VERSION/etc/pool.d/www.conf  
  
# Supervisor Config  
ADD ./supervisord.conf /etc/supervisord.conf  
RUN sed -i "s/PHP_VERSION/$PHP_VERSION/g" /etc/supervisord.conf  
# Start Supervisord  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# add test PHP file  
# ADD ./index.php /usr/share/nginx/html/index.php  
RUN chown -Rf www-data.www-data /usr/share/nginx/html/  
VOLUME /usr/share/nginx/html  
# Expose Ports  
EXPOSE 443  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  

