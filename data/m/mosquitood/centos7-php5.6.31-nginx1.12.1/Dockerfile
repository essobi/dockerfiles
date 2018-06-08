FROM centos:7  
LABEL maintainer="Mosquitood<mosquitood@gmail.com>"  
ENV NGINX_VERSION 1.12.1  
ENV PHP_VERSION 5.6.31  
ENV RUN_USER www  
ENV NGINX_INSTALL_DIR /usr/local/nginx  
ENV PHP_INSTALL_DIR /usr/local/php  
ENV PYTHON_INSTALL_DIR /usr/local/python  
ENV OPENSSL_INSTALL_DIR /usr/local/openssl  
ENV WWWROOT_DIR /data/wwwroot  
ENV WWWLOGS_DIR /data/wwwlogs  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7  
RUN sed -i 's@LANG=.*$@LANG="en_US.UTF-8"@g' /etc/locale.conf  
RUN mkdir -p $NGINX_INSTALL_DIR $PHP_INSTALL_DIR $OPENSSL_INSTALL_DIR
$PYTHON_INSTALL_DIR $WWWLOGS_DIR $WWWROOT_DIR  
RUN yum provides '*/applydeltarpm' \  
&& yum -y install deltarpm \  
&& yum -y update \  
&& yum -y install epel-release gcc gcc-c++ make cmake autoconf initscripts
libjpeg libjpeg-devel libpng re2c \  
libpng-devel freetype freetype-devel libxml2 libxml2-devel zlib zlib-devel
glibc glibc-devel glib2 \  
glib2-devel bzip2 bzip2-devel ncurses ncurses-devel libaio numactl numactl-
libs readline-devel curl \  
curl-devel krb5-devel libidn libidn-devel openssl openssl-devel libxslt-devel
libicu-devel libevent-devel \  
libtool libtool-ltdl gd-devel pcre-devel unzip ntpdate expect expat-devel git
wget bison sqlite-devel bc  
  
RUN useradd -M -s /sbin/nologin $RUN_USER  
  
WORKDIR /tmp  
  
#download  
RUN wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz  
RUN wget https://www.openssl.org/source/openssl-1.0.2l.tar.gz  
RUN wget http://mirrors.linuxeye.com/oneinstack/src/pcre-8.41.tar.gz  
RUN wget https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.15.tar.gz  
RUN wget https://curl.haxx.se/download/curl-7.55.1.tar.gz  
RUN wget
http://downloads.sourceforge.net/project/mcrypt/Libmcrypt/2.5.8/libmcrypt-2.5.8.tar.gz  
RUN wget
http://downloads.sourceforge.net/project/mhash/mhash/0.9.9.9/mhash-0.9.9.9.tar.gz  
RUN wget
http://downloads.sourceforge.net/project/mcrypt/MCrypt/2.6.8/mcrypt-2.6.8.tar.gz  
RUN wget http://mirrors.linuxeye.com/oneinstack/src/libiconv-glibc-2.16.patch  
RUN wget http://www.php.net/distributions/php-$PHP_VERSION.tar.gz  
RUN wget
http://mirrors.linuxeye.com/oneinstack/src/libevent-2.0.22-stable.tar.gz  
RUN wget http://ftp.gnu.org/gnu/bison/bison-2.7.1.tar.gz  
  
# 解压  
RUN tar xzf nginx-$NGINX_VERSION.tar.gz  
RUN tar xzf openssl-1.0.2l.tar.gz  
RUN tar xzf pcre-8.41.tar.gz  
RUN tar xzf libevent-2.0.22-stable.tar.gz  
RUN tar xzf php-$PHP_VERSION.tar.gz  
RUN tar xzf mcrypt-2.6.8.tar.gz  
RUN tar xzf mhash-0.9.9.9.tar.gz  
RUN tar xzf libmcrypt-2.5.8.tar.gz  
RUN tar xzf curl-7.55.1.tar.gz  
RUN tar xzf libiconv-1.15.tar.gz  
RUN tar xzf bison-2.7.1.tar.gz  
  
#编译安装  
RUN cd openssl-1.0.2l && pwd && ./config --prefix=$OPENSSL_INSTALL_DIR -fPIC
shared zlib-dynamic && make && make install  
RUN if [ -f "$OPENSSL_INSTALL_DIR/lib/libcrypto.a" ]; then \  
echo "$OPENSSL_INSTALL_DIR/lib" > /etc/ld.so.conf.d/openssl.conf; \  
fi  
  
RUN cd libevent-2.0.22-stable && ./configure && make && make install  
  
RUN cd libiconv-1.15 && ./configure --prefix=/usr/local && make && make
install  
  
RUN cd curl-7.55.1 && ./configure --prefix=/usr/local \--with-
ssl=$OPENSSL_INSTALL_DIR && make && make install  
  
RUN cd libmcrypt-2.5.8 && ./configure --prefix=/usr/local && make && make
install \  
&& cd libltdl && ./configure --enable-ltdl-install && make && make install  
RUN echo '/usr/local/lib' > /etc/ld.so.conf.d/local.conf  
RUN ln -s /usr/local/bin/libmcrypt-config /usr/bin/libmcrypt-config  
  
RUN cd mhash-0.9.9.9 && ./configure && make && make install  
  
RUN export
LD_LIBRARY_PATH=/usr/local/libmcrypt/lib:/usr/local/lib:$LD_LIBRARY_PATH \  
&& cd mcrypt-2.6.8 && ./configure && make && make install  
RUN cd bison-2.7.1 && ./configure && make && make install  
  
