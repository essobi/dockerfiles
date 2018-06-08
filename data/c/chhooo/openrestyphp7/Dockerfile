FROM daocloud.io/centos:7  
RUN yum -y update \  
&& yum install -y \  
epel-release \  
curl make gcc gcc-c++ build-essential procps \  
readline-devel pcre-devel openssl-devel perl \  
systemtap \  
&& yum install -y python-pip mysql mysql-devel  
  
ENV OPENRESTY_VERSION 1.11.2.3  
ENV OPENRESTY_PREFIX /opt/openresty  
ENV NGINX_PREFIX /opt/openresty/nginx  
ENV VAR_PREFIX /var/nginx  
  
# NginX prefix is automatically set by OpenResty to $OPENRESTY_PREFIX/nginx  
# look for $ngx_prefix in
https://github.com/openresty/ngx_openresty/blob/master/util/configure  
# Install openresty command  
RUN cd /root \  
&& echo "==> Downloading OpenResty..." \  
&& curl -sSL
http://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz | tar -xvz
\  
&& echo "==> Configuring OpenResty..." \  
&& cd openresty-* \  
&& readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& echo "using upto $NPROC threads" \  
&& ./configure \  
\--prefix=$OPENRESTY_PREFIX \  
\--http-client-body-temp-path=$VAR_PREFIX/client_body_temp \  
\--http-proxy-temp-path=$VAR_PREFIX/proxy_temp \  
\--http-log-path=$VAR_PREFIX/access.log \  
\--error-log-path=$VAR_PREFIX/error.log \  
\--pid-path=$VAR_PREFIX/nginx.pid \  
\--lock-path=$VAR_PREFIX/nginx.lock \  
\--with-luajit \  
\--with-pcre-jit \  
\--with-ipv6 \  
\--with-http_ssl_module \  
\--without-http_ssi_module \  
\--without-http_userid_module \  
\--without-http_uwsgi_module \  
\--without-http_scgi_module \  
-j${NPROC} \  
&& echo "==> Building OpenResty..." \  
&& make -j${NPROC} \  
&& echo "==> Installing OpenResty..." \  
&& make install \  
&& echo "==> Finishing..." \  
&& ln -sf $NGINX_PREFIX/sbin/nginx /usr/local/bin/nginx \  
&& ln -sf $NGINX_PREFIX/sbin/nginx /usr/local/bin/openresty \  
&& ln -sf $OPENRESTY_PREFIX/bin/resty /usr/local/bin/resty \  
&& ln -sf $OPENRESTY_PREFIX/luajit/bin/luajit-*
$OPENRESTY_PREFIX/luajit/bin/lua \  
&& ln -sf $OPENRESTY_PREFIX/luajit/bin/luajit-* /usr/local/bin/lua \  
&& rm -rf /root/ngx_openresty* \  
&& mkdir /opt/openresty/nginx/conf/conf.d  
  
