FROM centos/s2i-core-centos7  
MAINTAINER Skiychan <joao@getupcloud.com>  
  
ENV NGINX_VERSION 1.11.6  
ENV PHP_VERSION 7.1.0  
  
RUN set -x && \  
yum install -y gcc \  
gcc-c++ \  
autoconf \  
automake \  
libtool \  
make \  
cmake && \  
  
#Install PHP library  
## libmcrypt-devel DIY  
rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm && \  
yum install -y zlib \  
zlib-devel \  
openssl \  
openssl-devel \  
pcre-devel \  
libxml2 \  
libxml2-devel \  
libcurl \  
libcurl-devel \  
libpng-devel \  
libjpeg-devel \  
freetype-devel \  
libmcrypt-devel \  
openssh-server \  
python-setuptools && \  
  
#Add user  
mkdir -p /data/{www,phpext} && \  
useradd -r -s /sbin/nologin -d /data/www -m -k no www && \  
  
#Download nginx & php  
mkdir -p /home/nginx-php && cd $_ && \  
curl -Lk http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz | gunzip | tar
x -C /home/nginx-php && \  
curl -Lk http://php.net/distributions/php-$PHP_VERSION.tar.gz | gunzip | tar x
-C /home/nginx-php && \  
  
#Make install nginx  
cd /home/nginx-php/nginx-$NGINX_VERSION && \  
./configure \--prefix=/usr/local/nginx \  
\--user=www \--group=www \  
\--error-log-path=/opt/app-root/src/log/nginx_error.log \  
\--http-log-path=/opt/app-root/src/log/nginx_access.log \  
\--pid-path=/var/run/nginx.pid \  
\--with-pcre \  
\--with-http_ssl_module \  
\--without-mail_pop3_module \  
\--without-mail_imap_module \  
\--with-http_gzip_static_module && \  
make && make install && \  
  
#Make install php  
cd /home/nginx-php/php-$PHP_VERSION && \  
./configure \--prefix=/usr/local/php \  
\--with-config-file-path=/usr/local/php/etc \  
\--with-config-file-scan-dir=/usr/local/php/etc/php.d \  
\--with-fpm-user=www \  
\--with-fpm-group=www \  
\--with-mcrypt=/usr/include \  
\--with-mysqli \  
\--with-pdo-mysql \  
\--with-openssl \  
\--with-gd \  
\--with-iconv \  
\--with-zlib \  
\--with-gettext \  
\--with-curl \  
\--with-png-dir \  
\--with-jpeg-dir \  
\--with-freetype-dir \  
\--with-xmlrpc \  
\--with-mhash \  
\--enable-fpm \  
\--enable-xml \  
\--enable-shmop \  
\--enable-sysvsem \  
\--enable-inline-optimization \  
\--enable-mbregex \  
\--enable-mbstring \  
\--enable-ftp \  
\--enable-gd-native-ttf \  
\--enable-mysqlnd \  
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
cp php.ini-production /usr/local/php/etc/php.ini && \  
cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf &&
\  
cp /usr/local/php/etc/php-fpm.d/www.conf.default /usr/local/php/etc/php-
fpm.d/www.conf && \  
  
#Install supervisor  
easy_install supervisor && \  
mkdir -p /var/{log/supervisor,run/{sshd,supervisord}} && \  
  
#Clean OS  
yum remove -y gcc \  
gcc-c++ \  
autoconf \  
automake \  
libtool \  
make \  
cmake && \  
yum clean all && \  
rm -rf /tmp/* /var/cache/{yum,ldconfig} /etc/my.cnf{,.d} && \  
mkdir -p \--mode=0755 /var/cache/{yum,ldconfig} && \  
find /var/log -type f -delete && \  
rm -rf /home/nginx-php && \  
  
#Change Mod from webdir  
chown -R www:www /data/www  
  
ADD extini/ /usr/local/php/etc/php.d/  
ADD extfile/ /data/phpext/  
  
RUN yum install -y gcc gcc-c++ autoconf automake libtool make cmake && \  
mkdir -p /home/extension && \  
sh /data/phpext/extension.sh && \  
mv /data/phpext/extension.sh /data/phpext/extension_back.sh  
#Clean OS  
RUN yum remove -y gcc gcc-c++ autoconf automake libtool make cmake && \  
yum clean all && \  
rm -rf /tmp/* /var/cache/{yum,ldconfig} /etc/my.cnf{,.d} && \  
mkdir -p \--mode=0755 /var/cache/{yum,ldconfig} && \  
find /var/log -type f -delete && \  
rm -rf /home/extension/*  
  
  
#Add supervisord conf  
ADD supervisord.conf /etc/  
#Update nginx config  
ADD nginx.conf.template /  
  
#Add Start  
ADD start.sh /  
RUN chmod +x /start.sh  
#Set port  
EXPOSE 8080 8443  
  
# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH  
COPY ./s2i/bin/ $STI_SCRIPTS_PATH  
  
### FIX  
RUN chmod 770 /usr/local/php/var/log/ /var/log/ /usr/local/nginx/  
  
ADD php.ini /usr/local/php/etc/php.ini  
  
RUN mkdir -p /opt/app-root/src/log && chmod 770 /opt/app-root/src/log  
  
RUN chmod 770 /usr/local/nginx/conf/nginx.conf  
########################################################################  
  
USER 1001  
  
RUN mkdir /opt/app-root/src/nginx  
#Start it  
#ENTRYPOINT ["/start.sh"]  
#Start web server  
#CMD ["/bin/bash", "/start.sh"]  
  
CMD $STI_SCRIPTS_PATH/usage  