# nginx install  
RUN cd nginx-$NGINX_VERSION && pwd \  
&& ./configure --prefix=$NGINX_INSTALL_DIR \--user=$RUN_USER
\--group=$RUN_USER \--with-http_stub_status_module \  
\--with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module
--with-http_realip_module \  
\--with-http_flv_module --with-http_mp4_module --with-
openssl=../openssl-1.0.2l --with-pcre=../pcre-8.41 \  
\--with-pcre-jit \  
&& make && make install \  
&& ln -s $NGINX_INSTALL_DIR/sbin/nginx /usr/local/bin/nginx;  
  
COPY nginx/nginx.conf $NGINX_INSTALL_DIR/conf/nginx.conf  
COPY nginx/rewrite $NGINX_INSTALL_DIR/rewrite  
COPY nginx/vhosts $NGINX_INSTALL_DIR/conf/vhosts  
  
#php install  
RUN ldconfig && cd php-5.6.31 && ./configure \  
\--prefix=$PHP_INSTALL_DIR \  
\--with-config-file-path=$PHP_INSTALL_DIR/etc \  
\--with-config-file-scan-dir=$PHP_INSTALL_DIR/etc/php.d \  
\--with-fpm-user=$RUN_USER \  
\--with-fpm-group=$RUN_USER \  
\--enable-fpm \  
\--enable-opcache \  
\--disable-fileinfo \  
\--with-mysql=mysqlnd \  
\--with-mysqli=mysqlnd \  
\--with-pdo-mysql=mysqlnd \  
\--with-iconv-dir=/usr/local \  
\--with-freetype-dir \  
\--with-jpeg-dir \  
\--with-png-dir \  
\--with-zlib \  
\--with-libxml-dir=/usr \  
\--enable-xml \  
\--disable-rpath \  
\--enable-bcmath \  
\--enable-shmop \  
\--enable-exif \  
\--enable-sysvsem \  
\--enable-inline-optimization \  
\--with-curl=/usr/local \  
\--enable-mbregex \  
\--enable-mbstring \  
\--with-mcrypt \  
\--with-gd \  
\--enable-gd-native-ttf \  
\--with-openssl=$OPENSSL_INSTALL_DIR \  
\--with-mhash \  
\--enable-pcntl \  
\--enable-sockets \  
\--with-xmlrpc \  
\--enable-ftp \  
\--enable-intl \  
\--with-xsl \  
\--with-gettext \  
\--enable-zip \  
\--enable-soap \  
\--disable-debug \  
&& make ZEND_EXTRA_LIBS='-liconv' && make install \  
&& /bin/cp php.ini-production $PHP_INSTALL_DIR/etc/php.ini \  
&& /bin/cp sapi/fpm/init.d.php-fpm /usr/local/bin/php-fpm  
  
RUN mkdir -p $PHP_INSTALL_DIR/etc/php.d  
RUN ln -s $PHP_INSTALL_DIR/bin/php /usr/local/bin/php  
RUN ln -s $PHP_INSTALL_DIR/bin/pear /usr/local/bin/pear  
RUN ln -s $PHP_INSTALL_DIR/bin/pecl /usr/local/bin/pecl  
RUN ln -s $PHP_INSTALL_DIR/bin/phpize /usr/local/bin/phpize  
RUN ln -s $PHP_INSTALL_DIR/bin/php-config /usr/local/bin/php-config  
RUN chmod +x /usr/local/bin/php-fpm  
COPY php/docker-php-ext-enable /usr/bin/docker-php-ext-enable  
RUN chmod +x /usr/bin/docker-php-ext-enable  
RUN pecl install mongo mongodb && docker-php-ext-enable mongo mongodb  
  
#supervisor  
RUN mkdir -p /usr/local/python2.7.12  
RUN wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz  
RUN tar -zxvf Python-2.7.12.tgz  
RUN cd Python-2.7.12 && ./configure --prefix=/usr/local/python2.7.12 -enable-
unicode=ucs4 && make \  
&& make install  
  
RUN rm -rf Python-2.7.12  
RUN rm -f Python-2.7.12.tgz  
RUN rm -f /usr/bin/python  
RUN ln -s /usr/local/python2.7.12/bin/python /usr/bin/python  
RUN ln -s /usr/local/python2.7.12/bin/python-config /usr/bin/python-config  
RUN sed -i "s/\/usr\/bin\/python/\/usr\/bin\/python2/" /usr/bin/yum  
RUN sed -i "s/\/usr\/bin\/python/\/usr\/bin\/python2/"
/usr/libexec/urlgrabber-ext-down  
RUN wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'  
RUN python get-pip.py  
RUN ln -s /usr/local/python2.7.12/bin/pip /usr/bin/pip  
RUN pip install supervisor  
RUN ln -s /usr/local/python2.7.12/bin/supervisord /usr/bin/supervisord  
RUN ln -s /usr/local/python2.7.12/bin/scrapyd /usr/bin/scrapyd  
COPY supervisor/supervisord.conf /etc/supervisord.conf  
RUN mkdir -p /var/run/supervisor  
  
COPY supervisor/supervisord.d /etc/supervisord.d  
COPY php/php-fpm.conf /usr/local/php/etc/php-fpm.conf  
  
EXPOSE 80 443 9000  
WORKDIR $WWWROOT_DIR  
VOLUME ["$WWWROOT_DIR", "$WWWLOGS_DIR"]  
RUN rm -rf /tmp/*  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