# Install php7 command  
ADD libmcrypt /root/libmcrypt  
RUN cd /root/libmcrypt \  
&& chmod +x configure \  
&& ./configure --prefix=/usr/lib/libmcrypt \  
&& make && make install  
RUN cd /root \  
&& yum install -y libxml2 libxml2-devel openssl curl-devel \  
libjpeg-devel libpng-devel freetype-devel \  
bzip2 bzip2-devel gmp-devel libicu-devel readline-devel libxslt-devel \  
&& echo "==> Downloading PHP..." \  
&& curl -sSL http://php.net/distributions/php-7.0.8.tar.gz | tar -zxv \  
&& echo "==> Configuring PHP..." \  
&& cd php-7.0.8 \  
&& readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& echo "using upto $NPROC threads" \  
&& ./configure --prefix=/usr/local/php7 \  
\--with-mysql-sock --with-mysqli \  
\--enable-fpm --enable-soap \  
\--with-libxml-dir --with-openssl \  
\--with-mcrypt=/usr/lib/libmcrypt --with-mhash \  
\--with-pcre-regex --with-zlib \  
\--enable-bcmath --with-iconv \  
\--with-bz2 --enable-calendar \  
\--with-curl --with-cdb --enable-dom \  
\--enable-exif --enable-fileinfo \  
\--enable-filter --with-pcre-dir \  
\--enable-ftp --with-gd \  
\--with-openssl-dir --with-jpeg-dir \  
\--with-png-dir --with-zlib-dir \  
\--with-freetype-dir \  
\--enable-gd-native-ttf \  
\--enable-gd-jis-conv --with-gettext \  
\--with-gmp --with-mhash \  
\--enable-json --enable-mbstring \  
\--enable-mbregex \  
\--enable-mbregex-backtrack \  
\--with-libmbfl --with-onig \  
\--enable-pdo --with-pdo-mysql \  
\--with-zlib-dir --with-readline \  
\--enable-session --enable-shmop \  
\--enable-simplexml --enable-sockets \  
\--enable-sysvmsg --enable-sysvsem \  
\--enable-sysvshm --enable-wddx \  
\--with-libxml-dir --with-xsl \  
\--enable-zip \  
\--enable-mysqlnd-compression-support \  
\--with-pear --enable-intl --enable-opcache \  
&& echo "==> Building PHP..." \  
&& make -j${NPROC} \  
&& echo "==> Installing PHP..." \  
&& make install \  
&& ln -sf /usr/local/php7/bin/php /usr/local/bin/php \  
&& cp ./php.ini-development /usr/local/php7/lib/php.ini \  
&& echo -e "zend_extension=/usr/local/php7/lib/php/extensions/no-debug-non-
zts-20151012/opcache.so\nopcache.enable=1\nopcache.enable_cli=1" >>
/usr/local/php7/lib/php.ini \  
&& cp /usr/local/php7/etc/php-fpm.conf.default /usr/local/php7/etc/php-
fpm.conf \  
&& cp /usr/local/php7/etc/php-fpm.d/www.conf.default /usr/local/php7/etc/php-
fpm.d/www.conf \  
&& cp ./sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm \  
&& chmod +x /etc/init.d/php-fpm \  
&& echo "==> Finishing..."  
  
#Install supervisor  
RUN easy_install -i http://pypi.douban.com/simple/ supervisor  
  
ONBUILD RUN rm -rf conf/* html/*  
ONBUILD COPY nginx $NGINX_PREFIX/  
  
#Install Composer  
ADD composer /usr/local/bin/composer  
RUN chmod 755 /usr/local/bin/composer  
  
ADD supervisor /  
  
RUN yum -y install wget \  
&& wget https://phar.phpunit.de/phpunit.phar \  
&& chmod +x phpunit.phar \  
&& mv phpunit.phar /usr/local/bin/phpunit  
  
#Install MongoDB Extension  
RUN yum -y install php-devel \  
&& echo "==> Downloading MongoDB..." \  
&& /usr/local/php7/bin/pecl install mongodb  
  
RUN echo "extension=mongodb.so" >> /usr/local/php7/lib/php.ini \  
&& echo "==> Finishing..."  
#Install git  
RUN yum install -y git  
  
#Install xhprof  
RUN yum install m4 autoconf libpng graphviz -y \  
&& cd /root \  
&& git clone https://github.com/longxinH/xhprof.git ./xhprof \  
&& cd xhprof/extension/ \  
&& /usr/local/php7/bin/phpize \  
&& ./configure --with-php-config=/usr/local/php7/bin/php-config \  
&& make && make install \  
&& echo -e "[xhprof]" >> /usr/local/php7/lib/php.ini \  
&& echo -e "extension = xhprof.so" >> /usr/local/php7/lib/php.ini \  
&& echo -e "xhprof.output_dir = /opt/openresty/nginx/html/xhprof/data" >>
/usr/local/php7/lib/php.ini  
  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
COPY nginx.conf /opt/openresty/nginx/conf/nginx.conf  
  
CMD ["/config/bootstrap.sh"]

