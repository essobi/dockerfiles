FROM debian:jessie  
  
MAINTAINER takatost <takatost@gmail.com>  
  
ENV NGINX_VERSION 1.11.5  
ENV PHP_VERSION 7.0.12  
ENV FILEBEAT_VERSION=5.2.2 \  
FILEBEAT_SHA1=0f8e2f5f1145051435352b0e6a8b776040ea36e4  
  
COPY configs/pear_install.sh /tmp/  
COPY configs/go-pear.phar /tmp/  
#Add cron config  
COPY configs/schedule.sh /  
COPY configs/www /etc/cron.d/  
  
COPY configs/start.sh /  
  
RUN set -x  
  
RUN apt-get update && \  
apt-get install -y git \  
wget \  
curl \  
cron \  
gcc \  
build-essential \  
autoconf \  
automake \  
libtool \  
make \  
cmake \  
expect \  
dstat \  
libbz2-dev \  
libcurl4-openssl-dev\  
libssl-dev \  
libgd2-dev \  
libpcre3-dev \  
libfreetype6-dev \  
libxml2-dev \  
libpng++-dev \  
libmcrypt-dev \  
python-setuptools \  
vim && \  
#Set Timezone  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
#Add user  
mkdir -p /data/www && \  
useradd -r -s /sbin/nologin -d /data/www -m -k no www && \  
#Download nginx & php  
mkdir -p /home/nginx-php && cd $_ && \  
curl -Lk http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz | gunzip | tar
x -C /home/nginx-php && \  
curl -Lk http://php.net/distributions/php-$PHP_VERSION.tar.gz | gunzip | tar x
-C /home/nginx-php && \  
#Make install nginx  
cd /home/nginx-php/nginx-$NGINX_VERSION && \  
./configure --prefix=/usr/local/nginx \  
\--user=www --group=www \  
\--error-log-path=/var/log/nginx_error.log \  
\--http-log-path=/var/log/nginx_access.log \  
\--pid-path=/var/run/nginx.pid \  
\--with-pcre \  
\--with-http_v2_module \  
\--with-http_ssl_module \  
\--without-mail_pop3_module \  
\--without-mail_imap_module \  
\--with-http_gzip_static_module && \  
make && make install && \  
ln -s /usr/local/nginx/sbin/nginx /usr/local/bin/nginx && \  
#Make install php  
cd /home/nginx-php/php-$PHP_VERSION && \  
./configure --prefix=/usr/local/php \  
\--with-config-file-path=/usr/local/php/etc \  
\--with-config-file-scan-dir=/usr/local/php/etc/php.d \  
\--with-fpm-user=www \  
\--with-fpm-group=www \  
\--with-mcrypt=/usr/include \  
\--with-pdo-mysql \  
\--with-openssl \  
\--with-gd \  
\--with-iconv \  
\--with-zlib \  
\--with-curl \  
\--with-png-dir \  
\--with-jpeg-dir \  
\--with-freetype-dir \  
\--with-xmlrpc \  
\--with-mhash \  
\--enable-fpm \  
\--enable-xml \  
\--enable-inline-optimization \  
\--enable-mbregex \  
\--enable-mbstring \  
\--enable-ftp \  
\--enable-gd-native-ttf \  
\--enable-pcntl \  
\--enable-sockets \  
\--enable-zip \  
\--enable-soap \  
\--enable-session \  
\--enable-opcache \  
\--enable-bcmath \  
\--enable-exif \  
\--enable-fileinfo \  
\--disable-rpath \  
\--enable-ipv6 \  
\--disable-debug \  
\--without-pear && \  
make && make install && \  
#Install php-fpm  
cd /home/nginx-php/php-$PHP_VERSION && \  
cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf &&
\  
ln -s /usr/local/php/bin/php /usr/local/bin/php && \  
#Install supervisor  
easy_install supervisor && \  
mkdir -p /var/{log/supervisor,run/{sshd,supervisord}} && \  
#Install filebeat  
wget
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz
-O /tmp/filebeat.tar.gz && \  
cd /tmp && \  
echo "${FILEBEAT_SHA1} filebeat.tar.gz" | sha1sum -c - && \  
tar xzvf filebeat.tar.gz && \  
cd filebeat-* && \  
cp filebeat /bin && \  
cd /tmp && \  
rm -rf filebeat* && \  
  
#Clean OS  
apt-get remove -y gcc \  
build-essential \  
autoconf \  
automake \  
libtool \  
make \  
expect \  
dstat \  
wget \  
python-setuptools \  
cmake && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/* /etc/my.cnf{,.d} && \  
rm -rf /home/nginx-php && \  
  
#Change Mod from webdir  
chown -R www:www /data/www && \  
  
#Add supervisord conf  
mkdir -p /etc/supervisor/conf.d && \  
  
#Modify Cron Configs  
chown www.www /schedule.sh && \  
chmod +x /schedule.sh && \  
crontab /etc/cron.d/www && \  
touch /var/log/cron.log && \  
touch /tmp/cron.log && \  
chown www.www /tmp/cron.log && \  
  
#Add Start Script Priviliages  
chmod +x /start.sh  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php --install-dir=/bin --filename=composer && \  
chmod +x /bin/composer && \  
php -r "unlink('composer-setup.php');" && \  
composer global require "hirak/prestissimo:^0.3"  
  
COPY configs/supervisord.conf /etc/supervisor/  
COPY configs/conf.d/ /etc/supervisor/conf.d/  
  
#Update nginx config  
COPY configs/nginx.conf /usr/local/nginx/conf/  
  
#Update php config  
COPY configs/php.ini /usr/local/php/etc/  
  
#Update php pool config  
COPY configs/www.conf /usr/local/php/etc/php-fpm.d/  
  
#Add Filebeat config  
COPY configs/filebeat.yml /filebeat.yml  
  
WORKDIR /data/www  
  
#Set port  
EXPOSE 80 443  
  
#Start it  
ENTRYPOINT ["/start.sh"]  

