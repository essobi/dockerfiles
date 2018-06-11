FROM ubuntu:16.04  
LABEL maintainer="liuyang.z@hooowl.com"  
  
RUN buildDeps='libpcre3 libpcre3-dev zlib1g-dev libssl-dev libbz2-dev
libcurl4-openssl-dev libjpeg-dev \  
libpng12-dev libfreetype6-dev libpspell-dev librecode-dev libxml2-dev
libmcrypt-dev libcurl3-dev \  
libcurl3 wget unzip build-essential pkg-config libsslcommon2-dev bison libzip-
dev git'; \  
set -x \  
&& apt-get update \  
&& apt-get install -y $buildDeps \  
&& mkdir -p /data/softwares && cd /data/softwares \  
# 下载 NGINX 源码  
&& wget http://nginx.org/download/nginx-1.13.7.tar.gz && tar -xvf
nginx-1.13.7.tar.gz \  
# OpenSSL 库  
&& git clone -b tls1.3-draft-18 --single-branch
https://github.com/openssl/openssl.git openssl \  
# nginx-ct 模块  
#&& wget https://github.com/grahamedgecombe/nginx-ct/archive/master.zip &&
unzip master.zip && mv nginx-ct-master nginx-ct \  
#&& rm -rf master.zip \  
# ngx_brotli 模块  
&& git clone https://github.com/google/ngx_brotli.git && cd ngx_brotli && git
submodule update --init && cd .. \  
# ngx_http_substitutions_filter 模块  
&& wget
https://github.com/yaoweibin/ngx_http_substitutions_filter_module/archive/master.zip
\  
&& unzip master.zip && mv ngx_http_substitutions_filter_module-master
ngx_http_substitutions_filter_module && rm -rf master.zip \  
# 编译安装 re2c, PHP 需要  
&& wget https://sourceforge.net/projects/re2c/files/0.16/re2c-0.16.tar.gz &&
tar -xvf re2c-0.16.tar.gz && cd re2c-0.16 \  
&& ./configure && make && make install \  
# 下载 PHP 源码  
&& cd /data/softwares && wget http://php.net/distributions/php-7.1.12.tar.gz
&& tar -xvf php-7.1.12.tar.gz \  
# 编译安装 NGINX  
&& cd nginx-1.13.7 \  
&& ./configure --add-module=../ngx_brotli \--with-openssl=../openssl --add-
module=../ngx_http_substitutions_filter_module \  
\--with-openssl-opt='enable-tls1_3 enable-weak-ssl-ciphers' \  
\--with-stream \--with-http_v2_module --with-http_ssl_module --with-
http_gzip_static_module \  
&& make && make install \  
&& ln -s /usr/lib/x86_64-linux-gnu/libssl.so /usr/lib \  
# 编译安装 PHP  
&& cd /data/softwares/php-7.1.12 \  
&& ./configure --prefix=/usr/local/php --with-config-file-
path=/usr/local/php/etc --enable-fpm --enable-mysqlnd \  
\--with-mysqli=mysqlnd --with-pdo-mysql=mysqlnd --with-iconv-dir --with-
freetype-dir --with-jpeg-dir \  
\--with-png-dir --with-zlib --with-curl --with-gd --with-xmlrpc --with-openssl
--with-mhash \  
\--with-libxml-dir --with-pear --with-bz2 --with-libzip \  
\--enable-bcmath --enable-shmop --enable-sysvsem --enable-sysvshm --enable-
sysvmsg --enable-mbstring \  
\--enable-sockets --enable-zip --enable-soap --enable-dba --enable-exif \  
\--enable-ftp --enable-opcache \  
&& make && make install \  
&& cp /data/softwares/php-7.1.12/php.ini-production /usr/local/php/etc/php.ini
\  
&& cd /usr/local/php/etc && mv php-fpm.conf.default php-fpm.conf \  
&& mv php-fpm.d/www.conf.default php-fpm.d/www.conf \  
&& sed -Ei 's/user = nobody/user = www-data/g' ./php-fpm.d/www.conf \  
&& sed -Ei 's/group = nobody/group = www-data/g' ./php-fpm.d/www.conf \  
&& sed -Ei 's/;date.timezone =/date.timezone = Asia\/Shanghai/g' php.ini \  
&& chown -R www-data:www-data /usr/local/nginx /usr/local/php \  
&& mkdir -p /usr/local/nginx/conf/conf.d \  
&& rm -rf /data/softwares \  
&& apt-get purge -y --auto-remove build-essential wget unzip  
  
COPY nginx.conf /usr/local/nginx/conf/nginx.conf  
COPY nginx.default.conf /usr/local/nginx/conf/conf.d/default.conf  
COPY autoRun.sh /autoRun.sh  
RUN chmod a+x /autoRun.sh  
  
ENTRYPOINT ["/autoRun.sh"]  
  
CMD ["/bin/bash"]  

